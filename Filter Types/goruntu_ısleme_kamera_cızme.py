# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 14:06:17 2021

@author: Fatih
"""

import cv2
import numpy as np

kamera=cv2.VideoCapture(0)

while True:
    ret,goruntu=kamera.read()
    
    cv2.rectangle(goruntu, (100,100), (200,200), (255,0,0),2)
    
    cv2.line(goruntu, (0,0), (100,100), (0,0,255),1)
    
    cv2.circle(goruntu, (150,150), 50, (0,255,0),3)
    
    cv2.putText(goruntu, "fatih yasarq", (220,220), cv2.FONT_HERSHEY_COMPLEX, 1, (200,0,0),1)
    
    cv2.imshow("fatih", goruntu)
    
    if cv2.waitKey(25) & 0xFF ==ord("q"):
        break
    
    
kamera.release()





cv2.destroyAllWindows()
