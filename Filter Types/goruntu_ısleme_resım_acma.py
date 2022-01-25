# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 12:34:26 2021

@author: Fatih
"""

import cv2
import numpy as np

resim=cv2.imread("C:/Users/Fatih/Desktop/New folder/ata.png")



cv2.imshow("ataturk",resim)

print(resim.size)


cv2.waitKey(0)

cv2.destroyAllWindows()