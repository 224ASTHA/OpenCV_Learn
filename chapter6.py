############### JOINING IMAGES ###############
import cv2
import numpy as np

img = cv2.imread('Resources/lena.jpeg')
imgCar = cv2.imread('Resources/lambo.jpg')

imgHor = np.hstack((img,img))
imgVor = np.vstack((imgCar,imgCar))

cv2.imshow("Horizontal", imgHor)
cv2.imshow("Vertical", imgVor)

cv2.waitKey(0)

############ ISSUES ############
# We cannot resize the images
# If the images do not have the same numbers of channels then it will not work
# Example - if one is gray and other is coloured then this stacking will not work there
