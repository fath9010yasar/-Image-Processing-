# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 12:45:15 2021

@author: Fatih
"""

import cv2
import numpy as np


resim=cv2.imread("C:/Users/Fatih/Desktop/New folder/ata.png")
resim1=cv2.imread("C:/Users/Fatih/Desktop/New folder/ata2.png")


toplam=cv2.add(resim, resim1)
agırlıklıtoplam=cv2.addWeighted(resim, 0.7, resim1, 0.3, 0)



cv2.imshow("ataturk", resim)
cv2.imshow("atrk",resim1)
cv2.imshow("toplam resim", toplam)
cv2.imshow("agırlıklıtoplam",agırlıklıtoplam)


cv2.waitKey(0)
cv2.destroyAllWindows()