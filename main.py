from picamera import PiCamera
from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
import numpy as np
import cv2
import RPi.GPIO as GPIO
import time
import serial

lcd = LCD()
camera = PiCamera()
camera.resolution = (720,480)
camera.capture(‘/home/pi/Desktop/image.jpg’)
img2 = cv2.imread(‘image.jpg’,1)
hsv_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV);

min_mau_r = np.array([119,0,0]) #red
max_mau_r = np.array([255,60,80])
min_mau_g = np.array([0,80,0]) #green
max_mau_g = np.array([60,255,70])
min_mau_b = np.array([0,0,40]) #blue
max_mau_b = np.array([80,70,255])

mask_r = cv2.inRange(hsv_img2, min_mau_r, max_mau_r);
mask_g = cv2.inRange(hsv_img2, min_mau_g, max_mau_g);
mask_b = cv2.inRange(hsv_img2, min_mau_b, max_mau_b);
final_r = cv2.bitwise_and(img2, img2,mask = mask_r);
final_g = cv2.bitwise_and(img2, img2,mask = mask_g);
final_b = cv2.bitwise_and(img2, img2,mask = mask_b);

if np.any(final_r):
    lcd.text("Red", 1)
    time.sleep(3)
elif np.any(final_g):
    lcd.text("Green", 1)
    time.sleep(3)
elif np.any(final_b):
    lcd.text("Blue", 1)
    time.sleep(3)
else: #ko phai red, green, blue
    lcd.text("No RGB", 1)
    cv2.imshow(“anh_original”, img2); #anh goc
    time.sleep(3)

cv2.waitKey(0);