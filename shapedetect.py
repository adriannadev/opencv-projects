import cv2

def get_contours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        cv2.drawContours(img_contour, cnt, -1, (255, 0, 0), 3)
        if area>500:
            cv2.drawContours(img_contour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            obj_corn = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if obj_corn ==3: objectType = "Tri"
            elif obj_corn ==4:
                asp_ratio = w/float(h)
                if asp_ratio>0.95 and asp_ratio<1.05: objectType = 'Square'
                else: objectType = "Rectangle"
            elif obj_corn>4: objectType = "Circle"
            else: objectType = "None"
            cv2.rectangle(img_contour, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(img_contour,objectType,
                        (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        (0, 0, 0), 2)

img = cv2.imread('shapes.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7,7), 1)
img_canny = cv2.Canny(img_blur, 50, 50)
img_contour = img.copy()
get_contours(img_canny)

cv2.imshow('Result', img_contour)
cv2.waitKey(0)