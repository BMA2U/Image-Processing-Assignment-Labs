# 🧮 OCR Challenge Using Spatial Filters

This project aims to extract numbers (0-9) and mathematical operators (+, -, *, /) from noisy and rotated images, construct the equation, and evaluate the final result.

**Core Constraint:** The challenge strictly prohibits the use of any AI or Machine Learning libraries (like Tesseract or Neural Networks). The solution must rely entirely on **Classical Image Processing and Spatial Filters**.

---

## 📂 Project Structure

- `generate_images.py`: A script to generate the base "Templates" and create noisy test images with random colors and rotations to simulate real-world complexity.
- `ocr_engine.py`: The core engine containing all advanced filtering and matching algorithms.
- `main.py`: The entry point script that calls the engine and runs it on the `tests/` directory.

---

## 🛠️ Techniques Used & Why (What & Why)

Given the constraint to use only filters, the system was built using **Template Matching**. Here are the step-by-step techniques applied:

1. **Grayscale Conversion & Otsu's Thresholding:**
   - **Why:** To reduce data dimensionality, remove distracting colors, and binarize the image (pure black and white) to highlight character edges and make matching easier.
2. **Gaussian Blur:**
   - **Why:** To smooth out random (Gaussian) noise in the test images so it doesn't degrade the matching score.
3. **Morphological Dilation:**
   - **Why:** Thin characters like the minus sign (`-`) might disappear due to noise and blurring. Dilation "thickens" these characters to ensure they are preserved for matching.
4. **Normalized Cross-Correlation (`cv2.matchTemplate`):**
   - **Why:** This algorithm acts as a spatial filter that slides a "template" of a character across the image and calculates a correlation score. Templates were rotated at multiple angles to handle character rotation.
5. **Multi-Scale Matching:**
   - **Why:** To solve the issue of characters in the image being slightly larger or smaller than the base template. The system dynamically scales the templates up and down to find the best match.
6. **Non-Maximum Suppression (NMS):**
   - **Why:** When a template matches a character, it often triggers high scores on multiple adjacent pixels (resulting in overlapping bounding boxes). NMS filters out the duplicates and keeps only the most accurate bounding box.

---

## ⚠️ Limitations & Flaws

While the system performs exceptionally well on printed fonts similar to the templates, classical Template Matching has fatal flaws in real-world scenarios:

1. **Extreme Font Sensitivity:**
   - The system relies on strict pixel-shape matching. If the image contains handwritten text or a completely different font, the filter will fail to recognize it (as seen when testing on external images like `img1.jpg`).
2. **Scale Limits:**
   - Despite adding Multi-Scale matching, it only works within a predefined range (e.g., 80% to 150%). If the text is massive or tiny, the system will fail.
3. **High Computational Cost:**
   - Scanning every pixel in the image using 14 different templates, across 7 different rotation angles, and 8 different scales makes the algorithm extremely slow compared to modern AI feature-extraction methods.
4. **Fragility of Thin Objects:**
   - Symbols made of very thin lines (`-`, `/`, `=`) are highly vulnerable to distortion and noise, often leading them to be ignored as background noise.

---
*This challenge serves as a practical demonstration of both the power and the limitations of classical spatial filters in image processing.*
