

import cv2 as cv

### Reading photos

# image = cv.imread('coraline.jpg')
# cv.imshow('coraline image', image)
#
# cv.waitKey(0)
# cv.destroyAllWindows()


### Reading videos

# video = cv.VideoCapture('recording.mp4')
#
# while True:
#     isTrue, frame = video.read()
#
#     if isTrue:
#         cv.imshow('recording', frame)
#         if cv.waitKey(20) & 0xFF == ord('x'):
#             break
#
#     else:
#         break
#
# video.release()
# cv.destroyAllWindows()


#### camera feed

# vid = cv.VideoCapture(0)
#
# while True:
#     isTrue, frame = vid.read()
#     cv.imshow('camera', frame)
#
#     if cv.waitKey(3) & 0xFF == ord('x'):
#         break
#
# vid.release()
# cv.destroyAllWindows()




### resizing images

# img = cv.imread('coraline.jpg')
# img_resized = cv.resize(img,(800,500), interpolation=cv.INTER_CUBIC)
# print(img_resized.shape)
# cv.imshow('resized', img_resized)
# cv.waitKey(0)
# cv.destroyAllWindows()



### cropping pictures

# img = cv.imread('coraline.jpg')
# img_cropped = img[0:400, 0:800]
# cv.imshow('cropped',img_cropped)
# cv.waitKey(0)
# cv.destroyAllWindows()




### drawing on image

# import numpy as np
#
# empty = np.zeros((600,600,3), dtype='uint8')
# cv.imshow('img',empty)
#
# empty[:] = 250,0,140  #BGR
# cv.imshow('coloured',empty)
#
# cv.rectangle(empty,(0,0),(400,400),(0,0,120),thickness=3)
# cv.imshow('rectangle',empty)
#
#
# cv.line(empty,(0,0),(400,400),(0,0,120),thickness=3)
# cv.imshow('line',empty)
#
#
# cv.circle(empty,(200,200),100,(0,0,120),thickness=3)
# cv.imshow('circle',empty)
#
#
# cv.putText(empty, 'This is my start point!', (0,500), cv.FONT_HERSHEY_TRIPLEX, 1.0, (100,50,70), thickness=2)
# cv.imshow('text',empty)
#
# cv.waitKey(0)
# cv.destroyAllWindows()




image = cv.imread('coraline.jpg', cv.IMREAD_GRAYSCALE)
cv.imshow('coraline image', image)

cv.waitKey(0)
cv.destroyAllWindows()