#Sharpening of Image using Laplacian mask with negative center coefficient.
import cv2
import numpy as np

img = cv2.imread('C:/Users/nandhu/PycharmProjects/pythonProject/panda.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3, 3), 0)
laplacian = cv2.Laplacian(blur, cv2.CV_64F, ksize=3)
sharp = gray - 0.5*laplacian
sharp = np.uint8(sharp)
cv2.imshow('Original', img)
cv2.imshow('Sharpened', sharp)
cv2.waitKey(0)
cv2.destroyAllWindows()
