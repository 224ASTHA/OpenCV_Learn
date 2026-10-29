########### COLOR DETECTION ###########
import cv2
import numpy as np

def empty(a):
    pass

path = 'Resources/orange.jpg'
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min", "TrackBars", 0 , 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179 , 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 0 , 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255 , 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 0 , 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255 , 255, empty)

while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Min", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("Original", img)
    cv2.imshow("New", imgHSV)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", imgResult)
    cv2.waitKey(1)




# We need to define some color value some ranges in which we want our color to be

# We will define the hue , the saturation , the value limits
# within the limits if the color range fall we will grab that

# We will define track bars which will help us to play around the values in real time
# so that we can find the optimum minimum and maximum value of our color

############### EXPLANATION ################

# 1. Defining the Color Ranges (HSV vs. RGB)
#
# While we usually think of colors in RGB (Red, Green, Blue), OpenCV color detection almost always uses the HSV (Hue, Saturation, Value) color space.
# • Hue (\(H\)): Represents the actual color type (e.g., Red, Green, Blue). In OpenCV, this ranges from 0 to 179.
# • Saturation (\(S\)): Represents the vibrancy or purity of the color (from faded/grayish to fully intense). In OpenCV, this ranges from 0 to 255.
# • Value (\(V\)): Represents the brightness of the color (from dark/black to completely bright). In OpenCV, this ranges from 0 to 255.
# By defining a Minimum HSV limit and a Maximum HSV limit, you create a "color box." Any pixel in your image that falls inside this box is kept, and everything else is discarded.
#
# 2. "Within the limits... we will grab that" (Thresholding)
#
# In OpenCV, "grabbing" the color within your defined limits is done using the cv2.inRange() function.
# This function acts as a filter. It checks every single pixel in your image:
# • If a pixel's HSV values are between your Min and Max limits, OpenCV turns that pixel White (255).
# • If a pixel falls outside the limits, OpenCV turns it Black (0).
# The result is a binary image called a Mask. The white parts of the mask represent the exact objects or colors you wanted to "grab."
#
# 3. Dynamic Calibration Using Trackbars
#
# Lighting conditions completely change how a color looks to a camera. A green ball under a bright light has a different HSV value than the same green ball in a shadow. Because of this, hardcoding fixed Min/Max numbers rarely works.
# OpenCV provides Trackbars (cv2.createTrackbar()), which are visual sliders you can append to a window. By creating 6 sliders (Min H, Min S, Min V, Max H, Max S, Max V), you can tweak the color limits in real time while watching your live camera feed.
# You simply slide the trackbars until the object you want to detect turns completely white on your mask screen, and the background turns completely black. This is how you find the optimum minimum and maximum values for your specific environment.