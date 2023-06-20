# Edge detection using Sobel Matrix along X axis
import cv2
import numpy as np

img = cv2.imread('C:/Users/nandhu/PycharmProjects/pythonProject/panda.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobelx = np.uint8(np.absolute(sobelx))
cv2.imshow('Sobel X', sobelx)
cv2.waitKey(0)
cv2.destroyAllWindows()
