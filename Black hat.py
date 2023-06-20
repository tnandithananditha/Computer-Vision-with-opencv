import cv2
import numpy as np

# Load the input image
img = cv2.imread("C:/Users/surya/PycharmProjects/pythonProject/thalapathy.jpg", cv2.IMREAD_GRAYSCALE)

# Define the structuring element
kernel = np.ones((5,5), np.uint8)

# Apply Black hat operation
black_hat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

# Display the output image
cv2.imshow('Output', black_hat)
cv2.waitKey(0)
