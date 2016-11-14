import cv2

def nothing(x):
    pass


cv2.namedWindow('window')
cv2.createTrackbar('one', 'window', 0, 255, nothing)

while True:
    one = cv2.getTrackbarPos('one', 'window')

    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

cv2.destroyAllWindows()
