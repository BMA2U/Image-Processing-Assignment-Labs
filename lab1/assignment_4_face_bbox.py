import cv2 as cv
import os

image_path = 'image/person1.jpg'
if not os.path.exists(image_path):
    image_path = 'person1.jpg'

image = cv.imread(image_path)

x, y, w, h = 384, 165, 268, 268

cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)

cv.putText(image, "Ahmed", (x + 70, y + h + 35), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)

cv.imwrite('image/person_with_bbox.jpg', image)

try:
    cv.imshow('Face Box', image)
    cv.waitKey(1000)
    cv.destroyAllWindows()
except Exception:
    pass
