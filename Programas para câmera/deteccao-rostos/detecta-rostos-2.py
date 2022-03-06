from PIL import ImageGrab
import numpy as np
import cv2
import time

cascade_rostos = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

tela = np.array(ImageGrab.grab(bbox=(0,0,600,600)))
cinza = cv2.cvtColor(tela, cv2.COLOR_BGR2GRAY)
rostos = cascade_rostos.detectMultiScale(cinza)

for(x, y, h, w) in rostos:
    tela = cv2.rectangle(tela,(x,y),(x+h,y+w),(255,0,0),2)

cv2.imshow('tela', cv2.cvtColor(tela, cv2.COLOR_BGR2RGB))
