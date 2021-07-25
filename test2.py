from tkinter import*
from fpdf import FPDF
import tkinter as tk
from tkinter import messagebox
import cv2
import pytesseract
from PIL import Image,ImageTk
import webbrowser
from tkinter.filedialog import askopenfilename,asksaveasfilename
import sys

r=tk.Tk()
r.geometry('690x600')
r.resizable(1, 1)
r.config(bg='lavender')
r.title('IMPV')
icon=ImageTk.PhotoImage(Image.open('S:/Codes/Python/PP/icon.jpg'))
r.iconphoto(False,icon)

def BB():
 BB.im=askopenfilename(filetypes=(('Images','*.png;*.jpg;*.jpeg;*.bmp;*.tif;*.jfif;*.tiff'),('All Files','*.*')) )
 if BB.im: 
  BB.imp=BB.im
  photo = Image.open(BB.im)
  photo=photo.resize((305,305),Image.ANTIALIAS)
  render = ImageTk.PhotoImage(photo)  
  C.create_image(0,0, anchor=NW, image=render)    
  mainloop()
 if not BB.im:
   BB.im=BB.imp 

def H():
  if BB.im:    
    H.img = cv2.imread(BB.im)
    h, w, c = H.img.shape
    boxes = pytesseract.image_to_boxes(H.img) 
    for b in boxes.splitlines():
     b = b.split(' ')
     H.img = cv2.rectangle(H.img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (150, 200, 200), 2)
    H.img1=Image.fromarray(H.img)
    H.img=H.img1.resize((305,305),Image.ANTIALIAS)
    H.img = ImageTk.PhotoImage(H.img)    
    C1.create_image(0,0, anchor=NW, image= H.img)    
    mainloop()

def CI():
  BB.im=0
  C.delete('all') 
  
def CI1():
  C1.delete('all') 
  H.img=0 

H.img=0
def SaI(): 
 if H.img:
  FF=[('Image','.jpg')]
  savi=asksaveasfilename(defaultextension=".jpg",filetypes=FF)  
  H.img1.save(savi)

BB.im=0
def Pr(): 
  if BB.im:
   text = pytesseract.image_to_string(BB.im,lang='eng',config='--oem 1')
   ResultTextBox.insert(END,text)
   ResultTextBox.delete('end-2c','end')

def Cl():
  ResultTextBox.delete('1.0',END)

def SS():
  webbrowser.register('chrome',	None,	webbrowser.BackgroundBrowser("C:/Program Files/Google/Chrome/Application/chrome.exe"))
  Sea = ResultTextBox.get('1.0','end-1c')
  if Sea:
   webbrowser.open('https://www.google.com.tr/search?q={}'.format(Sea))

def PDF():
  PdfV = ResultTextBox.get('1.0','end-1c')
  if PdfV:
   pdf = FPDF()
   pdf.add_page()
   pdf.set_font("Arial", size = 20)
   pdf.multi_cell(200, 10, txt =PdfV)
   FF=[('PDF','.pdf')]
   save=asksaveasfilename(defaultextension=".pdf",filetypes=FF)  
   pdf.output(save)

def TXT():
  TxtV = ResultTextBox.get('1.0','end-1c')
  if TxtV:
   FF=[('Txt','.txt')]
   save=asksaveasfilename(defaultextension=".txt",filetypes=FF) 
   file = open(save, 'w')
   file.write(TxtV)
   file.close()

def Ext():
  Warn = ResultTextBox.get('1.0','end-1c')
  if Warn:
   t=messagebox.askyesnocancel("Save?","Do You Want to Save Extracted Data?")
   if t:
     TXT() 
     sys.exit()
   elif t is False:
     sys.exit()
  else:
    sys.exit()

C=Canvas(r,width=300,height=300,bg='seashell')
C.pack(side=LEFT,padx=30,pady=0)
C1=Canvas(r,width=300,height=300,bg='seashell')
C1.pack(side=RIGHT,padx=30,pady=0)
B= tk.Button(r, text="Select Image" ,command = BB,bg='snow3')
B.pack(padx=40,pady=305)

r.mainloop()