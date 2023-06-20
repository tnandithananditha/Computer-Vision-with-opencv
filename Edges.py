#Edge detection using canny method

import cv2

import numpy as np

img = cv2.imread("C:/Users/nandhu/PycharmProjects/pythonProject/panda.jpg")

edges = cv2.Canny(img, 100, 200)

cv2.imshow("Original", img)

cv2.imshow("Edges", edges)

cv2.waitKey(0)
