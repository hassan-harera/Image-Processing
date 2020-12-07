import cv2


img = cv2.imread("Skull.jpg")

width = int(img.shape[0])
height = int(img.shape[1])

for i in range(width):
    for j in range(height):
        img[i][j] = img[i][j] * 2;

cv2.imshow("Image", img)
cv2.waitKey(0)