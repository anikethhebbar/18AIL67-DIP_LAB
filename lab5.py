import cv2
import numpy as np

# Read the image
img = cv2.imread("taylor.jpg", cv2.IMREAD_GRAYSCALE )

# Apply histogram equalization to enhance contrast
eq_img = cv2.equalizeHist(img)

# Apply adaptive thresholding to segment the image 
thresh = cv2.adaptiveThreshold(eq_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Apply morphological operations to further enhance segmentation
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# Display the original image, equalized image, and segmented image
cv2.imshow('Original Image', img)
cv2.imshow('Equalized Image', eq_img)
cv2.imshow('Segmented Image', opening)

# Wait for a key press and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows() 