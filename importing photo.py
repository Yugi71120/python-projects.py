import cv2 as cv

img = cv.imread('D:\\codes\\PycharmProjects\\pythonproject3\\code.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2RGB)

cv.imshow("gray", gray)
cv.waitKey(0)
