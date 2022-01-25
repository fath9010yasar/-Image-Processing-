# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 13:02:33 2021

@author: Fatih
"""

import cv2
import numpy as np


resim=cv2.imread("C:/Users/Fatih/Desktop/New folder/ata.png")


resimgri=cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)


cv2.imshow("ataturk", resim)
cv2.imshow("atatrk",resimgri)



cv2.waitKey(0)
cv2.destroyAllWindows()
