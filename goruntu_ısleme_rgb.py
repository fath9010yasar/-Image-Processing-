# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 21:56:59 2021

@author: Fatih
"""

import cv2
import numpy as np

ataresmi = cv2.imread("C:/Users/Fatih/Desktop/New folder/ata.png")


cv2.imshow("ataturk", ataresmi)

print(ataresmi[(230,80)])

print("Resmin Boyutu: " +str(ataresmi.size))
print("Resmin Özellikleri: " +str(ataresmi.shape))
print("Resmin Veri Tipi: " +str(ataresmi.dtype))






cv2.waitKey(0)
cv2.destroyAllWindows()

