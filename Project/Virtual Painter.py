import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

# i first created arrays for each upper and lower color
# this allows me to use them in the inRange function later to filter my colors

# red ranges
lower_red = np.array([160, 120, 100])
upper_red = np.array([180, 255, 255])

# green ranges
lower_green = np.array([35, 100, 100])
upper_green = np.array([85, 255, 255])

# blue ranges
lower_blue = np.array([85, 100, 100])
upper_blue = np.array([125, 255, 255])


while True:
    ret, frame = cap.read()
    frame = cv.flip(frame, 1)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) # i changed my image to hsv values

    # the following block creates a mask for the color red then merges it with my original frames with logical operations
    red_mask = cv.inRange(hsv, lower_red, upper_red)
    res_red = cv.bitwise_and(frame, frame, mask = red_mask)
    median_red = cv.medianBlur(res_red, 15)


    # the following block does the same for green
    green_mask = cv.inRange(hsv, lower_green, upper_green)
    res_green = cv.bitwise_and(frame, frame, mask=green_mask)
    median_green = cv.medianBlur(res_green, 15)


    # the same for blue
    blue_mask = cv.inRange(hsv, lower_blue, upper_blue)
    res_blue = cv.bitwise_and(frame, frame, mask=blue_mask)
    median_blue = cv.medianBlur(res_blue, 15)


    # I wrote the following codes to help me, they are commented out because they are not necessary to show
    # cv.imshow('red', res_red)
    # cv.imshow('green', res_green)
    # cv.imshow('blue', res_blue)

    cv.imshow('red', median_red)
    cv.imshow('green', median_green)
    cv.imshow('blue', median_blue)

    # this code breaks code to stop it when i press the spacebar
    if cv.waitKey(1) & 0xFF == ord(' '):
        break

cap.release()
cv.destroyAllWindows()