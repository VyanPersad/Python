import numpy as np
import cv2

imgFile = 'bcc1.png'
img = cv2.imread(imgFile)
#This is the location of the particular pixel
px = img[100,100]
#These are the details
print(px)

blue = img[100,100,0]
print(blue)

imgS = cv2.imread(imgFile, cv2.IMREAD_COLOR)
alphaImg = cv2.imread(imgFile, cv2.IMREAD_UNCHANGED)
grayImg = cv2.imread(imgFile, cv2.IMREAD_GRAYSCALE)

print('RGB shape: ', imgS.shape)
print('ARGB shape: ', alphaImg.shape)
print('GSCALE shape: ', grayImg.shape)

#Select a region of an Img
winName = ''
#imgRegion = cv2.selectROI(winName, img, showCrosshair= , fromCenter= )
#print(imgRegion)
#OR
#This would allow you to draw the rectangle on the img
#It will then produced a cropped second image
imgRaw = cv2.imread(imgFile)
roi = cv2.selectROI(imgRaw)
print(roi)

roiCrop = imgRaw[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]
cv2.imshow("ROI_Image", roiCrop)
cv2.imwrite("Cropped.jpg",roiCrop)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Splitting & Merging
imgSplit = cv2.split(imgRaw)
#imgMerg = cv2.merge(imgRaw)
#OR
#This will split the image according to its constituent colors
#It will then show the particular part of the image
r,g,b=cv2.split(imgRaw)
cv2.imshow("The Green part", g)

#This should recombine and re-create the original image
imgMerg = cv2.merge((g,b,r))
cv2.imshow("Re-Combined Img", imgMerg)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Changing the colou
changCol =  cv2.cvtColor(imgRaw, cv2.COLOR_RGB2Lab)
cv2.imshow("Changed Color", changCol)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Blend two imgs
img1 = cv2.imread("filepath1",cv2.IMREAD_COLOR)
img1a = cv2.resize(img1, (800,600))
img2 = cv2.imread("filepath2",cv2.IMREAD_COLOR)
img2a = cv2.resize(img2, (800,600))
alpha = 1
beta = 0.5
gamma = 0.0
blendedImg = cv2.addWeighted(img1, alpha, img2, beta, gamma)
cv2.imshow("Blended Img", blendedImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Filters
img1 = cv2.imread("filepath1",cv2.IMREAD_COLOR)
#A sharpening mask
k_sharp = np.array([[1,1,1],
                    [1,9,1],
                    [1,1,1]
                    ])
sharpened = cv2.filter2D(img1, -1, k_sharp)
cv2.imshow("Original Img", img1)
cv2.imshow("Sharper Img", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()

img1 = cv2.imread("filepath1",cv2.IMREAD_GRAYSCALE)
#A threshold mask
ret , threshold = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)
cannyImg = cv2.Canny(img1,50,100)
cv2.imshow("Original Img", img1)
cv2.imshow("Threshold Img", threshold)
cv2.imshow("Canny Img", cannyImg)
cv2.waitKey(0)
cv2.destroyAllWindows()