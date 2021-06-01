import cv2
import numpy as np
from tkinter import *

cap = []

back_ground = []

cap = cv2.VideoCapture("CS231/img/space.mp4")
back_ground= cv2.imread("CS231/img/back_ground.jpg")

while True:
    flag, frame= cap.read()
    if not flag:
        cap = cv2.VideoCapture("CS231/img/space.mp4")
        continue

    if back_ground.shape != frame.shape:
        back_ground = cv2.resize(back_ground,(frame.shape[1],frame.shape[0]))
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_green = np.array([42, 180, 39])
    green = np.array([81,255,255])

    mask = cv2.inRange(hsv,lower_green,green)
    mask_inv = cv2.bitwise_not(mask)

    fg = cv2.bitwise_and(frame,frame, mask = mask_inv)

    fg = np.where(fg == 0,back_ground,fg)
    
    cv2.imshow("fg",fg)
    cv2.waitKey(delay=1)
