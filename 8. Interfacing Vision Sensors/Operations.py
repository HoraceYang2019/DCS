# -*- coding: utf-8 -*-
"""
pip install opencv-contrib-python
check opencv version: 
    cv2.__version__
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

# In[1]: original image
image = cv2.imread("Photo/A02.jpg")
cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

color = ('b','g','r')
for i, col in enumerate(color):
  histr = cv2.calcHist([image],[i],None,[256],[0, 256])
  plt.plot(histr, color = col)
  plt.xlim([0, 256])
plt.show()

# In[2]: resize
rows, cols = image.shape[:2]
resize = cv2.resize(image, (0.2*cols, 0.2*rows), interpolation = cv2.INTER_CUBIC)
cv2.imshow('Resize', resize)
cv2.waitKey(0)
cv2.destroyAllWindows()

# In[3]: Convert RGB to Gray/HSV
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
 # cv2.calcHist(image, channel, mask, bins, pixel range)
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
gray_r = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
hist_r = cv2.calcHist([gray_r], [0], None, [256], [0, 256])

plt.plot(hist, 'b')
plt.plot(hist_r, 'r')
plt.show()
cv2.waitKey(0)

# Convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)
cv2.waitKey(0)

# Convert HSV to RGB
bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imshow("BGR", bgr)
cv2.waitKey(0)

cv2.destroyAllWindows()

# In[4]: Mask Image 
mask = np.zeros(gray.shape, np.uint8)
mask[60:130, 50:180] = 255

# calculate image with mask
masked_gray = cv2.bitwise_and(gray, gray, mask = mask)

# historgram of orignial image
hist_full = cv2.calcHist([image], [0], None, [256], [0, 256])

# historgram of masked image
hist_mask = cv2.calcHist([image], [0], mask, [256], [0, 256])

# show result
plt.subplot(221), plt.imshow(gray, 'gray')
plt.subplot(222), plt.imshow(mask, 'gray')
plt.subplot(223), plt.imshow(masked_gray, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0,256])

plt.show()

# In[5]: Shift/Rotate
def shift(image, x, y):
    # define shift matrix
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return shifted

def rotate(image, angle, center=None, scale=1.0):
    (h, w) = image.shape[:2]
    if center is None:
        center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated

shifted = shift(image, 50, 30)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)

angle = 30
rotated = rotate(image, angle)
cv2.imshow("Rotated", rotated)
cv2.waitKey(0)

# In[6]: 微分
n,m=gray.shape
y0=np.full((1,m),255)
grayy = np.vstack((gray[1:,],y0))
dy=grayy-gray

# In[7]:  gamma correction

def adjust_gamma(image, gamma=1.0):

   invGamma = 1.0 / gamma
   table = np.array([((i / 255.0) ** invGamma) * 255
      for i in np.arange(0, 256)]).astype("uint8")

   return cv2.LUT(image, table)

cv2.imshow('original', image)

gamma = 3                                   # change the value here to get different result
adjusted = adjust_gamma(image, gamma=gamma)
cv2.putText(adjusted, "gamma={}".format(gamma), (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
cv2.imshow("gammam image 1", adjusted)

cv2.waitKey(0)
cv2.destroyAllWindows()
