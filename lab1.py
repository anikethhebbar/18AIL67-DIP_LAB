#p1
import cv2
import numpy as np

img = cv2.imread('taylor.jpg')

height, width = img.shape[:2]
center_x, center_y = int(width/2), int(height/2)
top_left = img[0:center_y, 0:center_x]
top_right = img[0:center_y, center_x:width]
bottom_left = img[center_y:height, 0:center_x]
bottom_right = img[center_y:height, center_x:width]



cv2.imshow('Top Left', top_left)
cv2.imshow('Top Right', top_right)
cv2.imshow('Bottom Left', bottom_left)
cv2.imshow('Bottom Right', bottom_right)
cv2.waitKey(0)
cv2.destroyAllWindows() 