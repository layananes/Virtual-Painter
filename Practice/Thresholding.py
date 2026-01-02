import cv2 as cv
import numpy as np

# cap = cv.VideoCapture(0)
#
# while True:
#     ret, frame = cap.read()
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#
#     cv.imshow('frame', frame)
#     cv.imshow('gray', gray)
#
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv.destroyAllWindows()





# img = cv.imread('coraline.jpg')
#
# cv.line(img, (0,0), (700,700), (90,0,20), 10)
# cv.rectangle(img, (300,300), (900,900), (0, 255, 0), 5 )
# cv.circle(img, (300,300), 100, (0,0,255), -5)
#
# pts = np.array([[100,100],[100,400], [400, 200]], np.int32)
# cv.polylines(img, [pts], True, (255,0,0), 4)
#
# cv.putText(img, 'this is fun!', (100, 700),cv.FONT_HERSHEY_TRIPLEX,5, (255,255,255), 4)
# cv.imshow('image', img)
# cv.waitKey(0)
# cv.destroyAllWindows()


# img = cv.imread('coraline.jpg')
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# pixel = img[100,100]
# print(pixel) # we check the pixel BGR value
# img[200,100] = [255,255,255] # makes pixel [100,100] white
# print(pixel)

# cv.imshow('white pixel', img)
# cv.waitKey(0)
# cv.destroyAllWindows()


# REGION OF IMAGE
# roi = img[0:100, 0:700]
# img[0:100, 0:700] = [255,255,255] # changes the color of a whole region of pixels

# cv.imshow('white region', img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# copy_face = img[0:100, 0:700]
# img[200:300, 200:900]= copy_face # copies [0:100, 0:700] region and pastes it to the other region
#
# cv.imshow('copy and paste', img)
# cv.waitKey(0)
# cv.destroyAllWindows()



#######################################################################################
# img1 = cv.imread('first.JPG')
# img2 = cv.imread('second.JPG')

# add = img1 + img2
# add = cv.add(img1, img2)
# weighted = cv.addWeighted(img1, 0.5, img2, 0.5, 0)

img1 = cv.imread('first.JPG')
img2 = cv.imread('smaller.JPG')
cv.imshow('img1', img1)
cv.imshow('img2', img2)

rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols]

img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 200, 255, cv.THRESH_BINARY)

cv.imshow('mask', mask)

mask_inv = cv.bitwise_not(mask)
cv.imshow('mask_inv', mask_inv)

img1_bg = cv.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv.bitwise_and(img2, img2, mask=mask)
cv.imshow('img1_bg', img1_bg)
cv.imshow('img2_fg', img2_fg)

dst = cv.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst




cv.imshow('dst', dst)
cv.imshow('img1', img1)

cv.waitKey(0)
cv.destroyAllWindows()
########################################################################################



