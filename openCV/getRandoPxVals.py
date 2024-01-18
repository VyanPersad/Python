import cv2
import numpy as np
import random

#0<--Blk+++White-->255

filename = 'bkl4.png'
img = cv2.imread(filename)

imgW = np.size(img,1)
imgH = np.size(img,0)

print(imgW)
print(imgH)

randoW = []
randoH = []
pxlArray = []
grayPixels = []

#Set sample size
n = 5
#Sample pixels
for i in range(0,n):
    randoW.append(random.randint(1,imgW-1))
    randoH.append(random.randint(1,imgH-1))

for i in range(0,n):
    pxlArray.append(img[randoH[i], randoW[i]])
    grayPixels.append(int(sum(pxlArray[i])//3))

print(grayPixels)
print(np.argmax(grayPixels))
print(np.argmin(grayPixels))

minPxVal = np.argmin(grayPixels)
maxPxVal = np.argmax(grayPixels)

print(pxlArray[minPxVal])
print(pxlArray[maxPxVal])

RGB_SCALE = 255
CMYK_SCALE = 100

def rgb_to_cmyk(r, g, b):
    if (r, g, b) == (0, 0, 0):
        # black
        return 0, 0, 0, CMYK_SCALE

    # rgb [0,255] -> cmy [0,1]
    c = 1 - r / RGB_SCALE
    m = 1 - g / RGB_SCALE
    y = 1 - b / RGB_SCALE

    # extract out k [0, 1]
    min_cmy = min(c, m, y)
    c = (c - min_cmy) / (1 - min_cmy)
    m = (m - min_cmy) / (1 - min_cmy)
    y = (y - min_cmy) / (1 - min_cmy)
    k = min_cmy

    # rescale to the range [0,CMYK_SCALE]
    return int(c * CMYK_SCALE), int(m * CMYK_SCALE), int(y * CMYK_SCALE), int(k * CMYK_SCALE)

r=pxlArray[minPxVal][0]
g=pxlArray[minPxVal][1]
b=pxlArray[minPxVal][2]

print(rgb_to_cmyk(r,g,b))

window_size = 3

center = (randoW[minPxVal],randoH[minPxVal])
region = cv2.getRectSubPix(img, (window_size, window_size), center)
resize = cv2.resize(region,(400,400),interpolation=cv2.INTER_CUBIC)
cv2.imshow("Darker", resize)

center2 = (randoW[maxPxVal],randoH[maxPxVal])
region2 = cv2.getRectSubPix(img, (window_size, window_size), center2)
resize2 = cv2.resize(region2,(400,400),interpolation=cv2.INTER_CUBIC)
cv2.imshow("Lighter", resize2)

cv2.waitKey(0)
cv2.destroyAllWindows()

