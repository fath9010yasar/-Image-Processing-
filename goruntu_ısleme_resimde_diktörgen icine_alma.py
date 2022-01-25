# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 10:46:46 2021

@author: Fatih
"""

import cv2
import numpy as np


resim=cv2.imread("C:/Users/Fatih/Desktop/New folder/ata.png")


cv2.rectangle(resim, (90, 100),(200,50),[0,0,255],1)


cv2.imshow("ataturk", resim)



cv2.waitKey(0)
cv2.destroyAllWindows()
