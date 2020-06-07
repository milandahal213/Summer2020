# Import necessary Python libraries 
# OpenCV library
import cv2
# Library that makes calls to openCV a bit more convinient 
import imutils

# Import library to plot histogram 
import matplotlib.pyplot as plt

#Read image from disk (reads as array)
img=cv2.imread("C:/Users/dipes/OneDrive/Desktop/RPiCamera/me35NotebookText/images/chrisNew.png")
# Resize the image using imutils    
img = imutils.resize(img, width=400, inter=cv2.INTER_LINEAR)

color = ('b','g','r')

for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()

# Split into channels
b,g,r=cv2.split(img)

# Display the image
cv2.imshow("Original", img)

# Display the image
cv2.imshow("Blue channel", b)
# Display the image
cv2.imshow("Green channel", g)
# Display the image
cv2.imshow("Red channel", r)

# Press any key on your keyboard to close the image
cv2.waitKey(0)
cv2.destroyAllWindows()
