import cv2 as cv
import numpy as np

img = cv.imread('first.JPG')

ret, threshold = cv.threshold(img, 20, 255, 0)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret1, threshold1 = cv.threshold(gray, 20, 255, 0)
gaus = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 115, 1)

cv.imshow('threshold', threshold)
cv.imshow('threshold1', threshold1)
cv.imshow('gaus', gaus)

cv.waitKey(0)
cv.destroyAllWindows()
