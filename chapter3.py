import cv2

img = cv2.imread("Resources/lambo.jpg")
print(img.shape)

############## RESIZE IMAGE ##############
imgResize = cv2.resize(img,(300,400)) # (width, height)

cv2.imshow("Image",img)
cv2.imshow("Resized Image", imgResize)

imgCropped = img[0:200, 200:500] #(height , width)
cv2.imshow("Cropped Image", imgCropped)
cv2.waitKey(0)