import cv2
import numpy as np

frame = cv2.imread("CS231/img/green_cat.jpg")
frame = cv2.resize(frame,(500,500))
back_ground= cv2.imread("CS231/img/back_ground.jpg")


if back_ground.shape != frame.shape:
    back_ground = cv2.resize(back_ground,(frame.shape[1],frame.shape[0]))

hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
lower_green = np.array([42, 180, 39])
green = np.array([77,255,255])
mask = cv2.inRange(hsv,lower_green,green)
mask_inv = cv2.bitwise_not(mask)


cv2.imshow("mask_inv", mask_inv)
cv2.imshow("mask", mask)
cv2.imshow("result", mask+mask_inv)

cv2.waitKey(0)
