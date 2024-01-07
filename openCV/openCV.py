import cv2

#read an img
path = r'image path here'
img=cv2.imread(path)
#Displays as grayscale
img=cv2.imread(path , 0)
#Displays as colour
img=cv2.imread(path , -1)
#Displays a Grayscale as a color image
img=cv2.imread(path , 1)

window_title='Your Title here'
cv2.imshow(window_title, img)

filename = "Name of file to save"
save_dir=r''
cv2.imwrite(filename,img)
cv2.imwrite(save_dir,img)

#Prints image details
#Point to note in image processing with greyscale 0 is black and 255 is white.
#Image resolution
print(img.shape)
#RGB -> Gray
gryImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Gray -> RGB
colImg = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

#Will show the converted image
cv2.imshow('Img Name', gryImg)
#Resize - will resize to an image 800pxx800px
resize = cv2.resize(img, (800,800))
cv2.imshow('Resized Img Name', resize)

#To place text onto the image
coordinates = (100,100)
text = cv2.putText(img, "Your text Here", coordinates, cv2.FONT_HERSHEY_DUPLEX,4,(255,0,0),2)

#Drawing shapes
cv2.line(img, (500,400), (900,500),(0,0,512),5)
cv2.circle(img, (630,200),80,(0,0,255),5)
cv2.rectangle(img, (1000,50),(200,600),(0,0,255),5)
cv2.ellipse(img, (250,250), (100,100), 0, 0, 180, 256, -1)

#These 2 allow for an input to close the windows.
cv2.waitKey(0)
cv2.destroyAllWindows()

#Webcam This will get a video stream from a webcam adn display it in a window
webObj = cv2.VideoCapture(0)

while(True):
    ret , frame = webObj.read()
    cv2.imshow('frame', frame)
    #If you press the q button you will end the stream
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        webObj.release()
cv2.destroyAllWindows()

if(webObj.isOpened() == False):
    print("Camera can't be opened")

frame_width = imt(webObj.get(3))
frame_height = imt(webObj.get(4))
#This sets the video output with the codec o be used as well as the video size and fps
videoCodec = cv2.VideoWriter_fourcc(*'XVID')
videoOutput = cv2.VideoWriter('Captured_Video.mp4', videoCodec, 30, (frame_width, frame_height))

while (True):
    ret , frame = webObj.read()

    if ret == True:
        videoOutput.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
            break
webObj.release()
videoOutput.release()
cv2.destroyAllWindows()

#Capture video from file
#Make sure to include the file format
capture = cv2.VideoCapture('file_name.mp4')

while(True):
    ret , frame = capture.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()