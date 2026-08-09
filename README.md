# 🖼️ Image Processing — Assignment Labs

**Bassem Al-Taheri**

A collection of Python lab assignments for an **Image Processing** course.  
Each lab explores a different set of techniques using **OpenCV**, **Pillow (PIL)**, **NumPy**, and **Matplotlib**.

---

## 📂 Project Structure

```
Assignment/
├── lab1/
│   ├── assignment_1_comparison.md      # Written report: OpenCV vs Pillow
│   ├── assignment_2_drawing_pillow.py  # Drawing shapes & text with Pillow
│   ├── assignment_3_batch_convert.py   # Batch image format conversion
│   ├── assignment_4_face_bbox.py       # Face bounding-box with OpenCV
│   └── image/                          # Lab 1 assets & outputs
│       ├── conversion_samples/         # Source images for batch conversion
│       ├── converted_output/           # Converted JPEG outputs
│       ├── person1.jpg                 # Input for face bbox
│       └── person_with_bbox.jpg        # Output with drawn bbox
│
├── lab2/
│   ├── assignment1.py                  # Image Transformation Tool (GUI)
│   ├── assignment2.py                  # Planet extraction & swap
│   ├── assignment3.py                  # Product background replacement
│   └── images/                         # Lab 2 assets & outputs
│       ├── varese.jpg                  # Input for transformation tool
│       ├── planet_glow.jpg             # Input for planet swap
│       ├── background.png              # Background for product composite
│       ├── product_no_bg.png           # Product with transparent background
│       └── product_result.jpg          # Final composited output
│
├── lab3/
│   ├── main.py                         # Point transformations runner/demo
│   ├── point_transformations.py        # Core transformation functions
│   └── images/                         # Lab 3 assets & outputs
│       ├── img1.png                    # Input for transformations demo
│       ├── background.png              # Background image
│       ├── product.png                 # Product image
│       ├── product_no_bg.png           # Product with no background
│       ├── product_result.jpg          # Composited result
│       ├── varese.jpg                  # Varese city image
│       └── img*.png, planet_glow.jpg   # Other lab image assets
│
└── README.md
```

---

## 🧪 Lab 1 — Fundamentals

### Assignment 1 · OpenCV vs Pillow Comparison

A detailed **written report** (`assignment_1_comparison.md`) comparing:

| Aspect              | OpenCV                          | Pillow                        |
| -------------------- | ------------------------------- | ----------------------------- |
| Color order          | BGR                             | RGB                           |
| Data representation  | NumPy `ndarray`                 | `PIL.Image` object            |
| Performance          | C/C++ core, real-time ready     | Great for everyday operations |
| Video support        | Full capture/record pipeline    | Not supported                 |
| Drawing API          | `cv2.rectangle`, `cv2.putText`… | `ImageDraw` module            |

### Assignment 2 · Drawing with Pillow

Creates a **512 × 512** canvas and draws lines, rectangles, ellipses, and text using `PIL.ImageDraw`.

```bash
python lab1/assignment_2_drawing_pillow.py
```

### Assignment 3 · Batch Format Conversion

Scans `lab1/image/conversion_samples/` for `.png` and `.jpg` files and converts them all to **JPEG** in `lab1/image/converted_output/`.

```bash
python lab1/assignment_3_batch_convert.py
```

### Assignment 4 · Face Bounding Box

Draws a **green bounding box** and a name label on a face in an image using OpenCV drawing functions.

```bash
python lab1/assignment_4_face_bbox.py
```

---

## 🧪 Lab 2 — Transformations & Compositing

### Assignment 1 · Image Transformation Tool (GUI)

A **Tkinter** desktop application that lets the user pick an operation from a dropdown and enter parameters:

| Operation   | Parameters               |
| ----------- | ------------------------ |
| **Crop**    | Y1, Y2, X1, X2          |
| **Resize**  | Width, Height            |
| **Rotate**  | Angle (degrees)          |
| **Translate** | TX, TY (pixel offsets) |

```bash
python lab2/assignment1.py
```

### Assignment 2 · Planet Extraction & Swap

Crops **three planets** from `planet_glow.jpg`, then **swaps their positions** and displays the original alongside the result with Matplotlib.

```bash
python lab2/assignment2.py
```

### Assignment 3 · Product Background Replacement

Composites a transparent-background product image onto a new blurred background using Pillow:

1. Loads `background.png` and `product_no_bg.png`
2. Resizes the product to 50 % of the background
3. Enhances brightness and applies Gaussian blur to the background
4. Centers and pastes the product using its alpha channel as a mask
5. Saves the final result as `product_result.jpg`

```bash
python lab2/assignment3.py
```

---

## 🧪 Lab 3 — Point Transformations

### Assignment 1 · Image Path Existence Checking

A utility function to verify if an image file exists at a given path before loading, avoiding runtime crashes.

### Assignment 2 · Negative Transformation

Inverts the pixel values of the input image. For an 8-bit image, the formula is:
$$s = 255 - r$$
where $r$ is the input intensity and $s$ is the output intensity.

### Assignment 3 · Logarithmic Transformation

Expands values of dark pixels in an image while compressing higher-level values. The formula is:
$$s = c \log(1 + r)$$
where $c$ is a scaling constant chosen so that the maximum output value is 255 ($c = 255 / \log(1 + \max(r))$).

### Assignment 4 · Histogram Equalization

Enhances the contrast of an image by stretching its intensity range. Color images are automatically converted to grayscale before applying the equalization.
Displays a $2 \times 2$ grid showing:
1. Original Grayscale Image
2. Histogram of the Original Image
3. Equalized Grayscale Image
4. Histogram of the Equalized Image

```bash
python lab3/main.py
```

---

## ⚙️ Requirements

- **Python 3.8+**
- [OpenCV](https://pypi.org/project/opencv-python/) — `pip install opencv-python`
- [Pillow](https://pypi.org/project/Pillow/) — `pip install Pillow`
- [NumPy](https://pypi.org/project/numpy/) — `pip install numpy`
- [Matplotlib](https://pypi.org/project/matplotlib/) — `pip install matplotlib`

**Quick install:**

```bash
pip install opencv-python Pillow numpy matplotlib
```

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/BMA2U/Image-Processing-Assignment-Labs.git
cd Image-Processing-Assignment-Labs

# Install dependencies
pip install -r requirements.txt   # or use the pip command above

# Run any assignment
python lab1/assignment_2_drawing_pillow.py
python lab2/assignment1.py
python lab3/main.py
```

> **Note:** Make sure to run scripts from the repository root so relative image paths resolve correctly.

---

## 📝 License

This project is for **educational purposes** as part of an Image Processing course.
