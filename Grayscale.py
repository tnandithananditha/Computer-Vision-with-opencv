import cv2
import numpy as np
img = cv2.imread("C:/Users/nandhu/PycharmProjects/pythonProject/panda.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", img)
cv2.imshow("Grayscale", gray)
cv2.waitKey(0)
