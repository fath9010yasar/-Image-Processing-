# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 18:40:05 2021

@author: Fatih
"""

import cv2

resim=cv2.imread("C:/Users/Fatih/Desktop/New folder/hav.jpg",0)

ret,thresh=cv2.threshold(resim, 127, 255, cv2.THRESH_BINARY)
ret,thresh1=cv2.threshold(resim, 127, 255, cv2.THRESH_BINARY_INV)
ret,thresh2=cv2.threshold(resim, 127, 255, cv2.THRESH_TRUNC)
ret,thresh3=cv2.threshold(resim, 127, 255, cv2.THRESH_TOZERO)
ret,thresh4=cv2.threshold(resim, 127, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow("orijinal", resim)
cv2.imshow("tresh", thresh)
cv2.imshow("tresh1", thresh1)
cv2.imshow("tresh2", thresh2)
cv2.imshow("tresh3", thresh3)
cv2.imshow("tresh4", thresh4)



cv2.waitKey(0)
cv2.destroyAllWindows()






