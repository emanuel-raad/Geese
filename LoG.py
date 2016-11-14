import cv2
import numpy

img = cv2.imread('filtered.jpg', 0)
blur = cv2.GaussianBlur(img, (3, 3), 0)
a = cv2.Laplacian(blur, cv2.CV_64F)

cv2.imwrite('log.jpg', a)

cv2.imshow('img', img)
cv2.imshow('blur', blur)
cv2.imshow('lap', a)
cv2.waitKey(0)
cv2.destroyAllWindows()

