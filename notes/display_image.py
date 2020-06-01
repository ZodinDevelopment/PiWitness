#!/usr/bin/python3


"""
    A simple demonstration of OpenCV functionality, showing the method for
loading and displaying a static image.
"""


import cv2
import sys


# Read the image, passing the image file's path as an argument
image = cv2.imread('lurp2018.jpg')

# Show the image and wait for user input before destroying the window
cv2.imshow('Image', image)
cv2.waitKey(0)
