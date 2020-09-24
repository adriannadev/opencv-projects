import cv2
import numpy as np

width = 640
height = 460
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)
cap.set(10, 150)

def preprocessing(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (5,5), 1)
    img_canny = cv2.Canny(img_blur, 200,200)
    kernel = np.ones((5,5))
    img_dial = cv2.dilate(img_canny, kernel, iterations=2)
    img_thres = cv2.erode(img_dial, kernel, iterations=1)
    return img_thres

def get_contours(img):
    biggest = np.array([])
    max_area = 0
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            # cv2.drawContours(img_cont, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            if area>max_area and len(approx) == 4:
                biggest = approx
                max_area = area
    cv2.drawContours(img_cont, biggest, -1, (255, 0, 0), 30)
    return biggest

def reorder(my_points):
    my_points = my_points.reshape((4,2))
    new_points = np.zeros((4,1,2), np.int32)
    add = my_points.sum(1)
    new_points[0] = my_points[np.argmin(add)]
    new_points[3] = my_points[np.argmax(add)]
    diff = np.diff(my_points, axis=1)
    new_points[1] = my_points[np.argmin(diff)]
    new_points[2] = my_points[np.argmax(diff)]
    return new_points

def get_warp(img, biggest):
    biggest = reorder(biggest)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    img_output = cv2.warpPerspective(img, matrix, (width, height))

    img_cropped = img_output[20:img_output.shape[0]-20, 20:img_output.shape[1]-20]
    img_cropped = cv2.resize(img_cropped, (width, height))

    return img_output

while True:
    success, img = cap.read()
    img = cv2.resize(img, (width, height))
    img_cont = img.copy()

    img_thres = preprocessing(img)
    biggest = get_contours(img_thres)
    print(biggest)

    if biggest.size !=0:
        img_warped = get_warp(img, biggest)
    else:
        img_warped = img_cont

    cv2.imshow('Video', img_warped)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break