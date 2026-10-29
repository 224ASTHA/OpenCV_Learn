import cv2
# print("Package Imported!")
#
##################### PHOTO CAPTURE ########################
# img = cv2.imread("Resources/lena.jpeg")
#
# cv2.imshow("Output",img)
# cv2.waitKey(0)

##################### VIDEO CAPTURE ########################
# cap = cv2.VideoCapture("Resources/test_video.mp4")
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

##################### LAPTOP CAMERA CAPTURING ########################
cap = cv2.VideoCapture(0)
cap.set(3,640) #width
cap.set(4,480) #height
cap.set(10,100) #brightness (id,amount)

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break