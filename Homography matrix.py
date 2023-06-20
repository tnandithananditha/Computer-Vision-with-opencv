#Homography Matrix
import cv2
import numpy as np
image = cv2.imread('C:/Users/nandhu/PycharmProjects/pythonProject/panda.jpg')
target_points = np.array([[0, 0], [500, 0], [500, 500], [0, 500]], dtype=np.float32)
source_points = np.array([[141, 131], [480, 159], [493, 630], [64, 601]], dtype=np.float32)
homography_matrix, _ = cv2.findHomography(source_points, target_points)
transformed_image = cv2.warpPerspective(image, homography_matrix, (500, 500))
cv2.imshow('Original Image', image)
cv2.imshow('Transformed Image', transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
