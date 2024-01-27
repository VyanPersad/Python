import cv2
import numpy as np
import random


#0<--Blk+++White-->255

filename = 'bkl4.png'
img = cv2.imread(filename)

imgW = np.size(img,1)
imgH = np.size(img,0)

#print(imgW)
#print(imgH)

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

#print(grayPixels)
#print(np.argmax(grayPixels))
#print(np.argmin(grayPixels))

minPxVal = np.argmin(grayPixels)
maxPxVal = np.argmax(grayPixels)

#print(pxlArray[minPxVal])
#print(pxlArray[maxPxVal])

RGB_SCALE = 255
CMYK_SCALE = 100

r=pxlArray[minPxVal][0]
g=pxlArray[minPxVal][1]
b=pxlArray[minPxVal][2]

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

def rgbToLab(r, g, b) :
    r = r / 255
    g = g / 255
    b = b / 255

    if r > 0.04045:
        r = (r + 0.055) / 1.055 ** 2.4
    else:
        r = r / 12.92

    if g > 0.04045:
        g = (g + 0.055) / 1.055 ** 2.4
    else:
        g = g / 12.92

    if b > 0.04045:
        b = (b + 0.055) / 1.055 ** 2.4
    else:
        b = b / 12.92

    x = (r * 0.4124 + g * 0.3576 + b * 0.1805) / 0.95047
    y = (r * 0.2126 + g * 0.7152 + b * 0.0722) / 1.00000
    z = (r * 0.0193 + g * 0.1192 + b * 0.9505) / 1.08883

    if x > 0.008856:
        x = x ** (1 / 3)
    else:
        x = (7.787 * x) + 16 / 116
    if y > 0.008856:
        y = y ** (1 / 3)
    else:
        y = (7.787 * y) + 16 / 116
    if z > 0.008856:
        z = z ** (1 / 3)
    else:
        z = (7.787 * z) + 16 / 116

    return f"{(116 * y) - 16:.5f},{500 * (x - y):.5f},{200 * (y - z):.5f}"

def rgbToHsv(r, g, b):
    rabs = r / 255
    gabs = g / 255
    babs = b / 255
    v = max(rabs, gabs, babs)
    diff = v - min(rabs, gabs, babs)
    diffc = lambda c: (v - c) / 6 / diff + 1 / 2
    percentRoundFn = lambda num: round(num * 100) / 100
    if diff == 0:
        h = s = 0
    else:
        s = diff / v
        rr = diffc(rabs)
        gg = diffc(gabs)
        bb = diffc(babs)
        if rabs == v:
            h = bb - gg
        elif gabs == v:
            h = (1 / 3) + rr - bb
        elif babs == v:
            h = (2 / 3) + gg - rr
        if h < 0:
            h += 1
        elif h > 1:
            h -= 1
    return f"{round(h * 360)},{percentRoundFn(s * 100)},{percentRoundFn(v * 100)}"

def rgbToLuminance(r, g, b):
      return (((0.2126*r/255)+(0.7152*g/255)+(0.0722*b/255))*100)

def temperature2rgb(kelvin):
    temperature = kelvin / 100.0
    if temperature < 66.0:
        red = 255
    else:
        red = temperature - 55.0
        red = 351.97690566805693 + 0.114206453784165 * red - 40.25366309332127 * math.log(red)
        if red < 0:
            red = 0
        if red > 255:
            red = 255
    if temperature < 66.0:
        green = temperature - 2
        green = -155.25485562709179 - 0.44596950469579133 * green + 104.49216199393888 * math.log(green)
        if green < 0:
            green = 0
        if green > 255:
            green = 255
    else:
        green = temperature - 50.0
        green = 325.4494125711974 + 0.07943456536662342 * green - 28.0852963507957 * math.log(green)
        if green < 0:
            green = 0
        if green > 255:
            green = 255
    if temperature >= 66.0:
        blue = 255
    else:
        if temperature <= 20.0:
            blue = 0
        else:
            blue = temperature - 10
            blue = -254.76935184120902 + 0.8274096064007395 * blue + 115.67994401066147 * math.log(blue)
            if blue < 0:
                blue = 0
            if blue > 255:
                blue = 255
    return {"red": round(red), "blue": round(blue), "green": round(green)}

def rgbToTemperature(r, g, b):
    epsilon = 0.4
    minTemperature = 1000
    maxTemperature = 40000
    while maxTemperature - minTemperature > epsilon:
        temperature = (maxTemperature + minTemperature) / 2
        testRGB = temperature2rgb(temperature)
        if (testRGB["blue"] / testRGB["red"]) >= (b / r):
            maxTemperature = temperature
        else:
            minTemperature = temperature
    return round(temperature)

def rgbToRyb(r, g, b):
    # Remove the whiteness from the color.
    w = min(r, g, b)
    r -= w
    g -= w
    b -= w

    mg = max(r, g, b)

    # Get the yellow out of the red+green.
    y = min(r, g)
    r -= y
    g -= y

    # If this unfortunate conversion combines blue and green, then cut each in
    # half to preserve the value's maximum range.
    if b and g:
        b /= 2.0
        g /= 2.0

    # Redistribute the remaining green.
    y += g
    b += g

    # Normalize to values.
    my = max(r, y, b)
    if my:
        n = mg / my
        r *= n
        y *= n
        b *= n

    # Add the white back in.
    r += w
    y += w
    b += w

    # And return back the ryb typed accordingly.
    return str(int(r)) + "," + str(int(y)) + "," + str(int(b))

def rgbToXyz(r, g, b):
    r = sRGBtoLinearRGB(r / 255)
    g = sRGBtoLinearRGB(g / 255)
    b = sRGBtoLinearRGB(b / 255)

    X = 0.4124 * r + 0.3576 * g + 0.1805 * b
    Y = 0.2126 * r + 0.7152 * g + 0.0722 * b
    Z = 0.0193 * r + 0.1192 * g + 0.9505 * b

    return str(int(X * 100)) + "," + str(int(Y * 100)) + "," + str(int(Z * 100))


#window_size = 3
#The center value is the centre-point of the selected pixel
#minPxVal is the location of the darkest pixel in the array
#It is the result of the 
#center = (randoW[minPxVal],randoH[minPxVal])
#region = cv2.getRectSubPix(img, (window_size, window_size), center)
#resize = cv2.resize(region,(400,400),interpolation=cv2.INTER_CUBIC)
#cv2.imshow("Darker", resize)

#center2 = (randoW[maxPxVal],randoH[maxPxVal])
#region2 = cv2.getRectSubPix(img, (window_size, window_size), center2)
#resize2 = cv2.resize(region2,(400,400),interpolation=cv2.INTER_CUBIC)
#cv2.imshow("Lighter", resize2)

#cv2.waitKey(0)
#cv2.destroyAllWindows()

