import cv2

img = cv2.imread('D:\\butterfly.jpg')
r = img[:, :, 0]
retVal, reg = cv2.threshold(r, 50, 255, cv2.THRESH_BINARY)
contour = cv2.findContours(reg, 1, 2)
cv2.drawContours(img, contour[1], -1, (255, 0, 0))
cv2.namedWindow('Img_window', cv2.WINDOW_NORMAL)
cv2.imshow('Img_window', img)

cv2.waitKey(0)

