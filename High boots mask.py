import cv2
import numpy as np

# Load the image
img = cv2.imread('C:/Users/nandhu/PycharmProjects/pythonProject/panda.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create a Laplacian filter
laplacian_filter = cv2.Laplacian(gray, cv2.CV_64F)

# Apply the Laplacian filter to the grayscale image to obtain the Laplacian image
laplacian_image = cv2.convertScaleAbs(laplacian_filter)

# Define a high-boost filter mask
factor = 2.0
highboost_mask = gray.astype(float) * factor - laplacian_image

# Apply the high-boost filter mask to the grayscale image to obtain the sharpened image
sharpened = cv2.convertScaleAbs(highboost_mask)

# Display the original image and the sharpened image side by side
cv2.imshow('Original', img)
cv2.imshow('Sharpened', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
