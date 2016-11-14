import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('frame')

img = cv2.imread('aerials/aerial_1.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

g1 = np.array([0, 0, 0])
g2 = np.array([200, 255, 255])

mask = cv2.inRange(hsv, g1, g2)

no_green = cv2.bitwise_and(hsv, hsv, mask=mask)

cv2.imshow('g', no_green)

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(grey, (5, 5), 0)

cv2.createTrackbar('l_h', 'frame', 3, 255, nothing)
cv2.createTrackbar('l_s', 'frame', 0, 255, nothing)
while True:
    l = cv2.getTrackbarPos('l_h', 'frame')
    if l%2==0:
        l = 3
    h = cv2.getTrackbarPos('l_s', 'frame')

    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, l, h)
    res = cv2.bitwise_and(img, img, mask=thresh)
    cv2.imshow('frame', res)
    k = cv2.waitKey(5) & 0xFF
    if k == ord('q'):
        break

cv2.imwrite('adapGauss.jpg', res)
cv2.destroyAllWindows()