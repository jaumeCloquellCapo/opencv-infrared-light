import cv2
import cv2.cv as cv
import sys
import numpy as np
FFMPEG_BIN = "ffmpeg" # on Linux ans Mac OS


video_capture = cv2.VideoCapture(1)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    retval, treshold = cv2.threshold(frame,250,255,cv2.THRESH_BINARY)
    gray = cv2.cvtColor(treshold, cv.CV_BGR2GRAY)

    circles = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT, 1, 20,param1=50,param2=10,minRadius=0,maxRadius=100)
   
    if circles is not None:
	    # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")
        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            print(x)
            print(y)
            print('---')
            #cv2.circle(gray, (x, y), r, (255, 255, 0), 4)
            #cv2.rectangle(gray, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
    
    #print(gray)
    cv2.imshow('pointDetect', gray)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
