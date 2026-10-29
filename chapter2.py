import cv2
import numpy as np
img = cv2.imread("Resources/lena.jpeg")
######### Convert to Grayscale #############
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image",imgGray)

######### Convert to Blur #############
imgBlur = cv2.GaussianBlur(img,(7,7),0) #have to be odd number
cv2.imshow("Blur Image",imgBlur)

######### Convert to Canny #############
imgCanny = cv2.Canny(img,100,100) # kitna line aayega (Threshold)
cv2.imshow("Canny Image", imgCanny)

kernel = np.ones((5,5),np.uint8)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
cv2.imshow("Dialation Image", imgDialation)

imgEroded = cv2.erode(imgDialation,kernel,iterations=1)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)
