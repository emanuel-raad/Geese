import cv2
import numpy as np
import threading
import time

class HSVTrackbar:

    def __init__(self, image):
        self.imageName = image
        self.image = cv2.imread(image, 1)
        self.hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        self.interval = 5.0/1000.0

        cv2.namedWindow('hsv')
        cv2.createTrackbar('l_h', 'hsv', 0, 255, self.nothing)
        cv2.createTrackbar('l_s', 'hsv', 0, 255, self.nothing)
        cv2.createTrackbar('l_v', 'hsv', 0, 255, self.nothing)

        cv2.createTrackbar('h_h', 'hsv', 0, 255, self.nothing)
        cv2.createTrackbar('h_s', 'hsv', 0, 255, self.nothing)
        cv2.createTrackbar('h_v', 'hsv', 0, 255, self.nothing)

        thread = threading.Thread(target=self.run)
        #thread.daemon = True
        self.isRunning = True
        thread.start()

    def nothing(self, x):
        pass

    def stop(self):
        print 'stopping HSVTrackbar'
        self.isRunning = False

    def run(self):
        while self.isRunning:
            l_h = cv2.getTrackbarPos('l_h', 'hsv')
            l_s = cv2.getTrackbarPos('l_s', 'hsv')
            l_v = cv2.getTrackbarPos('l_v', 'hsv')

            h_h = cv2.getTrackbarPos('h_h', 'hsv')
            h_s = cv2.getTrackbarPos('h_s', 'hsv')
            h_v = cv2.getTrackbarPos('h_v', 'hsv')

            low = np.array([l_h, l_s, l_v])
            high = np.array([h_h, h_s, h_v])

            mask = cv2.inRange(self.hsv, low, high)
            res = cv2.bitwise_and(self.image, self.image, mask=mask)
            cv2.imshow('hsv', res)
            time.sleep(self.interval)