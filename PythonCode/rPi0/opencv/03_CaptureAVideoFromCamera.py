# Import necessary Python libraries 
# OpenCV library
import cv2

# Initialize the video stream
cam = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
# codec XVID, output format *.avi, fps = 20, 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

# main loop
for i in range(100):
    ret, frame = cam.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

# Release everything when the job is finished
cam.release()
out.release() 