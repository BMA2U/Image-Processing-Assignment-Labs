import cv2 as cv
import numpy as np
import os
import glob

# Constants
NAME_TO_CHAR = {
    'plus': '+',
    'minus': '-',
    'mul': '*',
    'div': '/'
}
for i in range(10):
    NAME_TO_CHAR[str(i)] = str(i)

def non_max_suppression_fast(boxes, overlapThresh):
    """NMS to remove overlapping bounding boxes."""
    if len(boxes) == 0:
        return []
    if type(boxes).__module__ != np.__name__:
        boxes = np.array(boxes)

    pick = []
    x1 = boxes[:, 0].astype(float)
    y1 = boxes[:, 1].astype(float)
    x2 = boxes[:, 2].astype(float)
    y2 = boxes[:, 3].astype(float)
    score = boxes[:, 4].astype(float)

    area = (x2 - x1 + 1) * (y2 - y1 + 1)
    idxs = np.argsort(score)[::-1]

    while len(idxs) > 0:
        last = len(idxs) - 1
        i = idxs[0]
        pick.append(i)

        xx1 = np.maximum(x1[i], x1[idxs[1:]])
        yy1 = np.maximum(y1[i], y1[idxs[1:]])
        xx2 = np.minimum(x2[i], x2[idxs[1:]])
        yy2 = np.minimum(y2[i], y2[idxs[1:]])

        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)

        overlap = (w * h) / area[idxs[1:]]
        idxs = np.delete(idxs, np.concatenate(([0], np.where(overlap > overlapThresh)[0] + 1)))
    return pick

def rotate_image(image, angle):
    """Rotate image around its center."""
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv.INTER_LINEAR, borderValue=255)
    return result

def preprocess_image(image, is_template=False):
    """Grayscale, Blur, and Binarize with Morphology."""
    if len(image.shape) == 3:
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    else:
        gray = image.copy()
        
    if not is_template:
        blur = cv.GaussianBlur(gray, (5, 5), 0)
    else:
        blur = gray
        
    # Invert so objects are white, background is black
    _, thresh = cv.threshold(blur, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
    
    # Morphological Operation to thicken thin parts like the minus sign
    if not is_template:
        kernel = np.ones((2, 2), np.uint8)
        thresh = cv.dilate(thresh, kernel, iterations=1)
        
    return thresh

def load_templates(templates_dir):
    """Load and preprocess template images."""
    templates = {}
    for filepath in glob.glob(os.path.join(templates_dir, "*.png")):
        name = os.path.splitext(os.path.basename(filepath))[0]
        char = NAME_TO_CHAR.get(name, name)
        
        img = cv.imread(filepath, cv.IMREAD_GRAYSCALE)
        if img is not None:
            processed = preprocess_image(img, is_template=True)
            templates[char] = processed
    return templates

def process_image(image_path, templates):
    """Process a single image using Multi-Scale Template Matching."""
    img = cv.imread(image_path)
    if img is None:
        print(f"Error loading {image_path}")
        return
        
    processed_img = preprocess_image(img)
    detections = []
    
    # We loop over different scales to handle different sizes
    scales = np.linspace(0.8, 1.5, 8)
    angles = range(-15, 16, 5)
    threshold = 0.60
    
    for char, template in templates.items():
        tH_orig, tW_orig = template.shape
        
        for scale in scales:
            # Resize template (Multi-Scale)
            tW = int(tW_orig * scale)
            tH = int(tH_orig * scale)
            
            if tW == 0 or tH == 0:
                continue
                
            scaled_template = cv.resize(template, (tW, tH))
            
            # Ensure the scaled template is not larger than the input image
            if scaled_template.shape[0] > processed_img.shape[0] or scaled_template.shape[1] > processed_img.shape[1]:
                continue
                
            for angle in angles:
                rotated_template = rotate_image(scaled_template, angle)
                
                result = cv.matchTemplate(processed_img, rotated_template, cv.TM_CCOEFF_NORMED)
                y_locs, x_locs = np.where(result >= threshold)
                
                for (x, y) in zip(x_locs, y_locs):
                    score = result[y, x]
                    detections.append([x, y, x + rotated_template.shape[1], y + rotated_template.shape[0], score, char])
                    
    # Non-Maximum Suppression
    if len(detections) > 0:
        picks = non_max_suppression_fast(detections, overlapThresh=0.3)
        final_detections = [detections[p] for p in picks]
    else:
        final_detections = []
        
    final_detections.sort(key=lambda x: x[0])
    
    output_img = img.copy()
    equation = ""
    
    for det in final_detections:
        x1, y1, x2, y2, score, label = det
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        equation += label
        cv.rectangle(output_img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv.putText(output_img, f"{label} ({score:.2f})", (x1, y1 - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        
    print(f"[{os.path.basename(image_path)}] Detected Equation: {equation}")
    
    try:
        if equation:
            result_val = eval(equation)
            print(f"Result: {result_val}")
            cv.putText(output_img, f"{equation} = {result_val}", (20, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        else:
            print("No equation found.")
    except Exception as e:
        print(f"Failed to evaluate equation: {e}")
        
    cv.imshow(f"Output: {os.path.basename(image_path)}", output_img)
    cv.waitKey(0)
