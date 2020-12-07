import cv2 as cv
import numpy as np

img1 = cv.imread("img1.jpg")
img2 = cv.imread("img2.jpg")

addedImages = img2 + img1

cv.imshow("Subtracted", addedImages)
cv.waitKey(0)

# for i in range(img1.shape[0]):
#     for j in range(img1.shape[1]):