# Import necessary packages
import cv2
# Library that makes calls to openCV a bit more convinient 
import imutils

# Start video capture 
cam = cv2.VideoCapture(0)

# Grab the frame 
ret, frame = cam.read()

# Resize the image to 400px
frame = imutils.resize(frame, width=400, inter=cv2.INTER_LINEAR)

# Release the camera resource
cam.release()

# Display the frame
cv2.imshow("Original", frame)

# Save the file on disk
cv2.imwrite("green.png",frame)

# Press any key on your keyboard to close the image
cv2.waitKey(0)
cv2.destroyAllWindows()



