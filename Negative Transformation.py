import cv2 
import matplotlib.pyplot as plt 


# Read an image 
img_bgr = cv2.imread('img2.jpg', 1)
plt.imshow(img_bgr) 

# get height and width of the image 
height, width, _ = img_bgr.shape 

for i in range(0, height - 1): 
	for j in range(0, width - 1): 

		pixel = img_bgr[i, j] 
		
		pixel[0] = 255 - pixel[0] 
		
		pixel[1] = 255 - pixel[1] 
		
		pixel[2] = 255 - pixel[2] 
		
		img_bgr[i, j] = pixel 


plt.imshow(img_bgr) 
plt.show() 
