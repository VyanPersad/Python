import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#Using a grayscale image can be more accurate at times with openCV
#img = cv2.imread("photo.jpg")
img = cv2.imread("news.jpg")

#The lower the scale factor the better but the longer the time needed to process
#minNeighbors will determine the number of neighbors to search around
#The values used are acceptable.
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_img,
                                      scaleFactor=1.05,
                                      minNeighbors=5)

#This loop draws a rectangle around the object identified as a face.
#It take 5 params and cycles through
for x, y, w, h in faces:
    #The first is the imng you are going to load
    #The second is the start pt. of the rectangle and the next is the end pt.
    #The 4th is the color of the line and the last is the line thickness
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

#print(type(faces))
#print(faces)

resized_img = cv2.resize(img, (int(img.shape[1] / 3), int(img.shape[0] / 3)))

cv2.imshow("Face Detector", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()