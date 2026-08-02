import os
from PIL import Image

src_folder = 'image/conversion_samples'
out_folder = 'image/converted_output'

if not os.path.exists(out_folder):
    os.makedirs(out_folder)

for filename in os.listdir(src_folder):
    if filename.endswith('.png') or filename.endswith('.jpg'):
        img_path = os.path.join(src_folder, filename)
        img = Image.open(img_path).convert('RGB')
        
        name = os.path.splitext(filename)[0]
        save_path = os.path.join(out_folder, name + '.jpg')
        img.save(save_path, 'JPEG')
        print(f"Saved: {save_path}")
