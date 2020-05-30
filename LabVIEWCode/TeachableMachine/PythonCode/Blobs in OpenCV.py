import cv2, imutils
import numpy as np

def showimage():
    global frame
    cap = cv2.VideoCapture(0)

    params = cv2.SimpleBlobDetector_Params()   # Setup SimpleBlobDetector parameters.
     
    # Change thresholds
    params.minThreshold = 50;
    params.maxThreshold = 255;
     
    # Filter by Area.
    params.filterByArea = True
    params.minArea = 1500
     
    # Filter by Circularity
    params.filterByCircularity = False
    params.minCircularity = 0.1
     
    # Filter by Convexity
    params.filterByConvexity = False
    params.minConvexity = 0.87
     
    # Filter by Inertia
    params.filterByInertia = False
    params.minInertiaRatio = 0.01

    # Create a detector with the parameters

    ver = (cv2.__version__).split('.')
    if int(ver[0]) < 3 :
        detector = cv2.SimpleBlobDetector(params)
    else : 
        detector = cv2.SimpleBlobDetector_create(params)
    
    while True:
        ret, frame = cap.read()
        frame = imutils.resize(frame, width=400)
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        keypoints = detector.detect(frame)
        try:
            print(keypoints.pt[0],keypoints.pt[1],keypoints.size)
        except:
            pass
        im_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        # Show keypoints
        cv2.imshow("Keypoints", im_with_keypoints)
        #cv2.waitKey(0)

        if cv2.waitKey(1) & 0xFF == ord('c'):
            break
    cap.release()
    cv2.destroyAllWindows()

showimage()

'''
        #frame = cv2.imread("/Applications/National Instruments/LabVIEW 2019 64-bit/resource/dialog/GSW/Course/_Subs/TeachableMachine/Ziyi.jpg", cv2.IMREAD_GRAYSCALE)

        # Detect blobs.
        #ret,thresh1 = cv2.threshold(frame,150,255,cv2.THRESH_BINARY)
        #cv2.imshow("Thresh",thresh1)
        # Draw detected blobs as red circles.
        # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
        #im_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        # convert the image to grayscale
        #gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
         
        # convert the grayscale image to binary image
        #ret,thresh = cv2.threshold(gray_image,127,255,0)
         
        # find contours in the binary image

        contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        for c in contours:
           # calculate moments for each contour
           M = cv2.moments(c)

           # calculate x,y coordinate of center
           try:
               cX = int(M["m10"] / M["m00"])
               cY = int(M["m01"] / M["m00"])
           except:
               cX = 0
               cY = 0
           img = frame

           cv2.circle(thresh1, (cX, cY), 5, (255, 0, 0), 5)
           cv2.putText(thresh1, "centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
         
           # display the image
           cv2.imshow("Image", thresh1)
'''
           

 
