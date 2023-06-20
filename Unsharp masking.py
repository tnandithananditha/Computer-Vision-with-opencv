import cv2
import numpy as np

# Load the image
img = cv2.imread('C:/Users/nandhu/PycharmProjects/pythonProject/panda.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply a Gaussian blur to the grayscale image
blur = cv2.GaussianBlur(gray, (0, 0), 3)

# Subtract the blurred image from the original grayscale image to obtain the high-pass image
highpass = cv2.subtract(gray, blur)

# Scale the high-pass image by a factor and add it back to the original grayscale image to create the sharpened image
factor = 1.5
sharpened = cv2.addWeighted(gray, 1 + factor, highpass, -factor, 0)

# Display the original image and the sharpened image side by side
cv2.imshow('Original', img)
cv2.imshow('Sharpened', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
