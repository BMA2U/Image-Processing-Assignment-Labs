import cv2 as cv
import matplotlib.pyplot as plt

# Read the planets image
image = cv.imread("./images/planet_glow.jpg")
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

# Make a copy for the result
result = image.copy()

# Planet crop size
w = 150
h = 150

# Coordinates for each planet
x1, y1 = 40, 150
x2, y2 = 210, 0
x3, y3 = 430, 150

# Crop 3 planets from the image
planet1 = image[y1:y1+h, x1:x1+w].copy()
planet2 = image[y2:y2+h, x2:x2+w].copy()
planet3 = image[y3:y3+h, x3:x3+w].copy()

# Swap the planets in the result image
result[y2:y2+h, x2:x2+w] = planet1
result[y3:y3+h, x3:x3+w] = planet2
result[y1:y1+h, x1:x1+w] = planet3

# Display original and result side by side
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original")

plt.subplot(1, 2, 2)
plt.imshow(result)
plt.title("Swap 3 Planets")

plt.show()
