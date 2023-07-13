import cv2
import numpy as np

# Load the image
img = cv2.imread('taylor.jpg', 0)

# Define the structuring element
kernel = np.ones((5,5), np.uint8)

# Perform erosion
erosion = cv2.erode(img, kernel, iterations=1)

# Perform dilation
dilation = cv2.dilate(img, kernel, iterations=1)

# Subtract the erosion result from the original image
edge_erosion = img - erosion

# Subtract the dilation result from the original image
edge_dilation = dilation - img

# Display the results
cv2.imshow('Original Image', img)
cv2.imshow('Erosion Result', erosion)
cv2.imshow('Dilation Result', dilation)
cv2.imshow('Edge Image (Erosion)', edge_erosion)
cv2.imshow('Edge Image (Dilation)', edge_dilation)
cv2.waitKey(0)
cv2.destroyAllWindows() 