import cv2
import numpy as np

# Read the image
img = cv2.imread('taylor.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Canny edge detection
edges = cv2.Canny(img, 100, 200)

# Apply Sobel filter for texture detection
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
texture = np.sqrt(sobel_x ** 2 + sobel_y ** 2)

# Show the images in the windows
cv2.imshow('Original Image', img)
cv2.imshow('Canny Edges', edges)
cv2.imshow('Texture', texture)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows() 