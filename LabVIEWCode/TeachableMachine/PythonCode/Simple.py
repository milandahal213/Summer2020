import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

import time
    
def mainthread():
    model = tensorflow.keras.models.load_model('converted_keras/keras_model.h5')
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    paths = ['micro.jpg','EV3.jpg','key.jpg']

    for path in paths:
        # Replace this with the path to your image
        image = Image.open(path)

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


mainthread()

'''
t1 = threading.Thread(target = showimage)
t1.start()
t2 = threading.Thread(target = mainthread)
t2.start()
'''
