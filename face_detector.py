# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 16:45:53 2019

@author: Maria
"""

import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


#import image
img = cv2.imread("news.jpg")

#use the gray image to pass to the methods
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#return the rectangle of the face
faces = face_cascade.detectMultiScale(gray_img,
                                      scaleFactor=1.5,
                                      minNeighbors=5)
#draw a reactangle around face
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), )

#resize image before showing
resized = cv2.resize(img, (int(img.shape[1]/2),
                     int(img.shape[0]/2)))

#show the image
cv2.imshow("Face", resized)
#press any key to close
cv2.waitKey(0)
cv2.destroyAllWindows()

