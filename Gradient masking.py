import cv2
import numpy as np

# Load the image
img = cv2.imread('C:/Users/surya/PycharmProjects/pythonProject/thalapathy.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create horizontal and vertical Sobel filters
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1)

# Apply the horizontal and vertical Sobel filters to the grayscale image to obtain the gradient images
gradient_x = cv2.convertScaleAbs(sobel_x)
gradient_y = cv2.convertScaleAbs(sobel_y)

# Add the gradient images together to obtain the total gradient image
total_gradient = cv2.addWeighted(gradient_x, 0.5, gradient_y, 0.5, 0)

# Invert the total gradient image
inverted_gradient = cv2.bitwise_not(total_gradient)

# Add the inverted total gradient image to the original grayscale image to obtain the sharpened image
sharpened = cv2.addWeighted(gray, 1, inverted_gradient, 1, 0)

# Display the original image and the sharpened image side by side
cv2.imshow('Original', img)
cv2.imshow('Sharpened', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
