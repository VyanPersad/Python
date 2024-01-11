# import the necessary packages
import imutils
import numpy as np
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",
                help="path to the image file",
                default='C:\\Users\\Vyan Persad\\Documents\\Coding\\Python\\SkinTone\\img.jpg')
args = vars(ap.parse_args())

# define the upper and lower boundaries of the HSV pixel
# intensities to be considered 'skin'
lower = np.array([3, 15, 10], dtype="uint8")
upper = np.array([20, 255, 255], dtype="uint8")

#load image
image = cv2.imread(args["image"])

# resize the image to a reasonable width for display (optional)
image = cv2.resize(image, (800, 600))

# convert the image to the HSV color space
converted = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# determine the HSV pixel intensities that fall into
# the specified upper and lower boundaries
skinMask = cv2.inRange(converted, lower, upper)

# apply a series of erosions and dilations to the mask
# using an elliptical kernel
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
skinMask = cv2.erode(skinMask, kernel, iterations=2)
skinMask = cv2.dilate(skinMask, kernel, iterations=2)

# blur the mask to help remove noise
skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)

# apply the mask to the original image
skin = cv2.bitwise_and(image, image, mask=skinMask)

# display the original image and the skin-detected image side by side
#cv2.imshow("Original Image", image)
cv2.imshow("Skin Detection", np.hstack([image, skin]))
cv2.waitKey(0)
cv2.destroyAllWindows()
