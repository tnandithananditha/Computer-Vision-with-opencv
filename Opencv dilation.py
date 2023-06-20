import cv2
import numpy as np

# Load the image
img = cv2.imread('C:/Users/nandhu/PycharmProjects/pythonProject/panda.jpg', cv2.IMREAD_GRAYSCALE)

# Define the structuring element
kernel = np.ones((5,5), np.uint8)

# Apply dilation
dilation = cv2.dilate(img, kernel, iterations=1)

# Show the results
cv2.imshow('Input Image', img)
cv2.imshow('Dilated Image', dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()
