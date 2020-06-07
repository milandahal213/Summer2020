# Import necessary Python libraries 
# OpenCV library
import cv2
# Library that makes calls to openCV a bit more convinient 
import imutils
# Useful library for array manipulation 
import numpy as np
# Time library for delay 
import time

# Face detector class
class FaceDetector:
    def __init__(self, faceCascadePath):
        # load the face detector
        self.faceCascade = cv2.CascadeClassifier(faceCascadePath)

    def detect(self, image, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30)):
        # detect faces in the image
        rects = self.faceCascade.detectMultiScale(image,
            scaleFactor = scaleFactor, minNeighbors = minNeighbors,
            minSize = minSize, flags = cv2.CASCADE_SCALE_IMAGE)

        # return the rectangles representing boundinb
        # boxes around the faces
        return rects

# construct the face detector
fd = FaceDetector("cascades/haarcascade_frontalface_default.xml")

# Start video capture 
cam = cv2.VideoCapture(0)

# main loop 
while True:
    # Grab the frame 
    ret, frame = cam.read()
    # Display the image
    #cv2.imshow("Original", frame)
    
    # resize the frame and convert it to grayscale
    frame = imutils.resize(frame, width = 200, inter=cv2.INTER_LINEAR)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces in the image and then clone the frame
    # so that we can draw on it
    faceRects = fd.detect(gray, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30))
    frameClone = frame.copy()

    # loop over the face bounding boxes and draw them
    for (fX, fY, fW, fH) in faceRects:
        cv2.rectangle(frameClone, (fX, fY), (fX + fW, fY + fH), (0, 255, 0), 2)
        x=fX+(fX + fW)/2
        y=fY+(fH + fH)/2
        print('({},{})'.format(x, y))
    # show our detected facesq
    # Display the image
    cv2.imshow("Detected", frameClone)
    # if the 'q' key is pressed, stop the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# cleanup the camera and close any open windows
cam.release()
cv2.destroyAllWindows()