import cv2
import numpy as np

img =cv2.imread('taylor.jpg')
print("size of original image: height width",img.shape[:2])

rows,cols =img.shape[:2]
M=cv2.getRotationMatrix2D((cols/2, rows/2), 45,1)
rotated_img=cv2.warpAffine(img,M,(cols,rows))

scaled_img=cv2.resize(img,None,fx=0.01,fy=0.01,interpolation=cv2.INTER_LINEAR)
print("size of scaled image: height, width",img.shape[0:2])


M=np.float32([[1,0,100],[0,1,50]])
translated_img=cv2.warpAffine(img,M,(cols,rows))


cv2.resizeWindow('original image', 300, 300)
# Display the original and transformed images
cv2.imshow('Original Image', img)
cv2.imshow('Rotated Image', rotated_img)
cv2.imshow('Resized Image', scaled_img)
cv2.imshow('Translated Image', translated_img)

cv2.waitKey(0)
cv2.destroyAllWindows()