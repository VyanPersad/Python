import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('shape_detect.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, threshold = cv2.threshold(gray,127,255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
i=0
for contour in contours:
    if i==0:
        i=1
        continue
    appox = cv2.approxPolyDP(contour, 0.01-cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [contour], 0, (255,0,255),5)
#Center of the shapes
    M = cv2.moments(contour)
    if M['m00'] != 0.0:
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])

    if len(appox) == 3:
        cv2.putText(img, 'Triangle', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,255), 2)

    elif len(appox) == 4:
        cv2.putText(img, 'Quad', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

    elif len(appox) == 5:
        cv2.putText(img, 'Pentagon', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

    else:
        cv2.putText(img, 'Circle', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)


cv2.imshow('Shapes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Color Detection
img = cv2.imread('shape_detect.png')
#HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
l_blue = np.array([0,50,50])
u_blue = np.array([140,255,255])

msk_blue = cv2.inRange(hsv,l_blue,u_blue)
var =  cv2.bitwise_and(img, img, mask = msk_blue)
cv2.imshow('Res', var)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Object Replacemment
img = cv2.imread('shape_detect.png', cv2.IMREAD_COLOR)
img1 = img.copy()
msk = np.zeros((100,300,3))
#print(msk.shape)

pos = (200,200)
var = img1[200:(200+msk.shape[0]), 200:(200+msk.shape[1])] = msk
cv2.imshow('Mask', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()