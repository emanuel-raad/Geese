from HSVTrackbar import HSVTrackbar
from Geese import SnowGoose
import cv2
import numpy as np
import Queue

HSV_WINDOW = 'hsv'
HSV2_WINDOW = 'hsv2'
cv2.namedWindow(HSV_WINDOW)
cv2.namedWindow(HSV2_WINDOW)

print SnowGoose().upper
queue = Queue.Queue(maxsize=5)

imgPath = 'aerials/yard4.jpg'
original = cv2.imread(imgPath)
original = cv2.resize(original, (640, 480))

s = HSVTrackbar(queue, HSV_WINDOW, original)

print 'main continue'

while True:
    img = queue.get()
    cv2.imshow(HSV_WINDOW, img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        s.stop()
        kernel = np.ones((3, 3), np.uint8)
        i = cv2.erode(img, kernel, iterations=1)

        blur = cv2.GaussianBlur(i, (3, 3), 0)
        #cv2.imwrite('filtered.jpg', blur)
        break

cv2.destroyAllWindows()