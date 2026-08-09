import cv2 as cv
import numpy as np
import point_transformations as pt
def main():
    print("==================================================")
    print("     Assignment 3: Point Transformations Dem      ")
    print("==================================================")
    
    # 1. Test image path validation
    valid_path = "./images/img1.png"
    invalid_path = "./images/non_existent.png"
    
    print(f"\n1. Testing image existence checking:")
    print(f"   Checking '{invalid_path}': {'Found' if pt.check_image_exists(invalid_path) else 'Not Found (Correct)'}")
    print(f"   Checking '{valid_path}': {'Found (Correct)' if pt.check_image_exists(valid_path) else 'Not Found'}")
    
    if not pt.check_image_exists(valid_path):
        print(f"Error: Target image '{valid_path}' could not be found.")
        return
        
    # Read the image
    image = cv.imread(valid_path)
    
    # 2. Test Negative Transformation
    print("\n2. Applying Negative Transformation...")
    neg_image = pt.negative_transform(image)
    
    # Display Negative Transform results (1 row, 2 columns)
    print("   Displaying Negative Transform results...")
    pt.display_images(
        images=[image, neg_image],
        rows=1,
        cols=2,
        titles=["Original Image", "Negative Image (255 - r)"],
        figsize=(10, 5),
        fig_title="Negative Transformation"
    )
    
    # 3. Test Logarithmic Transformation
    print("\n3. Applying Logarithmic Transformation...")
    log_image = pt.log_transform(image)
    
    # Display Log Transform results (1 row, 2 columns)
    print("   Displaying Logarithmic Transform results...")
    pt.display_images(
        images=[image, log_image],
        rows=1,
        cols=2,
        titles=["Original Image", "Log Image (c * log(1 + r))"],
        figsize=(10, 5),
        fig_title="Logarithmic Transformation "
    )
    
    # 4. Test Histogram Equalization
    # For a clear contrast difference, we can use a low-contrast image if one exists,
    # or just use the same image 'img1.png'.
    print("\n4. Applying Histogram Equalization...")
    hist_before, hist_after, eq_image = pt.histogram_equalize(image)
    
    # Get original image as grayscale to correspond to the equalized version
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY) if len(image.shape) == 3 else image
    
    # Display Histogram Equalization results (2 rows, 2 columns)
    # Grid order: Original Gray, Original Hist, Equalized Gray, Equalized Hist
    print("   Displaying Histogram Equalization results in a 2x2 grid...")
    pt.display_images(
        images=[gray_image, hist_before, eq_image, hist_after],
        rows=2,
        cols=2,
        titles=[
            "Original Grayscale", "Original Histogram",
            "Equalized Image", "Equalized Histogram"
        ],
        figsize=(12, 10),
        fig_title="Histogram Equalization "
    )
    
    print("\n==================================================")
    print("             Demo Completed Successfully          ")
    print("==================================================")
if __name__ == "__main__":
    main()
