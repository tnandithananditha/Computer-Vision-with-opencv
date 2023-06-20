import cv2
img = cv2.imread("C:/Users/nandhu/PycharmProjects/pythonProject/panda.jpg")
(h, w) = img.shape[:2]
angle = 45
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated = cv2.warpAffine(img, M, (w, h))
cv2.imshow("Original", img)
cv2.imshow("Rotated (Angle {})".format(angle), rotated)
cv2.waitKey(0)
