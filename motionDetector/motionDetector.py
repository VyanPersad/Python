import cv2, time
import pandas as pd
from datetime import datetime

#We get the value of the first frame of the footage.
first_frame = None
status_list = [None, None]
times = []
data_fr = pd.DataFrame(columns=["Start", "End"])

vid = cv2.VideoCapture(0)

while True:
    check, frame = vid.read()
    #Used to indicate no motion in 1st frame
    stat = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #Use this to blur the img to remove noise and
    #reduces inaccuracies in the difference calc.
    #The values used are standard values for the function
    #The docs have the explanation and other details.
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    #We will compare everyother frame to this original frame to
    #determine the difference, the degree of the difference
    #will determine the magnitude of the motion.
    if first_frame is None:
        first_frame = gray
        #This facititates the continuation of the loop
        #and not breaking out at this point
        continue
        #This line would also not be executed
        #on the second iteration of the loop.

    delta_fr = cv2.absdiff(first_frame, gray)
    #This produces another img.
    threshold_delta = cv2.threshold(delta_fr, 35, 255, cv2.THRESH_BINARY)[1]
    #This specifices the threshold for the img, and sets the pixel
    #values above a certain number to another number and hence colour.
    threshold_delta = cv2.dilate(threshold_delta, None, iterations=2)
    #This helps to smoothen out the images and the wihite areas.
    #The higher the iterations number the smoother the image.

    #for opencv2 and python 2
    #(cnts,_)
    #for opencv2 and python 3
    #(_, cnts, _)
    (cnts, _) = cv2.findContours(threshold_delta.copy(), cv2.RETR_EXTERNAL,
                                 cv2.CHAIN_APPROX_SIMPLE)
    for contours in cnts:
        if cv2.contourArea(contours) < 10000:
            continue
        stat = 1

        (x, y, w, h) = cv2.boundingRect(contours)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    status_list.append(stat)

    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())
    #cv2.imshow("Delta Frame", delta_fr)
    cv2.imshow("Threshold Frame", threshold_delta)
    cv2.imshow("Colour Frame", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

#print(status_list)
#print(times)

#This loop gets the start nad end times listed in the times[]
for i in range(0, len(times) - 1, 2):
    #data_fr = data_fr.append({"Start :": times[i],"End :": times[i + 1]},ignore_index=True)
    data_fr = pd.concat([
        data_fr,
        pd.DataFrame.from_dict({
            "Start :": [times[i]],
            "End :": [times[i + 1]]
        })
    ],
                        ignore_index=True)
#Exports times[] data to a .csv file
data_fr.to_csv("Times.csv")
vid.release()
cv2.destroyAllWindows()