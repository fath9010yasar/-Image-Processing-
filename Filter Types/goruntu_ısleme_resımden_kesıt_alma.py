# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 23:00:31 2021

@author: Fatih
"""

import cv2
import numpy as np

resim=cv2.imread("C:/Users/Fatih/Desktop/New folder/ata.png")

kesit=resim[50:150,200:300]

resim[0:100,0:100]=kesit

resim[ : ,: ,1]=150
kesit[ : ,: ,0]=255
resim[100:150,160:200]=(0,150,255)



cv2.imshow("kesit alanı", kesit)
cv2.imshow("ataturk", resim)


cv2.waitKey(0)
cv2.destroyAllWindows()