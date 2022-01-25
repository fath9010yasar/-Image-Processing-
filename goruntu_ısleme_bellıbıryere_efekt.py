# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 22:36:32 2021

@author: Fatih
"""

import cv2
import numpy as np


resim=cv2.imread("C:/Users/Fatih/Desktop/New folder/ata.png")


resim[100:150,150:300,0]=255
resim[100:150,150:300,1]=200







cv2.imshow("ataturk", resim)






cv2.waitKey(0)
cv2.destroyAllWindows()
