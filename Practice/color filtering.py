import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_red = np.array([0,45,50])
    upper_red = np.array([255,230,200])

    redmask = cv.inRange(hsv, lower_red, upper_red)
    res = cv.bitwise_and(frame, frame, mask = redmask)

    kernel = np.ones((5,5),np.uint8)
    erosion = cv.erode(redmask,kernel,iterations = 1)
    dilation = cv.dilate(redmask,kernel,iterations = 1)
    opening = cv.morphologyEx(redmask, cv.MORPH_OPEN, kernel)
    closing = cv.morphologyEx(redmask, cv.MORPH_CLOSE, kernel)



    # kernel = np.ones((15,15), np.float32)/225
    # smoothed = cv.filter2D(res, -1, kernel)
    # blur = cv.GaussianBlur(res, (15,1), 0)
    # median = cv.medianBlur(res, 15)
    # bilateral = cv.bilateralFilter(blur, 15, 75, 75)

    cv.imshow('res', res)
    cv.imshow('frame', frame)
    cv.imshow('erosion', erosion)
    cv.imshow('dilation', dilation)
    cv.imshow('opening', opening)
    cv.imshow('closing', closing)

    # cv.imshow('mask', redmask)
    # cv.imshow('smoothed', smoothed)
    # cv.imshow('blur', blur)
    # cv.imshow('median', median)
    # cv.imshow('bilateral', bilateral)



    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

