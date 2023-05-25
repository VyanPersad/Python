import cv2
import glob
#The second parameter varies the image in accordance with the cv2 library
img = cv2.imread("horimiya_43_2.jpg", 0)

#Prints the numpy array that makes up the image
#print(img)
#print(img.shape)
#print(img.ndim)

resize_img = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))

#This shows the image and waits for 2 secs and closes it.
cv2.imshow("horimiya_43_2.1", resize_img)
#The number in brackets is the time in milliseconds.
cv2.waitKey(0)
cv2.imwrite("horimiya_43_2.1.jpeg", resize_img)
cv2.destroyAllWindows()

#The code below will get a list of images
#from a file path and then resize all of them
#it will apppend the resize to thefile name so you know
imgs = glob.glob("*.jpg")

for imag in imgs:
    img = cv2.imread(imag, 0)
    res = cv2.resize(img, (100, 100))
    cv2.imshow("Hey", res)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized" + imag, res)
