from HSVTrackbar import HSVTrackbar
from Geese import SnowGoose
from goose import FindWhiteGoose
import cv2

print SnowGoose().upper
s = HSVTrackbar('test2.jpg')
#find = FindWhiteGoose()

print 'main continue'
k = cv2.waitKey(0) & 0xFF
if k == ord('q'):
    s.stop()
    #find.stop()
