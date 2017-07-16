import cv2
import numpy as np

img = cv2.imread("D:/butterfly.jpg")
#b, g, r = cv2.split(img)
b = cv2.split(img)[0]
g = cv2.split(img)[1]
r = cv2.split(img)[2]
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 13))

cv2.dilate(b, kernel)



# cv2.imshow("Blue", r)
# cv2.imshow("Red", g)
cv2.namedWindow("Green", cv2.WINDOW_NORMAL)
cv2.imshow("Green", img)

cv2.waitKey(0)
cv2.destroyAllWindows()



#可以操作np来分割通道
#import cv2
#import numpy as np

#img = cv2.imread("D:/cat.jpg")

#b = np.zeros((img.shape[0], img.shape[1]), dtype=img.dtype)
#g = np.zeros((img.shape[0], img.shape[1]), dtype=img.dtype)
#r = np.zeros((img.shape[0], img.shape[1]), dtype=img.dtype)

# b[:, :] = img[:, :, 0]
# g[:, :] = img[:, :, 1]
# r[:, :] = img[:, :, 2]
#
# cv2.imshow("Blue", r)
# cv2.imshow("Red", g)
# cv2.imshow("Green", b)
# cv2.waitKey(0)
# cv2.destroyAllWindows()