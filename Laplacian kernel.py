import cv2
import numpy as np

# Load the image
img = cv2.imread('C:/Users/nandhu/PycharmProjects/pythonProject/panda.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Define the modified Laplacian kernel with a positive center coefficient
a = 1.5
laplacian_kernel = np.array([
    [0, -1, 0],
    [-1, a, -1],
    [0, -1, 0]
])

# Apply the modified Laplacian kernel to the grayscale image
laplacian = cv2.filter2D(gray, -1, laplacian_kernel)

# Add the result of the modified Laplacian mask to the original image to create the sharpened image
sharpened = cv2.add(gray, laplacian)

# Display the original image and the sharpened image side by side
cv2.imshow('Original', img)
cv2.imshow('Sharpened', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
