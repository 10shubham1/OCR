import cv2
import pytesseract
import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image ,ImageTk
from tkinter import*


r=tk.Tk()

im=askopenfilename(filetypes=(('Images','*.png;*.jpg;*.jpeg;*.bmp;*.tif;*.jfif;*.tiff;*.'),('All Files','*.*')) )
print(im)
imgg=ImageTk.open(im)
im1=tk.PhotoImage(file=im)
img=tk.Label(r,image=im1)
img.pack()



r.mainloop()
