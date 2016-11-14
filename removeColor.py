import cv2
import Color

def removeColor(image, colorLow, colorHigh):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, colorLow, colorHigh)
    maskInv = cv2.bitwise_not(mask)

    filtered = cv2.bitwise_and(image, image, mask=maskInv)
    return filtered

'''
imgPath = 'aerials/yard4.jpg'

original = cv2.imread(imgPath)
original = cv2.resize(original, (640, 480))

colorLow = Color.GRASS_LOWER
colorHigh = Color.GRASS_UPPER

newImg = removeColor(original, colorLow, colorHigh)

cv2.imshow('newImg', newImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''