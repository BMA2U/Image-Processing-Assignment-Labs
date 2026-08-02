import cv2 as cv
import numpy as np
import tkinter as tk
from tkinter import messagebox

# Read the image
img = cv.imread('./images/varese.jpg')

if img is None:
    print("Image not found. Please check the path.")
    exit()

# --- Crop Operation ---
def crop_image():
    try:
        y1 = int(entry_y1.get())
        y2 = int(entry_y2.get())
        x1 = int(entry_x1.get())
        x2 = int(entry_x2.get())
        # Validate that coordinates produce a valid region
        if y2 <= y1 or x2 <= x1:
            messagebox.showerror("Error", "Y2 must be > Y1 and X2 must be > X1")
            return
        (h, w) = img.shape[:2]
        if y1 < 0 or x1 < 0 or y2 > h or x2 > w:
            messagebox.showerror("Error", f"Coordinates out of range. Image size: {w}x{h}")
            return
        result = img[y1:y2, x1:x2]
        cv.imshow('Cropped Image', result)
        cv.waitKey(0)
        cv.destroyAllWindows()
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# --- Resize Operation ---
def resize_image():
    try:
        w = int(entry_width.get())
        h = int(entry_height.get())
        # Validate positive dimensions
        if w <= 0 or h <= 0:
            messagebox.showerror("Error", "Width and Height must be > 0")
            return
        result = cv.resize(img, (w, h))
        cv.imshow('Resized Image', result)
        cv.waitKey(0)
        cv.destroyAllWindows()
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# --- Rotate Operation ---
def rotate_image():
    try:
        angle = float(entry_angle.get())
        (h, w) = img.shape[:2]
        center = (w // 2, h // 2)
        M = cv.getRotationMatrix2D(center, angle, 1.0)
        result = cv.warpAffine(img, M, (w, h))
        cv.imshow('Rotated Image', result)
        cv.waitKey(0)
        cv.destroyAllWindows()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# --- Translate Operation ---
def translate_image():
    try:
        tx = int(entry_tx.get())
        ty = int(entry_ty.get())
        (h, w) = img.shape[:2]
        M = np.float32([[1, 0, tx], [0, 1, ty]])
        result = cv.warpAffine(img, M, (w, h))
        cv.imshow('Translated Image', result)
        cv.waitKey(0)
        cv.destroyAllWindows()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# --- Show fields based on selected operation ---
def show_fields():
    # Hide all frames first
    frame_crop.pack_forget()
    frame_resize.pack_forget()
    frame_rotate.pack_forget()
    frame_translate.pack_forget()

    choice = operation.get()

    if choice == "Crop":
        frame_crop.pack(pady=10)
    elif choice == "Resize":
        frame_resize.pack(pady=10)
    elif choice == "Rotate":
        frame_rotate.pack(pady=10)
    elif choice == "Translate":
        frame_translate.pack(pady=10)

# --- Build the GUI window ---
root = tk.Tk()
root.title("Image Processing Tool")
root.geometry("400x350")
root.resizable(False, False)

# Operation selection
tk.Label(root, text="Select Operation:", font=("Arial", 12, "bold")).pack(pady=10)

operation = tk.StringVar(value="Crop")
options = ["Crop", "Resize", "Rotate", "Translate"]
menu = tk.OptionMenu(root, operation, *options, command=lambda _: show_fields())
menu.config(width=20)
menu.pack()

# --- Crop Frame ---
frame_crop = tk.Frame(root)
tk.Label(frame_crop, text="Y1:").grid(row=0, column=0)
entry_y1 = tk.Entry(frame_crop, width=8)
entry_y1.grid(row=0, column=1, padx=5)

tk.Label(frame_crop, text="Y2:").grid(row=0, column=2)
entry_y2 = tk.Entry(frame_crop, width=8)
entry_y2.grid(row=0, column=3, padx=5)

tk.Label(frame_crop, text="X1:").grid(row=1, column=0, pady=5)
entry_x1 = tk.Entry(frame_crop, width=8)
entry_x1.grid(row=1, column=1, padx=5)

tk.Label(frame_crop, text="X2:").grid(row=1, column=2)
entry_x2 = tk.Entry(frame_crop, width=8)
entry_x2.grid(row=1, column=3, padx=5)

tk.Button(frame_crop, text="Apply Crop", command=crop_image).grid(row=2, column=0, columnspan=4, pady=10)

# --- Resize Frame ---
frame_resize = tk.Frame(root)
tk.Label(frame_resize, text="Width:").grid(row=0, column=0)
entry_width = tk.Entry(frame_resize, width=8)
entry_width.grid(row=0, column=1, padx=5)

tk.Label(frame_resize, text="Height:").grid(row=0, column=2)
entry_height = tk.Entry(frame_resize, width=8)
entry_height.grid(row=0, column=3, padx=5)

tk.Button(frame_resize, text="Apply Resize", command=resize_image).grid(row=1, column=0, columnspan=4, pady=10)

# --- Rotate Frame ---
frame_rotate = tk.Frame(root)
tk.Label(frame_rotate, text="Angle:").grid(row=0, column=0)
entry_angle = tk.Entry(frame_rotate, width=10)
entry_angle.grid(row=0, column=1, padx=5)

tk.Button(frame_rotate, text="Apply Rotate", command=rotate_image).grid(row=1, column=0, columnspan=2, pady=10)

# --- Translate Frame ---
frame_translate = tk.Frame(root)
tk.Label(frame_translate, text="TX:").grid(row=0, column=0)
entry_tx = tk.Entry(frame_translate, width=8)
entry_tx.grid(row=0, column=1, padx=5)

tk.Label(frame_translate, text="TY:").grid(row=0, column=2)
entry_ty = tk.Entry(frame_translate, width=8)
entry_ty.grid(row=0, column=3, padx=5)

tk.Button(frame_translate, text="Apply Translate", command=translate_image).grid(row=1, column=0, columnspan=4, pady=10)

# Show default fields
show_fields()

# Run the GUI
root.mainloop()
