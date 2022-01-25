# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 13:52:08 2021

@author: Fatih
"""

import cv2
import numpy as np

resim=np.zeros((300,300,3),dtype="uint8")

cv2.line(resim,(0,0),(100,100),(20,60,255),2)
cv2.circle(resim, (150,150), (25), (0,255,0),3)
cv2.putText(resim, "fatih yasar", (100,200), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0))



cv2.imshow("cizgi", resim)



cv2.waitKey(0)

cv2.destroyAllWindows()
