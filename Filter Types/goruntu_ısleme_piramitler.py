# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 13:15:11 2021

@author: Fatih
"""

import cv2
import numpy as np

resim=cv2.imread("C:/Users/Fatih/Desktop/New folder/ata.png")


ikikat=cv2.pyrUp(resim)
ikikatkucuk=cv2.pyrDown(resim)

cv2.imshow("ataturk",resim)
cv2.imshow("ikikat", ikikat)
cv2.imshow("ikikatkucuk", ikikatkucuk)




cv2.waitKey(0)

cv2.destroyAllWindows()