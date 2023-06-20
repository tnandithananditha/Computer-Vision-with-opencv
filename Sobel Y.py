# Edge detection using Sobel Matrix along Y axis
import cv2
import numpy as np

img = cv2.imread('C:/Users/nandhu/PycharmProjects/pythonProject/panda.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobely = np.uint8(np.absolute(sobely))
cv2.imshow('Sobel Y', sobely)
cv2.waitKey(0)
cv2.destroyAllWindows()
