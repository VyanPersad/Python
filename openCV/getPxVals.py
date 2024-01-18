import cv2
import numpy as np

#0<--Blk+++White-->255

filename = 'bkl4.png'
img = cv2.imread(filename)

imgWidth = np.size(img,1)
imgHeight = np.size(img,0)

#imgWidth = gryImng[1]
#imgHeight = gryImng[0]

#If you only use / for division you get a floating point, // gives a rounded down value
mid = imgWidth//2
midLinePixels = []
grayLinePixels = []

for px in range(imgHeight):
    midLinePixel = img[px, mid]
    midLinePixels.append(midLinePixel)

#print(midLinePixels)
for px in range(len(midLinePixels)):
    grayLinePixels.append(int(sum(midLinePixels[px])//3))

print(grayLinePixels)
print(np.argmax(grayLinePixels))
print(np.argmin(grayLinePixels))

minPxVal = np.argmin(grayLinePixels)
maxPxVal = np.argmax(grayLinePixels)

print(midLinePixels[minPxVal])
print(midLinePixels[maxPxVal])

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

#RGB for minPixel
r=midLinePixels[minPxVal][0]
g=midLinePixels[minPxVal][1]
b=midLinePixels[minPxVal][2]
print(rgb_to_cmyk(r,g,b))

#RGB for minPixel
r=midLinePixels[maxPxVal][0]
g=midLinePixels[maxPxVal][1]
b=midLinePixels[maxPxVal][2]
print(rgb_to_cmyk(r,g,b))

window_size = 3
#center is essentially the x y location of the pixel
#In this case the mid is the x as its along the mid-line
#The y is height value of the pixel which corresponds to its position in the array
center = (mid, float(minPxVal))
region = cv2.getRectSubPix(img, (window_size, window_size), center)
resize = cv2.resize(region,(400,400),interpolation=cv2.INTER_CUBIC)
cv2.imshow("Darker", resize)

center2 = (mid, float(maxPxVal))
region2 = cv2.getRectSubPix(img, (window_size, window_size), center2)
resize2 = cv2.resize(region2,(400,400),interpolation=cv2.INTER_CUBIC)
cv2.imshow("Lighter", resize2)

cv2.waitKey(0)
cv2.destroyAllWindows()


