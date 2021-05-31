import cv2
import numpy as np
from tkinter import *

cap = []

back_ground = []

cap = cv2.imread("CS231/img/green_cat.jpg")

back_ground= cv2.imread("CS231/img/back_ground.jpg")

if back_ground.shape != cap.shape:
    back_ground = cv2.resize(back_ground,(cap.shape[1],cap.shape[0]))

hsv = cv2.cvtColor(cap,cv2.COLOR_BGR2HSV)

lower_green = np.array([33,123,0])
green = np.array([141,255,255])

mask = cv2.inRange(hsv,lower_green,green)
mask_inv = cv2.bitwise_not(mask)

bg = cv2.bitwise_and(cap,back_ground, mask = mask)
fg = cv2.bitwise_and(cap,cap, mask = mask_inv)

fg = np.where(fg == 0,back_ground,fg)

cv2.imshow("frame",cap)
cv2.imshow("fg",fg)

cv2.waitKey(0)

cv2.destroyAllWindows()

