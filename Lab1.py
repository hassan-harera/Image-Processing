import numpy as np
import cv2 as ocv

def im2double():
    min_pixel=np.min(im)
    max_pixel=np.max(im)
    return (im-min_pixel)/(max_pixel-min_pixel)

im = np.zeros((800,800))
im = ocv.imread('news.png',0)
row,col=np.shape(im)

im=im2double()
ocv.imshow("before",im)
for r in range(1,row-1,1):
    for c in range(1,col-1,1):
        im[r][c]=(im[r][c]*(1/9))+(im[r][c-1]*(1/9))+(im[r][c+1]*(1/9))+(im[r-1][c+1]*(1/9))+\
                 (im[r-1][c]*(1/9))+(im[r-1][c-1]*(1/9))+(im[r+1][c+1]*(1/9))\
                 +(im[r+1][c]*(1/9))+(im[r+1][c-1]*(1/9))
ocv.imshow("after",im)
ocv.waitKey()
