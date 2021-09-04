#pip install cv2

import cv2 as cv
#import the path of a image
img = cv.imread('img path')

gray = cv.cvtColor(img, cv.COLOR_BGR2RGB)

cv.imshow("gray", gray)
cv.waitKey(0)
