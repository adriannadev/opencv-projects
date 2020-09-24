import cv2
import numpy as np
# (width, height, color channels)
img = np.zeros((512, 512, 3), np.uint8)
# Add color with pixel range
# img[50:100, 200:300]=255, 0, 0
# Draw a line: img, starting point, img width, img height, color, thickness
cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
# Draw a rectangle
cv2.rectangle(img, (0,0), (250, 350), (0,0,255), cv2.FILLED)
# Draw a circle: img, starting point, radius, color, thickness
cv2.circle(img, (400,50), 30, (255,255,0),5)
# Add text: img, text, starting point, font, scale, color, thickness
cv2.putText(img, "OPENCV", (300, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 150, 0), 2)
cv2.imshow('Image',img)
cv2.waitKey(0)