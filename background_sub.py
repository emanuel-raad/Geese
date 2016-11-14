import cv2

img = cv2.imread('aerials/aerial_1.jpg')

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg = cv2.createBackgroundSubtractorMOG2()

fgmask = fgbg.apply(img)
#fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

cv2.imshow('original', img)
cv2.imshow('win', fgmask)
cv2.waitKey(0)
cv2.destroyAllWindows()

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_video/py_bg_subtraction/py_bg_subtraction.html?highlight=background
# Need to try with video, as the results are better