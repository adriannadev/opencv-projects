import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

#h_min, s_min, v_min, h_max, s_max, v_max for color detection
my_colors = [[4,188,193,21,238,255],
            [133,56,0,159,156,255],
            [57,76,0,100,255,255]]

# Painting colors
my_colors_v = [[9, 87, 234],
               [183, 74, 121],
               [68, 112, 22]]

# [x, y, color_id]
my_points = []

def find_color(img, my_colors, my_colors_v):
    img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    new_points=[]
    for color in my_colors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(img_HSV, lower, upper)
        x, y = get_contours(mask)
        # Draw a color circle by detected color
        cv2.circle(img_result, (x, y), 10, my_colors_v[count], cv2.FILLED)
        if x!=0 and y!=0:
            new_points.append([x, y, count])
        count+=1
        # cv2.imshow(str(color[0]), mask)
    return new_points

def get_contours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # cv2.drawContours(img_result, cnt, -1, (255, 0, 0), 3)
        if area>500:
            # cv2.drawContours(img_result, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2, y

def draw_on_canvas(my_points, my_colors_v):
        for point in my_points:
            cv2.circle(img_result, (point[0], point[1]), 10, my_colors_v[point[2]], cv2.FILLED)

while True:
    success, img = cap.read()
    img_result = img.copy()
    new_points = find_color(img, my_colors, my_colors_v)
    if len(new_points)!=0:
        for newp in new_points:
            my_points.append(newp)
    if len(my_points)!=0:
        draw_on_canvas(my_points, my_colors_v)

    cv2.imshow('Video', img_result)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
