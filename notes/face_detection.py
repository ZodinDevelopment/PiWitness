#!/usr/bin/python3


import sys
import cv2


imagePath = 'lurp2018.jpg'
cascPath = 'haarcascade_frontalface_default.xml'

# create the haar cascade
face_cascade = cv2.CascadeClassifier(cascPath)

# read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# detect faces inthe image
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.2,
    minNeighbors=5,
    minSize=(30,30)
)

print(f'Found {len(faces)} faces')

# draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('Faces found', image)
cv2.waitKey(0)
