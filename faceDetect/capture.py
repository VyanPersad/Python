import cv2, time
#The number determines the camera the feed will be from starting from 0...n
#If you have a file simple enter the file directory with file name and ext.
#This allows the program the access the webcam.
vid = cv2.VideoCapture(0)

while True:
    #We will halt ther script for 5 secs to allow for the
    #camera to catch up with the exceution of the script
    check, frame = vid.read()
    #print(check)
    #print(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #time.sleep(5)
    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(1)
    #When you press q the program will quit.
    if key == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()