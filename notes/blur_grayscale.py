#!/usr/bin/python3


"""
    Two important functions in image processing are blurring and grayscale.
Many image processing operations take place on grayscale images, as they are
simpler to process.

Similarly, blurring is also useful in edge detection.
"""


import cv2


# Load the image
image = cv2.imread('lurp2018.jpg')

# convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


"""
    First, we convert the image to gray. The second argument stands for
'Blue Green Red to Gray'.
"""


# blur it
blurred_image = cv2.GaussianBlur(image, (7,7), 0) # The second arg is the window size. The larger, the more blur

# show all 3 images
cv2.imshow('Original', image)
cv2.imshow('Gray', gray_image)
cv2.imshow('Blurred', blurred_image)

cv2.waitKey(0)
