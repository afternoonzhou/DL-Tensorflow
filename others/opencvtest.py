import cv2
img = cv2.imread("D:\\butterfly.jpg")
SIFT = cv2.SIFT()
cv2.namedWindow("Image")
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()




