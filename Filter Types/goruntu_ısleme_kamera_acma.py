# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 13:37:17 2021

@author: Fatih
"""

import cv2
import numpy as np

kamera=cv2.VideoCapture(0)

while True:
    ret,goruntu=kamera.read()
    
    cv2.imshow("fatih", goruntu)
    
    if cv2.waitKey(30) & 0xFF ==ord("q"):
        break
    
    
kamera.release()


cv2.destroyAllWindows()
