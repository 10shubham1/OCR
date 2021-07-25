import cv2 
from tkinter.filedialog import askopenfilename
import pytesseract 
import numpy as np
from matplotlib import pyplot as plt
img1=askopenfilename(filetypes=(('Images','*.png;*.jpg;*.jpeg;*.bmp;*.tif;*.jfif;*.tiff'),('All Files','*.*')) )
img= cv2.imread(img1,0)
img=cv2.resize(img,(600,600))
cv2.imshow('captcha_result', img) 
cv2.waitKey()
im2=img

#img = cv2.medianBlur(img,5)
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

cv2.imshow('captcha_result', th2) 
cv2.waitKey()
img= cv2.imread(img1)
img=cv2.resize(img,(600,600))

img_final = cv2.imread(img1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('captcha_result', gray) 
cv2.waitKey()
ret, mask = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)
image_final = cv2.bitwise_and(gray, gray, mask=mask)
cv2.imshow('captcha_result', image_final) 
cv2.waitKey()
ret, new_img = cv2.threshold(image_final, 180, 255, cv2.THRESH_BINARY)
cv2.imshow('captcha_result', image_final) 
cv2.waitKey()

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3)) 
dilated = cv2.dilate(th2, kernel, iterations=9) 

contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)



for cnt in contours: 

    [x, y, w, h] = cv2.boundingRect(cnt)   
   
    if w < 35 and h < 35:
            continue   

    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
    cropped = im2[y:y + h, x:x + w]   
    text = pytesseract.image_to_string(cropped) 

cv2.imshow('captcha_result', img) 
cv2.waitKey()
 
print(text)