import cv2 as cv


img3 = cv.imread("img3.jpg")
img1 = cv.imread("img1.jpg")

subtractedImages = img3 - img1


cv.imshow("Subtracted", subtractedImages)
cv.waitKey(0)