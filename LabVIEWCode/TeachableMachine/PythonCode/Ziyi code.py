import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import threading
import time

global frame

def showimage():
    global frame
    cap = cv2.VideoCapture(0)
    while (1):
        ret, frame = cap.read()
        cv2.imshow("capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('c'):
            break
    cap.release()
    cv2.destroyAllWindows()
    
def mainthread():
    global frame
    model = tensorflow.keras.models.load_model('/Users/crogers/Desktop/TeachableMachine/converted_keras/keras_model.h5')
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    while True:
        cv2.imwrite("/Users/crogers/Desktop/TeachableMachine/Ziyi.jpg", frame)
        # Replace this with the path to your image
        image = Image.open('/Users/crogers/Desktop/TeachableMachine/Ziyi.jpg')

        # resize the image to a 224x224 with the same strategy as in TM2:
        # resizing the image to be at least 224x224 and then cropping from the center
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)

        # turn the image into a numpy array
        image_array = np.asarray(image)

        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

        # Load the image into the array
        data[0] = normalized_image_array

        # run the inference
        prediction = model.predict(data)
        result = prediction.tolist()
        print(result)
        time.sleep(0.5)

t1 = threading.Thread(target = showimage)
t1.start()
time.sleep(10)
t2 = threading.Thread(target = mainthread)
t2.start()
