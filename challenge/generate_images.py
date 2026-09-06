import cv2 as cv
import numpy as np
import os
import random

# Constants
FONTS = cv.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 1.5
THICKNESS = 3
TEMPLATE_SIZE = (50, 50)
CHARACTERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/']

# Mapping for file names since '*' and '/' can't be used in filenames
CHAR_NAMES = {
    '+': 'plus',
    '-': 'minus',
    '*': 'mul',
    '/': 'div'
}

def create_template(char):
    """Generate a clean template image for a specific character."""
    # Create white background
    img = np.ones((TEMPLATE_SIZE[1], TEMPLATE_SIZE[0]), dtype=np.uint8) * 255
    
    # Get text size to center it
    text_size = cv.getTextSize(char, FONTS, FONT_SCALE, THICKNESS)[0]
    text_x = (TEMPLATE_SIZE[0] - text_size[0]) // 2
    text_y = (TEMPLATE_SIZE[1] + text_size[1]) // 2
    
    # Draw black text
    cv.putText(img, char, (text_x, text_y), FONTS, FONT_SCALE, 0, THICKNESS)
    return img

def add_noise(image):
    """Add Gaussian noise to a color image."""
    row, col, ch = image.shape
    mean = 0
    var = 400 # High variance for noticeable noise
    sigma = var**0.5
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy = image + gauss
    return np.clip(noisy, 0, 255).astype(np.uint8)

def rotate_image(image, angle):
    """Rotate an image with white background."""
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv.INTER_LINEAR, borderValue=(255, 255, 255))
    return result

def generate_test_image(equation="5 + 3 * 2"):
    """Generate a noisy, colored image with the given equation."""
    # Base canvas (colored background, light gray)
    canvas = np.ones((150, 400, 3), dtype=np.uint8) * 200 
    
    x_offset = 20
    for char in equation:
        if char == ' ':
            x_offset += 15
            continue
            
        # Create character image (BGR)
        char_img = np.ones((TEMPLATE_SIZE[1], TEMPLATE_SIZE[0], 3), dtype=np.uint8) * 255
        
        # Random color for text
        color = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
        
        text_size = cv.getTextSize(char, FONTS, FONT_SCALE, THICKNESS)[0]
        text_x = (TEMPLATE_SIZE[0] - text_size[0]) // 2
        text_y = (TEMPLATE_SIZE[1] + text_size[1]) // 2
        
        cv.putText(char_img, char, (text_x, text_y), FONTS, FONT_SCALE, color, THICKNESS)
        
        # Apply random rotation (-15 to 15 degrees)
        angle = random.randint(-15, 15)
        char_img = rotate_image(char_img, angle)
        
        # Place on canvas
        y_offset = 50 + random.randint(-5, 5)
        
        # Paste ignoring white background (naive blending)
        roi = canvas[y_offset:y_offset+TEMPLATE_SIZE[1], x_offset:x_offset+TEMPLATE_SIZE[0]]
        mask = cv.cvtColor(char_img, cv.COLOR_BGR2GRAY) < 250
        roi[mask] = char_img[mask]
        
        x_offset += TEMPLATE_SIZE[0] + 5

    # Add noise
    noisy_canvas = add_noise(canvas)
    return noisy_canvas

if __name__ == "__main__":
    base_dir = "d:/lastYear/imageProcessing/labs/scr/Assignment/challenge"
    templates_dir = os.path.join(base_dir, "templates")
    
    os.makedirs(templates_dir, exist_ok=True)
    
    # 1. Generate and save templates
    for char in CHARACTERS:
        img = create_template(char)
        name = CHAR_NAMES.get(char, char)
        cv.imwrite(os.path.join(templates_dir, f"{name}.png"), img)
        print(f"Generated template for {char}")
        
    tests_dir = os.path.join(base_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)
    
    # 2. Generate and save a test image
    eq1 = "8 * 4 + 7"
    test_img = generate_test_image(eq1)
    cv.imwrite(os.path.join(tests_dir, "test_1.png"), test_img)
    print(f"Generated test image for equation: {eq1}")
    
    eq2 = "9 - 2 / 1"
    test_img2 = generate_test_image(eq2)
    cv.imwrite(os.path.join(tests_dir, "test_2.png"), test_img2)
    print(f"Generated test image for equation: {eq2}")
