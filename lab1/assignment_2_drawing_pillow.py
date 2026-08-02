from PIL import Image, ImageDraw

img = Image.new('RGB', (512, 512), (255, 255, 255))
draw = ImageDraw.Draw(img)

draw.line([(0, 0), (400, 400)], fill=(0, 255, 0), width=2)
draw.rectangle([(100, 100), (500, 500)], outline=(255, 0, 0), width=5)
draw.ellipse([(156, 156), (356, 356)], outline=(255, 255, 0), width=3)
draw.text((0, 256), "Hello World", fill=(0, 255, 255))

img.save('pinting_pillow.png')
try:
    img.show()
except Exception:
    pass
