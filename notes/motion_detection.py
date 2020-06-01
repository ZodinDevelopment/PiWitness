#!/usr/bin/python3


import cv2
import sys
import numpy as np


if len(sys.argv) < 2:
    video_capture = cv2.VideoCapture(0)

else:
    video_capture = cv2.VideoCapture(sys.argv[1])

# read two frames, last and current, and convert current to gray
ret, last_frame = video_capture.read()
ret, current_frame = video_capture.read()
gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)

i = 0
while True:
    # we want two frames -  last and current, so we can calc the difference between them
    last_frame = current_frame
    ret, current_frame = video_capture.read()
    gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
    # find the absolute difference between frames
    diff = cv2.absdiff(last_frame, current_frame)

    #i += 1
    #if i % 10 == 0:
    #    i = 0
    #print(np.mean(current_frame))
    #print(np.mean(diff))
    if np.mean(diff) > 10:
        print("Motion detected")

    # display the resulting frame
    cv2.imshow('Video', diff)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
