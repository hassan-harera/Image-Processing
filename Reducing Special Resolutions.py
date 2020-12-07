import cv2


def rescale_frame(Frame, percent=75):
    width = int(Frame.shape[1] * percent / 100)
    height = int(Frame.shape[0] * percent / 100)
    dim = (width, height)
    return cv2.resize(Frame, dim, interpolation=cv2.INTER_AREA)


frame = cv2.imread("news.png")
frame75 = rescale_frame(frame, percent=75)
cv2.imshow('frame75', frame75)
frame150 = rescale_frame(frame, percent=150)
cv2.imshow('frame150', frame150)

cv2.waitKey(0)
cv2.destroyAllWindows()
