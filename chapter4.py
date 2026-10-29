import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
# print(img.shape)
# img[200:300, 100:300] = 255,0,0

############## HAVING LINE ##############
# cv2.line(img,(0,0),(300,300), (0,0,255),3) # (starting point , Ending point , color, thickness)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]), (0,0,255),3)

############## HAVING LINE ##############
cv2.rectangle(img,(100,200),(300,500),(255,0,0),2)
# cv2.rectangle(img,(100,200),(300,500),(255,0,0),cv2.FILLED)

############## HAVING CIRCLE ##############
cv2.circle(img, (400,50), 40, (255,255,0), 4)

############## HAVING TEXT ##############
cv2.putText(img, " ASTHA ", (300,100), cv2.FONT_ITALIC, 0.5, (0,150,0),3) #(position , font style , length, color , font width)

cv2.imshow("Image",img)

cv2.waitKey(0)