# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 20:00:25 2018
https://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_Image_Gradient_Sobel_Laplacian_Derivatives_Edge_Detection.php
@author: hao
"""

import cv2
from matplotlib import pyplot as plt

# In[1]: Load and preprocess
img = cv2.imread('Photo/Lenna.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# remove noise
gray = cv2.GaussianBlur(gray,(3,3),0)

# In[]

laplacian = cv2.Laplacian(gray, cv2.CV_64F)
sobelx = cv2.Sobel(gray, cv2.CV_64F, 2, 0, ksize=5)  # x
''' parameter1: image
    parameter2: cv2.CV_64F(64 bits float)  Depth of output image is passed -1 to get the result in np.uint8 type.
    parameter3: X gradient 0: original; 1: 1 order; 2: 2 order
    parameter4: Y gradient 0: original; 1: 1 order; 2: 2 order
    parameter5: kernel size default 3,  '''
    
    
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 2, ksize=5)  # y

edges = cv2.Canny(gray, 100, 200)
  # edge = cv2.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient ]]]) 
  
ret, binary = cv2.threshold(gray, 127, 255, 0) # transform into binary 
im2, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(gray, contours,-1,(0, 0, 255), 3)
  
plt.subplot(2,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(2,3,2),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])

plt.subplot(2,3,3),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.subplot(2,3,4),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])

plt.subplot(2,3,5),plt.imshow(edges, cmap = 'gray')
plt.title('Canny'), plt.xticks([]), plt.yticks([])

plt.subplot(2,3,6),plt.imshow(binary, cmap = 'gray')
plt.title('Contour'), plt.xticks([]), plt.yticks([])

plt.show()

# In[]
cv2.imwrite('Results/EdgeDetected.png', edges)
