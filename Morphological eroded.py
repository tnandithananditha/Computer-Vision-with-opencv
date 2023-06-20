import cv2
import numpy as np

# Load the input image in grayscale
img = cv2.imread('C:/Users/nandhu/PycharmProjects/pythonProject/panda.jpg', cv2.IMREAD_GRAYSCALE)

# Define the erosion kernel
kernel_size = (5, 5)
kernel = np.ones(kernel_size, dtype=np.uint8)

# Perform erosion on the input image
eroded = cv2.erode(img, kernel, iterations=1)

# Save the resulting image
cv2.imwrite('eroded_image.jpg', eroded)
