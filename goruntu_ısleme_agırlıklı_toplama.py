# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 12:24:32 2021

@author: Fatih
"""

import cv2
import numpy as np


resim=cv2.imread("C:/Users/Fatih/Desktop/New folder/ata.png")
resim1=cv2.imread("C:/Users/Fatih/Desktop/New folder/ata2.png")


print(resim[100,200])
print(resim1[200,430])
print(resim[100,200]+resim1[200,430])



cv2.imshow("ataturk", resim)
cv2.imshow("atrk",resim1)


cv2.waitKey(0)
cv2.destroyAllWindows()