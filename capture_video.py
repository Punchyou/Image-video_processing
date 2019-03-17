# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 18:30:48 2019

@author: Maria
"""

import cv2

first_frame = None

#capture the video
video = cv2.VideoCapture(0)

while True:
    #check if the camera works
    #store the frame values
    check, frame = video.read()
    
    #keep first frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0) #removes noise, improves accuracy
    if first_frame is None:
        first_frame = gray
        continue
    
    #delta frame
    delta_frame = cv2.absdiff(first_frame, gray)
    #white above threshold, black below threshold
    thresh_frame = cv2.threshold(delta_frame, 20, 255, cv2.THRESH_BINARY)[1]
    
    #smooth threshold
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)
    
#    #area of countours as tuple
#    (_, cnts, _) = cv2.findContours(thresh_frame.copy(),
#     cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    
    #show the frame
    cv2.imshow("Gray frame", gray)
    cv2.imshow("Delta frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    
    #exit the preview
    key = cv2.waitKey(40)
    if key == ord('q'):
        break

#release the video
video.release()
#close window
cv2.destroyAllWindows()