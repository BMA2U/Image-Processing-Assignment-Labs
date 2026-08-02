from PIL import Image, ImageFilter, ImageEnhance

# Load the background image
bg = Image.open('./images/background.png').convert('RGBA')

# Load the product image (PNG with transparency)
product = Image.open('./images/product_no_bg.png').convert('RGBA')

# Get background size
bg_w, bg_h = bg.size

# Resize product to fit nicely on the background
product_size = (int(bg_w * 0.5), int(bg_h * 0.5))
product = product.resize(product_size, Image.LANCZOS)

# Enhance product brightness slightly
enhancer = ImageEnhance.Brightness(product)
product = enhancer.enhance(1.1)

# Calculate center position for the product
p_w, p_h = product.size
x = (bg_w - p_w) // 2
y = (bg_h - p_h) // 2

# Add slight blur to background for depth effect
bg_blurred = bg.filter(ImageFilter.GaussianBlur(radius=2))

# Paste product onto blurred background using alpha channel as mask
bg_blurred.paste(product, (x, y), product)

# Convert to RGB and save/show
final = bg_blurred.convert('RGB')

# Save the result
final.save('./images/product_result.jpg', quality=95)

# Show the final image
final.show()

print("Product image saved to ./images/product_result.jpg")
