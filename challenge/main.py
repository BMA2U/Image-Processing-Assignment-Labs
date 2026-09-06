import os
import glob
import cv2 as cv
from ocr_engine import load_templates, process_image

if __name__ == "__main__":
    base_dir = "d:/lastYear/imageProcessing/labs/scr/Assignment/challenge"
    templates_dir = os.path.join(base_dir, "templates")
    tests_dir = os.path.join(base_dir, "tests")
    
    print("Loading templates...")
    templates = load_templates(templates_dir)
    print(f"Loaded {len(templates)} templates.")
    
    test_files = glob.glob(os.path.join(tests_dir, "*.*"))
    if not test_files:
        print(f"No test images found in {tests_dir}")
    
    for test_file in test_files:
        print("-" * 30)
        print(f"Processing {test_file}...")
        process_image(test_file, templates)
        
    cv.destroyAllWindows()
