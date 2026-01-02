import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    laplacian = cv.Laplacian(frame, cv.CV_64F, ksize=5)
    sobelx = cv.Sobel(frame, cv.CV_64F, 1, 0, ksize=5)
    sobely = cv.Sobel(frame, cv.CV_64F, 0, 1, ksize=5)
    edges = cv.Canny(frame, 100, 200)

    cv.imshow('laplacian', laplacian)
    cv.imshow('original', frame)
    cv.imshow('sobelx', sobelx)
    cv.imshow('edges', edges)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()