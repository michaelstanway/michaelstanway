 # -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 18:47:04 2022

@author: micha
"""

#To find the face in an image
'''

import cv2
from random import randrange

#Load some pre-trained data on face frontals from open cv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('OneDrive/haarcascade_frontalface_default.xml')

#Choose an image to detect faces in
img = cv2.imread('OneDrive/RDJ.png')

#Convert to grayscale for simplicity
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
#print(face_coordinates)

#Draw the rectangles around the detected faces
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 2)

#Show the image
cv2.imshow('Clever Programmer Face Detector', img)
cv2.waitKey()


'''

import cv2
from random import randrange

#Load some pre-trained data on face frontals from open cv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('OneDrive/haarcascade_frontalface_default.xml')

#Choose a video to detect faces in, using 0 will go to default webcam
webcam = cv2.VideoCapture(0)


#Iterate forever over frames
while True:
    
    #Read current frame
    successful_frame_read, frame = webcam.read()


    #Convert to grayscale for simplicity
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 2)


    cv2.imshow('Clever Programmer Face Detector', frame)
    #Waits for this number of milliseconds
    key = cv2.waitKey(1)
    
    if key == 81 or key == 113:
        break

webcam.release()

print("End of programme")
