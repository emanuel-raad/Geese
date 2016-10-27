import cv2
import numpy as np
import Color
from Geese import SnowGoose
import threading
import time

def filterAreaLow(contours, thresLow):
    filteredAreas = []
    for i in contours:
        if cv2.contourArea(i) >= thresLow:
            filteredAreas.append(i)
    return filteredAreas

class FindWhiteGoose:

    def __init__(self):
        thread = threading.Thread(target=self.run)
        thread.daemon = True
        self.isRunning = True
        thread.start()

    def stop(self):
        self.isRunning = False

    def run(self):
        #Filters a contour array by low bound

        frame = cv2.imread('test.jpg', 1)

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv, SnowGoose().lower, SnowGoose().upper)
        res = cv2.bitwise_and(frame, frame, mask=mask)
        res = cv2.GaussianBlur(res, (5, 5), 0)

        kernel = np.ones((7, 7), np.uint8)
        erosion = cv2.erode(res, kernel, iterations=2)
        im = cv2.cvtColor(erosion, cv2.COLOR_BGR2GRAY)

        # Use canny edge to find outline after erosion
        edges = cv2.Canny(im, 206, 438)

        # Dilate the lines to join them and form one contour
        kernelDilate = np.ones((5, 5), np.uint8)
        edges = cv2.dilate(edges, kernel, iterations=1)

        cv2.imshow('edges', edges)

        # Finds the contours. Use cv2.RETR_EXTERNAL to only get the outer contour for the thick edge
        imgContours, contours, h = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Only keep areas above 10,000
        MIN_AREA = 10000
        filteredContours = filterAreaLow(contours, MIN_AREA)

        # Draws each contour
        for i in filteredContours:
            cv2.drawContours(frame, [i], 0, Color.randomColor(), 3)

        print "Number of geese: {}".format(len(filteredContours))
        cv2.imshow('frame', frame)
        cv2.imwrite("contour.jpg", frame)