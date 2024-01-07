import cv2
import numpy as np

#0<--Blk+++White-->255

filename = 'bkl2.png'
img = cv2.imread(filename)
gryImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
threshold = 125
maxVal = threshold+50
#For threshold the vales above are considered.
#Threshold outputs 2 values the first is the threshold the other is the image.
_, msk = cv2.threshold(gryImg, threshold, maxVal, cv2.THRESH_BINARY_INV)
contours, hierarchy = cv2.findContours(msk, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    # Get the coordinates and dimensions of the bounding rectangle
    x, y, w, h = cv2.boundingRect(c)
    # Draw the rectangle on the original image with a color of your choice and a thickness of 2 pixels
    cv2.rectangle(gryImg, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #cv2.drawContours(gryImg, [c], 0, (255, 0, 255), 2)


#cv2.imshow("Original", img)
# Display the image with the rectangles
cv2.imshow("Region of Interest", gryImg)
cv2.waitKey(0)
cv2.destroyAllWindows()