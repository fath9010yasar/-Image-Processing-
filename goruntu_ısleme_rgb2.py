# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 22:24:51 2021

@author: Fatih
"""

import cv2
import numpy as np

resim=cv2.imread("C:/Users/Fatih/Desktop/New folder/ata.png")

resim[250,30]=[255,255,255]

for i in range(300):
    resim[250,i]=[255,255,255]
    resim[260,i]=[255,25,255]

cv2.imshow("ataturk", resim)

cv2.waitKey(0)
cv2.destroyAllWindows()







