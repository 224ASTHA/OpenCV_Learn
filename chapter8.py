########### CONTOURS/SHAPE DETECTION ###########
## Detect each shape, classify it, and count the total
import cv2
import numpy as np


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])

    # Use the first image's size for all images
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]

    for x in range(rows):
        for y in range(cols):
            img = imgArray[x][y]
            img = cv2.resize(img, (width, height))

            # Convert grayscale to BGR so everything can be stacked
            if len(img.shape) == 2:
                img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

            img = cv2.resize(img, (0, 0), fx=scale, fy=scale)
            imgArray[x][y] = img

    hor = [np.hstack(row) for row in imgArray]
    return np.vstack(hor)


# def getContours(imgCanny, imgContour):
#     contours, _ = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#     count = 0
#
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         if area > 500:  # ignore tiny noise; tune this for your image
#             count += 1
#             cv2.drawContours(imgContour, [cnt], -1, (255, 0, 0), 3)
#
#             peri = cv2.arcLength(cnt, True)
#             approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
#             corners = len(approx)
#             x, y, w, h = cv2.boundingRect(approx)
#
#             if corners == 3:
#                 shape = "Triangle"
#             elif corners == 4:
#                 aspectRatio = w / float(h)
#                 shape = "Square" if 0.95 < aspectRatio < 1.05 else "Rectangle"
#             elif corners > 4:
#                 shape = "Circle"
#             else:
#                 shape = "Unknown"
#
#             cv2.putText(imgContour, shape, (x + w // 2 - 40, y + h // 2),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
#
#     return count

def getContours(img, imgContour):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print("Area:", area)
        if area > 300:
            #cv2.drawContours(imgContour, [cnt], -1, (255, 0, 0), 3)

            peri = cv2.arcLength(cnt, True)  # perimeter of the closed contour
            print("Perimeter:", peri)

            approx = cv2.approxPolyDP(cnt, 0.04 * peri, True)  # simplified polygon
            print("Corners:", len(approx))
            objCor = len(approx)
            # Bounding Box
            x, y, w, h = cv2.boundingRect(approx)

            cv2.rectangle(imgContour, (x,y), (x+w, y+h), (0,255,0), 2)

            # Categorising
            if objCor == 3:
                shape = "Triangle"
            elif objCor == 4:
                aspectRatio = w / float(h)
                shape = "Square" if 0.95 < aspectRatio < 1.05 else "Rectangle"
            elif objCor > 4:
                shape = "Circle"
            else:
                shape = "Unknown"

            cv2.putText(imgContour,shape,(x+(w//2)-30, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.6,(0,0,0), 1)

path = 'Resources/shapes.png'
img = cv2.imread(path)
if img is None:
    raise FileNotFoundError(f"Could not read {path}")

imgContour = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50) # find the number of edges
getContours(imgCanny, imgContour)
# shapeCount = getContours(imgCanny, imgContour)
# print("Number of shapes:", shapeCount)
#
imgBlank = np.zeros_like(imgCanny)
imgStack = stackImages(0.8, [[img, imgGray, imgBlur],
                             [imgCanny, imgContour, imgBlank]])

cv2.imshow("Stack", imgStack)
cv2.waitKey(0)
#cv2.destroyAllWindows()