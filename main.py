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
r.title('IPMV Project')
r.resizable(0,0)
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

BB.im=0
def Pr(): 
  if BB.im:
   img=im2= cv2.imread(BB.im)
   Pr.gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   
   Pr.th = cv2.adaptiveThreshold(Pr.gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2) 
     
   kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3)) 
   dilated = cv2.dilate(Pr.th, kernel, iterations=9) 
   contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

   for cnt in contours:
     [x, y, w, h] = cv2.boundingRect(cnt)         
     cv2.rectangle(Pr.gray, (x, y), (x + w, y + h), (255, 0, 255), 1)
     Pr.cropped = Pr.gray[y:y + h, x:x + w] 

Pr.cropped=0
def Ex():
   Pr()  
   Pr.cropped=BB.im   
   text = pytesseract.image_to_string(Pr.cropped,lang='eng',config='--oem 1')
   ResultTextBox.insert(END,text)
   ResultTextBox.delete('end-2c','end')

Pr.th=Pr.gray=0
def thr():
 Pr()
 gr.img1=H.img=0
 if BB.im:
  thr.img1=Image.fromarray(Pr.th)
  img=thr.img1.resize((305,305),Image.ANTIALIAS)
  img = ImageTk.PhotoImage(img)    
  C1.create_image(0,0, anchor=NW, image= img)    
  mainloop()

def gr():
 Pr()
 H.img=thr.img1=0
 if BB.im:
  gr.img1=Image.fromarray(Pr.gray)
  img=gr.img1.resize((305,305),Image.ANTIALIAS)
  img = ImageTk.PhotoImage(img)    
  C1.create_image(0,0, anchor=NW, image= img)    
  mainloop()

def H():
  gr.img1=thr.img1=0
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
  gr.img1=0
  thr.img1=0

H.img=0
gr.img1=0
thr.img1=0

def SaI(): 
 if H.img:
  FF=[('Image','.jpg')]
  savi=asksaveasfilename(defaultextension=".jpg",filetypes=FF)    
  H.img1.save(savi)
 if gr.img1:
  FF=[('Image','.jpg')]
  savi=asksaveasfilename(defaultextension=".jpg",filetypes=FF)  
  gr.img1.save(savi)
 if thr.img1:
  FF=[('Image','.jpg')]
  savi=asksaveasfilename(defaultextension=".jpg",filetypes=FF)  
  thr.img1.save(savi)

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
C.place(x=30,y=0)
C1=Canvas(r,width=300,height=300,bg='seashell')
C1.place(x=360,y=0)
B= tk.Button(r, text="Gray Image" ,command = gr,bg='snow3')
B.place(x=370,y=305)
B= tk.Button(r, text="Threshold Image" ,command = thr,bg='light pink')
B.place(x=465,y=305)
B= tk.Button(r, text="Select Image" ,command = BB,bg='snow3')
B.place(x=40,y=305)
B= tk.Button(r, text="Clear Image" ,command = CI,bg='light pink')
B.place(x=147,y=305)
B=tk.Button(r ,text='Extract Text',command = Ex,bg='orange')
B.place(x=250,y=305)
B= tk.Button(r, text="Box Text Image" ,command = H ,bg='snow3')
B.place(x=465,y=335)
B= tk.Button(r, text="Clear Image" ,command = CI1,bg='light pink')
B.place(x=370,y=335)
B= tk.Button(r, text="Save Image" ,command = SaI ,bg='orange')
B.place(x=585,y=305)
DataLabel = Label(r,text = "Data From Image :",bg='light sea green')
DataLabel.place(x = 0,y = 350)
ResultTextBox = Text(r,height = 10,width=85,bg='pale green')
ResultTextBox.place(x = 0,y = 370)
B=tk.Button(r,text='Clear Data',command = Cl,bg='powder blue')
B.place(x=35,y=535)
B= tk.Button(r, text="Search On Web" ,command = SS,bg='khaki')
B.place(x=155,y=535)
B= tk.Button(r, text="Convert To PDF" ,command = PDF,bg='powder blue')
B.place(x=295,y=535)
B= tk.Button(r, text="Save As Text" ,command = TXT,bg='khaki')
B.place(x=430,y=535)
B= tk.Button(r, text="Close And Exit" ,command = Ext,bg='powder blue')
B.place(x=560,y=535)
r.mainloop()