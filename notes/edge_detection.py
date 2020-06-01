#!/usr/bin/python3


"""
    Edge detection uses an algorithm to look for things like change in color,
brightness, etc. to find the edges.
"""


import cv2


# Load the image
image = cv2.imread('lurp2018.jpg')

# convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# blur it
blurred_image = cv2.GaussianBlur(gray_image, (7,7), 0)

cv2.imshow('Original Image', image)
cv2.waitKey(0)

# Canny edge detection takes two arguments for the low and high thresholds
canny = cv2.Canny(blurred_image, 10, 30)
cv2.imshow('Canny with low thresholds', canny)
cv2.waitKey(0)

canny2 = cv2.Canny(blurred_image, 50, 150)
cv2.imshow('Canny with high thresholds', canny2)
cv2.waitKey(0)
