# Import necessary packages
import cv2
# Library that makes calls to openCV a bit more convinient 
import imutils

#Read image from disk
image=cv2.imread("C:/Users/dipes/OneDrive/Desktop/RPiCamera/me35NotebookText/images/chrisNew.png")

# Resize the image using imutils    
image = imutils.resize(image, width=400, inter=cv2.INTER_LINEAR)

# Display the image
cv2.imshow("Original", image)

# Press any key on your keyboard to close the image
cv2.waitKey(0)
cv2.destroyAllWindows()