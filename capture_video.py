# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 18:30:48 2019

@author: Maria
"""

import cv2

#capture the video
video = cv2.VideoCapture(0)

while True:
    #check if the camera works
    #store the frame values
    check, frame = video.read()
    print(frame)
    
    #store the first frame, gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #show the frame
    cv2.imshow("Capturing", gray)
    
    #exit the preview
    key = cv2.waitKey(40)
    if key == ord('q'):
        break

#release the video
video.release()
#close window
cv2.destroyAllWindows()



