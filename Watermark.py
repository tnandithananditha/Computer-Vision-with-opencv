import cv2
import numpy as np

# Load the original image and the watermark image
img = cv2.imread('C:/Users/nandhu/PycharmProjects/pythonProject/panda.jpg')
watermark = cv2.imread('watermark.png')

# Resize the watermark image to match the size of the original image
watermark = cv2.resize(watermark, (img.shape[1], img.shape[0]))

# Add the watermark to the original image
watermarked = cv2.addWeighted(img, 1, watermark, 0.5, 0)

# Save the watermarked image
cv2.imwrite('watermarked_image.jpg', watermarked)
