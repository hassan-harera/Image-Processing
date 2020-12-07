import cv2 as cv
import numpy as np

img1 = cv.imread("img2.jpg")


# for i in range(img1.shape[0]):
#     for j in range(img1.shape[1]):
#         for k in range(img1.shape[2]):
#             if(1.3 * img1[i][j][k] + 10) < 256:
#                 img1[i][j][k] = 1.3 * img1[i][j][k] + 10


def change_contrast(img1, alpha, beta):
    for y in range(img1.shape[0]):
        for x in range(img1.shape[1]):
            for c in range(img1.shape[2]):
                img1[y, x, c] = np.clip(alpha * img1[y, x, c] + beta, 0, 255)
    return img1


img1 = change_contrast(img1, 1.5, 10)

cv.imshow("Image", img1)
cv.waitKey(0)
