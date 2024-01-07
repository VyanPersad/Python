import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('df5.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, threshold = cv2.threshold(gray,80,130, cv2.THRESH_BINARY_INV)

contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
i=0
for contour in contours:
    if i==0:
        i=1
        continue
    appox = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [appox], 0, (255,0,255),5)
#Center of the shapes
    M = cv2.moments(contour)
    if M['m00'] != 0.0:
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])


cv2.imshow('Shapes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
