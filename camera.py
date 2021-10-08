"""
Bounding box
References: 
	https://docs.opencv.org/master/df/d9d/tutorial_py_colorspaces.html

"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

#object tracking
while(1):
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	#thresholding?
	lower_blue = np.array([100,0,0])
	upper_blue = np.array([150,255,255])
	mask = cv2.inRange(hsv, lower_blue, upper_blue)

	#mask color with video frame
	res = cv2.bitwise_and(frame, frame, mask= mask)

	#bounding box
	contours = cv2.findContours(mask.copy(), 1, 2)[-2]
	if len(contours) > 0:
		area = max(contours, key=cv2.contourArea)
		x,y,w,h = cv2.boundingRect(area)
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

	cv2.imshow('frame', frame)

	k = cv2.waitKey(5) & 0xFF

	if k == 27:
		break

cv2.destroyAllWindows()
