import cv2
import numpy as np

def distance(x1, x2, y1, y2):
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

image = cv2.imread('shoe.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edge = cv2.Canny(gray, 50, 100)

cv2.imshow('Original Image', image)
cv2.imshow('Edge Image', edge)

contours, _ = cv2.findContours(edge.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Corrected line
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:2]

ref_width = 9.5

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)  # Corrected line
    pixels_per_metric = w / ref_width
    object_size = distance(x, x + w, y, y + h) / pixels_per_metric  # Corrected line
    print(f'The size of the shoe is approximately {object_size} inches.')
    uk = (3*object_size) - 23
    print("size of the shoe in uk =",int(uk))

cv2.waitKey(0)
cv2.destroyAllWindows()
