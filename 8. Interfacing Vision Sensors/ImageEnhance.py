# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 07:46:05 2018

@author: hao
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt

# In[]
def auto_canny(image, sigma=0.15):
	# compute the median of the single channel pixel intensities
	v = np.median(image)
 
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
 
	# return the edged image
	return edged

imgA = cv2.imread('Photo/20cm_upper_right.jpg')
imgB = cv2.imread('Photo/20cm_no_cover.jpg')
imgT = cv2.imread('Photo/20cm_with_cover.jpg')

# In[]
img = cv2.GaussianBlur(imgT, (3, 3), 0) # Denoise
imgT_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV) # conver to YUV

# equalize the histogram of the Y channel
imgT_yuv[:,:,0] = cv2.equalizeHist(imgT_yuv[:,:,0])

# convert the YUV image back to RGB format
imgT_hist = cv2.cvtColor(imgT_yuv, cv2.COLOR_YUV2BGR)

fig = plt.figure()
plt.subplot(2,4,1),plt.imshow(imgA)
plt.title('upper right'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,2),plt.imshow(imgB)
plt.title('no cover (N/C)'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,3),plt.imshow(imgT)
plt.title('with cover (W/C)'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,4),plt.imshow(imgT_hist)
plt.title('His. equ. from W/C'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,5),plt.imshow(auto_canny(imgA))
plt.title('Canny from U/R'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,6),plt.imshow(auto_canny(imgB))
plt.title('Canny from N/C'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,7),plt.imshow(auto_canny(imgT))
plt.title('Canny from W/C'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,8),plt.imshow(auto_canny(imgT_hist))
plt.title('Canny from H.E.'), plt.xticks([]), plt.yticks([])

plt.show()

fig.savefig('Results/20_cm_tool.jpg')