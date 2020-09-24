import cv2

img = cv2.imread('car.jpg')
num_casc = cv2.CascadeClassifier('haarcascades/haarcascade_russian_plate_number.xml')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plates = num_casc.detectMultiScale(img_gray, 1.1, 4)

for (x, y, w, h) in plates:
    area = w*h
    if area >500:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(img, 'Number Plate', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 0, 0), 2)
        img_roi = img[y:y+h, x:x+w]
        cv2.imshow('ROI', img_roi)

cv2.imshow('Output',img)
if cv2.waitKey(0) & 0xFF == ord('s'):
    cv2.imwrite('numplate.jpg', img_roi)
    cv2.rectangle(img, (0,200), (700,300), (0,255,0), cv2.FILLED)
    cv2.putText(img, 'Scan saved', (150, 265), cv2.FONT_HERSHEY_SIMPLEX,
                2, (0, 0, 255), 2)
    cv2.imshow('Result', img)
    cv2.waitKey(1000)