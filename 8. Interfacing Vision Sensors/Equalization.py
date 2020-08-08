# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 07:46:05 2018

@author: hao
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt

# In[]
image = cv2.imread('Photo/A01.jpg')

# In[]
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hist_g = cv2.calcHist([gray], [0], None, [256], [0, 256])

#cv2.imshow("Gray", gray)
eq = cv2.equalizeHist(gray)
hist_e = cv2.calcHist([eq], [0], None, [256], [0, 256])

cv2.imshow("Histogram Equalization", np.hstack([gray, eq]))
cv2.imwrite("mountain_eq.jpg", np.hstack([gray, eq]))

plt.plot(hist_g, 'b'); plt.xlim([0, 256])
plt.plot(hist_e, 'r'); plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

# In[]
# Settings
def auto_canny(image, sigma=0.1):
	# compute the median of the single channel pixel intensities
	v = np.median(image)
 
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
 
	# return the edged image
	return edged

kernel_size = 3 # Size of Sobel

imgA = cv2.imread('Photo/10cm_upper_right.jpg')
imgB = cv2.imread('Photo/10cm_no_cover.jpg')
imgC = cv2.imread('Photo/10cm_with_cover.jpg')

img = cv2.GaussianBlur(imgC, (5, 5), 0) # Denoise
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

# equalize the histogram of the Y channel
img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

# convert the YUV image back to RGB format
img_hist = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

fig = plt.figure()
plt.subplot(2,4,1),plt.imshow(imgA)
plt.title('10cm upper right'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,2),plt.imshow(imgB)
plt.title('10cm no cover (N/C)'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,3),plt.imshow(imgC)
plt.title('10cm with cover (W/C)'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,4),plt.imshow(img_hist)
plt.title('His. equ. from W/C'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,5),plt.imshow(auto_canny(imgA))
plt.title('Canny from U/R'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,6),plt.imshow(auto_canny(imgB))
plt.title('Canny from N/C'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,7),plt.imshow(auto_canny(imgC))
plt.title('Canny from W/C'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,8),plt.imshow(auto_canny(img_hist))
plt.title('Canny from H.E.'), plt.xticks([]), plt.yticks([])

plt.show()

fig.savefig('Results/10_cm_tool.jpg')