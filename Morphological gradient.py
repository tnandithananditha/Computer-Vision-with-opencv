import cv2
import numpy as np

# Load the input image
img = cv2.imread('C:/Users/nandhu/PycharmProjects/pythonProject/panda.jpg', cv2.IMREAD_GRAYSCALE)

# Define the structuring element
kernel = np.ones((5,5), np.uint8)

# Apply Morphological Gradient operation
morph_gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# Display the output image
cv2.imshow('Output', morph_gradient)
cv2.waitKey(0)
