import os
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = BASE_DIR
CONVERSION_DIR = os.path.join(IMAGE_DIR, "conversion_samples")

os.makedirs(CONVERSION_DIR, exist_ok=True)

ARTIFACT_NETWORK = r"C:\Users\Bassem\.gemini\antigravity-ide\brain\fba6d675-4d6c-43ac-9c12-11c31a014de1\network_jpg_1785094448139.png"
ARTIFACT_PERSON = r"C:\Users\Bassem\.gemini\antigravity-ide\brain\fba6d675-4d6c-43ac-9c12-11c31a014de1\man_face_1785094987451.png"

network_out = os.path.join(IMAGE_DIR, "network.jpg")
person_out = os.path.join(IMAGE_DIR, "person1.jpg")

if os.path.exists(ARTIFACT_NETWORK):
    img = Image.open(ARTIFACT_NETWORK).convert("RGB")
    img.save(network_out, "JPEG")
    img.save(os.path.join(os.path.dirname(IMAGE_DIR), "network.jpg"), "JPEG")

if os.path.exists(ARTIFACT_PERSON):
    img = Image.open(ARTIFACT_PERSON).convert("RGB")
    img.save(person_out, "JPEG")

for i in range(1, 4):
    sample_path = os.path.join(CONVERSION_DIR, f"sample_{i}.png")
    sample_img = Image.new("RGB", (300, 300), color=((i*70)%255, (i*110)%255, (i*150)%255))
    sample_img.save(sample_path)
