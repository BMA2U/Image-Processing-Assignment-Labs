import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os
from typing import Tuple, List, Optional, Union

def check_image_exists(image_path: str) -> bool:
    """
    Checks if an image file exists at the given path.
    
    Parameters:
        image_path (str): The file path to verify.
        
    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.exists(image_path)

def negative_transform(image: np.ndarray) -> np.ndarray:
    """
    Applies the negative transformation to the input image.
    Formula: s = L - 1 - r (for 8-bit image, s = 255 - r)
    
    Parameters:
        image (np.ndarray): The input image.
        
    Returns:
        np.ndarray: The negative-transformed image.
    """
    return 255 - image

def log_transform(image: np.ndarray) -> np.ndarray:
    """
    Applies the logarithmic transformation to the input image.
    Formula: s = c * log(1 + r)
    
    Parameters:
        image (np.ndarray): The input image.
        
    Returns:
        np.ndarray: The log-transformed image (8-bit uint8).
    """
    image_float = np.float32(image)
    max_val = np.max(image_float)
    if max_val == 0:
        return np.zeros_like(image, dtype=np.uint8)
    
    c = 255.0 / np.log(1.0 + max_val)
    image_log = c * np.log(1.0 + image_float)
    return np.uint8(image_log)

def histogram_equalize(image: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Performs histogram equalization on the input image.
    If the image is color (BGR), it is first converted to grayscale.
    
    Parameters:
        image (np.ndarray): The input image.
        
    Returns:
        Tuple[np.ndarray, np.ndarray, np.ndarray]:
            - hist_before: Histogram before equalization.
            - hist_after: Histogram after equalization.
            - equalized_image: The resulting equalized grayscale image.
    """
    # Convert to grayscale if it is a color image
    if len(image.shape) == 3 and image.shape[2] == 3:
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    else:
        gray = image.copy()
        
    # Calculate histogram before equalization
    hist_before = cv.calcHist([gray], [0], None, [256], [0, 256])
    
    # Equalize histogram
    equalized_image = cv.equalizeHist(gray)
    
    # Calculate histogram after equalization
    hist_after = cv.calcHist([equalized_image], [0], None, [256], [0, 256])
    
    return hist_before, hist_after, equalized_image

def display_images(images: List[Union[np.ndarray, List]], rows: int, cols: int, titles: Optional[List[str]] = None, figsize: Tuple[int, int] = (12, 8), fig_title: Optional[str] = None) -> None:
    """
    Dynamically displays a grid of images and histograms using Matplotlib.
    It automatically detects if an item is a histogram (1D array of 256 values)
    and plots it accordingly, while images are rendered as subplots.
    
    Parameters:
        images (List): List of images (numpy arrays) or histograms (numpy arrays / list).
        rows (int): Number of rows in the display grid.
        cols (int): Number of columns in the display grid.
        titles (List[str], optional): Titles for each subplot.
        figsize (Tuple[int, int]): Total figure size for the Matplotlib window.
        fig_title (str, optional): Overall title for the figure.
    """
    fig, axes = plt.subplots(rows, cols, figsize=figsize)
    
    if fig_title:
        fig.suptitle(fig_title, fontsize=14, fontweight='bold')
        try:
            fig.canvas.manager.set_window_title(fig_title)
        except Exception:
            pass
    
    # Handle single subplot case where axes is not an array
    if rows == 1 and cols == 1:
        axes = np.array([axes])
    else:
        axes = np.array(axes).flatten()
        
    for i in range(rows * cols):
        if i < len(images):
            item = images[i]
            title = titles[i] if (titles and i < len(titles)) else f"Item {i+1}"
            ax = axes[i]
            
            # Detect if the item is a histogram
            # Typically a histogram calculated by cv.calcHist has shape (256, 1) or is a 1D array of size 256
            is_hist = False
            if isinstance(item, np.ndarray):
                if item.ndim == 1 and len(item) == 256:
                    is_hist = True
                elif item.ndim == 2 and item.shape[0] == 256 and item.shape[1] == 1:
                    is_hist = True
                    
            if is_hist:
                ax.plot(item, color='crimson', linewidth=1.5)
                ax.set_title(title, fontsize=10, fontweight='bold')
                ax.set_xlabel("Pixel Value", fontsize=8)
                ax.set_ylabel("Frequency", fontsize=8)
                ax.grid(True, linestyle='--', alpha=0.5)
            else:
                # Render as an image
                if isinstance(item, np.ndarray):
                    if len(item.shape) == 3:
                        # OpenCV loads BGR, Matplotlib expects RGB
                        img_rgb = cv.cvtColor(item, cv.COLOR_BGR2RGB)
                        ax.imshow(img_rgb)
                    else:
                        # Grayscale image
                        ax.imshow(item, cmap='gray')
                ax.set_title(title, fontsize=10, fontweight='bold')
                ax.axis('off')
        else:
            # Hide unused subplot axes
            axes[i].axis('off')
            
    if fig_title:
        plt.tight_layout(rect=[0, 0, 1, 0.93])
    else:
        plt.tight_layout()
    plt.show()
