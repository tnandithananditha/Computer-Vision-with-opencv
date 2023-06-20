# Edge detection using Sobel Matrix along XY axis
import cv2
import numpy as np

img = cv2.imread('C:/Users/nandhu/PycharmProjects/pythonProject/panda.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
grad_x = cv2.filter2D(gray, cv2.CV_64F, sobel_x)
grad_y = cv2.filter2D(gray, cv2.CV_64F, sobel_y)
grad_mag = np.sqrt(grad_x**2 + grad_y**2)
grad_dir = np.arctan2(grad_y, grad_x)
thresh = 50
grad_mag[grad_mag < thresh] = 0
grad_mag = np.uint8(grad_mag)
cv2.imshow('Sobel Edge Detection', grad_mag)
cv2.waitKey(0)
cv2.destroyAllWindows()
