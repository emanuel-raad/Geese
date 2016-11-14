import cv2
import numpy as np
import Color
from removeColor import removeColor

def nothing(x):
    pass

imgPath = 'aerials/yard4.jpg'

original = cv2.imread(imgPath)
original = cv2.resize(original, (640, 480))
imgColor = removeColor(original, Color.GRASS_LOWER, Color.GRASS_UPPER)

gray = cv2.cvtColor(imgColor, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)

ret, otsu = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Closing and opening before contours to fix up the image
kernel = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(otsu, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

imgContours = closing.copy()
#imgContours = otsu.copy()
imgContours, contours, hierarchy = cv2.findContours(imgContours, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for i in range(0, len(contours)):
    cv2.drawContours(original, contours, i, Color.randomColor(), 2)

# for i in contours:
#     rect = cv2.minAreaRect(i)
#     tl = (int(rect[0][0]), int(rect[0][1]))
#     br = (int(rect[1][0]), int(rect[1][1]))
#     cv2.rectangle(imgColor, tl, br, Color.randomColor(), thickness=1)

#cv2.imshow('window', otsu)
cv2.imshow('closing', closing)
cv2.imshow('original', original)
#cv2.imshow('color', imgColor)

k = cv2.waitKey(0) & 0xFF
if k == ord('q'):
    cv2.destroyAllWindows()
