# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 10:13:43 2021

@author: Fatih
"""

import cv2
import numpy as np

resim = cv2.imread("C:/Users/Fatih/Desktop/New folder/ata.png")


aynalama=cv2.copyMakeBorder(resim, 70, 70, 70, 100,cv2.BORDER_REFLECT)
uzatma=cv2.copyMakeBorder(resim, 100, 100, 100, 100,cv2.BORDER_REPLICATE)
tekrar=cv2.copyMakeBorder(resim, 100, 50, 50, 100, cv2.BORDER_WRAP)
cerceve=cv2.copyMakeBorder(resim, 30, 50, 50, 30, cv2.BORDER_CONSTANT)
                           
                                                



cv2.imshow("ataturk", aynalama)
cv2.imshow("atatrk", uzatma)
cv2.imshow("ata", tekrar)
cv2.imshow("atam", cerceve)




cv2.waitKey(0)
cv2.destroyAllWindows()