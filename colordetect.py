import cv2
import numpy as np

def empty():
    pass

cv2.namedWindow('Track Bars')
cv2.resizeWindow('Track Bars', 640, 240)
cv2.createTrackbar('Hue Min', 'Track Bars', 0, 179, empty)
cv2.createTrackbar('Hue Max', 'Track Bars', 19, 179, empty)
cv2.createTrackbar('Sat Min', 'Track Bars', 110, 255, empty)
cv2.createTrackbar('Sat Max', 'Track Bars', 240, 255, empty)
cv2.createTrackbar('Val Min', 'Track Bars', 153, 255, empty)
cv2.createTrackbar('Val Max', 'Track Bars', 255, 255, empty)
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    success, img = cap.read()
    # img = cv2.imread('lambo.png')
    img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos('Hue Min', 'Track Bars')
    h_max = cv2.getTrackbarPos('Hue Max', 'Track Bars')
    s_min = cv2.getTrackbarPos('Sat Min', 'Track Bars')
    s_max = cv2.getTrackbarPos('Sat Max', 'Track Bars')
    v_min = cv2.getTrackbarPos('Val Min', 'Track Bars')
    v_max = cv2.getTrackbarPos('Val Max', 'Track Bars')
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    # Create a mask using track bars with desired color
    mask = cv2.inRange(img_HSV, lower, upper)
    # Add images to create new one
    img_result = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # cv2.imshow('Image',img)
    cv2.imshow('Mask', mask)
    # cv2.imshow('Result', img_result)
    cv2.waitKey(1)