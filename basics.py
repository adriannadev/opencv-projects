import cv2
import numpy as np

# Open an image
img = cv2.imread('lena.png')
# Define kernel for dilation and erosion
kernel = np.ones((5,5), np.uint8)
# Convert to B&W
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur
img_blur = cv2.GaussianBlur(img_gray, (7,7), 0)
# Canny edge detector (threshold values)
img_canny = cv2.Canny(img, 150, 200)
# Thicker lines
img_dilated = cv2.dilate(img_canny, kernel, iterations=1)
# Thinner lines
img_eroded = cv2.erode(img_dilated, kernel, iterations=1)
# Resize
img_resize = cv2.resize(img, (300,300))
# Crop using matrix [height start:end, width start:end]
img_cropped = img[0:200, 200:500]
cv2.imshow('Cropped', img_cropped)
cv2.waitKey(0)

# Webcam
# cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)
#
# while True:
#     success, img = cap.read()
#     cv2.imshow('Video', img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break