#!/usr/bin/python3


import cv2


# Read the image
image = cv2.imread('lurp2018.jpg')

# convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# blur it
blurred_image = cv2.GaussianBlur(gray_image, (7,7), 0)

# show both our images
cv2.imshow('Original', image)
cv2.imshow('Blurred', blurred_image)
cv2.waitKey(0)

# Run the canny edge detector
canny = cv2.Canny(blurred_image, 30, 100)
cv2.imshow('Canny', canny)
cv2.waitKey(0)

# find the contours
contours, hierarchy= cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print(f'Number of objects found: {len(contours)}')

cv2.drawContours(image, contours, -1, (0,255,0), 2)
cv2.imshow('objects Found', image)
cv2.waitKey(0)
