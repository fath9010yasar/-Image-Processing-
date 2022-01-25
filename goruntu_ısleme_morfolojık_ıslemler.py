# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 16:03:05 2021

@author: Fatih
"""

import cv2
import numpy as np

resim=cv2.imread("C:/Users/Fatih/Desktop/New folder/fat.png")

kernel=np.ones((5,5),np.uint8)

dilation=cv2.dilate(resim, kernel,iterations=1)
erosion=cv2.erode(resim, kernel,iterations=1)


cv2.imshow("orijinal", dilation)
cv2.imshow("dilation", dilation)
cv2.imshow("erosion", erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()