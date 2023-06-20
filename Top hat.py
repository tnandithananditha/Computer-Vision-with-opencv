import cv2
import numpy as np

# Load the input image
img = cv2.imread('C:/Users/nandhu/PycharmProjects/pythonProject/panda.jpg', cv2.IMREAD_GRAYSCALE)

# Define the structuring element
kernel = np.ones((5,5), np.uint8)

# Apply Top hat operation
top_hat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# Display the output image
cv2.imshow('Output', top_hat)
cv2.waitKey(0)
