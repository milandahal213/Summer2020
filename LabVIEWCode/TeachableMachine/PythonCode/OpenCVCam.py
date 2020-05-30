import cv2
import numpy as np
import time

global video

class ChrisCam(object):
    def __init__(self,camera = 'c:/fred.avi'):
        self.cap = cv2.VideoCapture(camera)
        self.image_type = 0
        
    def size(self,width = 320, height = 240):
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
        return self.cap.isOpened()

    def snap(self,show=True, fx=0.1, fy=0.1):
        ret,frame = self.cap.read()
        if ret:
            frame = cv2.resize(frame, None, fx=fx, fy=fy)
        if show:
            cv2.imshow('image',frame)
        return ret, frame

    def rotate(self, img, rotation):
        rows,cols,depth = img.shape
        rotationMatrix = cv2.getRotationMatrix2D((cols/2,rows/2),rotation,1)
        frame = cv2.warpAffine(img,rotationMatrix,(cols,rows))
        return frame

    def toLV(self,frame,plane = 'RGB'):      # takes around 30 ms per call
        array = frame.ravel()
        mask = np.array([])
        if not plane == 'Gray':
            image_depth = 24
            colors = np.array([])
            fixedFrame = np.empty((array.size,),dtype = array.dtype)
            if 'R' in plane:
                fixedFrame[0::3] = array[2::3]   # go from BGR ro RGB
            if 'G' in plane:
                fixedFrame[1::3] = array[1::3]
            if 'B' in plane:
                fixedFrame[2::3] = array[0::3]
        else:
            fixedFrame = np.empty((int(array.size/3),),dtype = array.dtype)
            fixedFrame[0::1] = array[0::3]# int((int(array[0::3]) + int(array[1::3]) +  int(array[2::3]) ) / 3)
            image_depth = 8
            colors = np.array([ (i | i<<8 | i<<16) for i in range(256)])  # define color map
        self.rectangle = (0,0,frame.shape[1],frame.shape[0])  # this is the LabVIEW rectangle format
        reply =  (self.image_type, image_depth,fixedFrame.tolist(),mask.tolist(),colors.tolist(),self.rectangle)
        return reply

    def toCV(self,LVimage):      # takes around 30 ms per call
        rows,cols = LVimage[5][3],LVimage[5][2]
        array = np.asarray(LVimage[2],dtype='uint8')
        fixedFrame = np.empty((array.size,),dtype = array.dtype)
        fixedFrame[0::3] = array[2::3]   # go from RGB to BGR
        fixedFrame[1::3] = array[1::3]
        fixedFrame[2::3] = array[0::3]
        img = fixedFrame.reshape(rows,cols,3)
        return img

    def close(self):
        self.cap.release()
        cv2.destroyAllWindows()
        return True

def initCam(camera = 'c:/fred.avi',width = 640, height = 480):
    global video
    video = ChrisCam(camera)
    return video.size(width,height)

def snap(show=True, rotation = 90, plane = 'RGB',fx=0.1, fy=0.1):
    ret, frame = video.snap(show,fx,fy)
    if not ret:
        return 
    if not rotation == 0:
        frame = video.rotate(frame,rotation)
    return video.toLV(frame,plane)

def closeCam():
    return video.close()

