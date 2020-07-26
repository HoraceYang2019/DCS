# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 09:07:08 2018

@author: hao
"""
import cv2

# In[1]
camera = cv2.VideoCapture(0)
cv2.namedWindow("Camera Frame")

img_counter = 0

while True:
    ret, frame = camera.read()
    cv2.imshow("Frame", frame)
    
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
 
camera.release()

cv2.destroyAllWindows()
