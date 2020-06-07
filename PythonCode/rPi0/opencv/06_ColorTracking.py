# Import necessary Python libraries 
# OpenCV library
import cv2
# Library that makes calls to openCV a bit more convinient 
import imutils
# Useful library for array manipulation 
import numpy as np
# Time library for delay 
import time

from collections import deque

# define the lower and upper boundaries of the "green"
# ball in the HSV color space, then initialize the
# list of tracked points
# Use 06_2findHSVvalue.py to find the HSV values 
# HSV (0-180,0-255,0-255)
greenLower = (35, 91, 0)
greenUpper = (81, 255, 255)
#redLower = (7, 0, 0)
#redUpper = (98, 255, 255)

buffer = 5
pts = deque(maxlen=buffer)

# Start video capture 
cam = cv2.VideoCapture(0)

# keep looping
while True:
    # Grab the frame 
    ret, frame = cam.read()

    # determine which pixels fall within the blue boundaries
    # and then blur the binary image
    green = cv2.inRange(frame, greenLower, greenUpper)
    green = cv2.GaussianBlur(green, (3, 3), 0)

    # find contours in the image
    cnts = cv2.findContours(green.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    # check to see if any contours were found
    if len(cnts) > 0:
        # sort the contours and find the largest one -- we
        # will assume this contour correspondes to the area
        # of my phone
        cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0]

        # compute the (rotated) bounding box around then
        # contour and then draw it      
        rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
        cv2.drawContours(frame, [rect], -1, (0, 255, 0), 2)

    # show the frame and the binary image
    cv2.imshow("Tracking", frame)
    cv2.imshow("Binary", green)

    # if your machine is fast, it may display the frames in
    # what appears to be 'fast forward' since more than 32
    # frames per second are being displayed -- a simple hack
    # is just to sleep for a tiny bit in between frames;
    # however, if your computer is slow, you probably want to
    # comment out this line
    time.sleep(0.025)

    # if the 'q' key is pressed, stop the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# cleanup the camera and close any open windows
cam.release()
cv2.destroyAllWindows()

