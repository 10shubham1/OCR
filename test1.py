from tkinter import*
from fpdf import FPDF
import tkinter as tk
from tkinter.filedialog import askopenfilename,asksaveasfilename
import cv2
import pytesseract
from PIL import Image,ImageTk
import webbrowser


r=tk.Tk()
r.geometry('650x600')
r.config(bg='lavender')
r.title('IMPV')
icon=ImageTk.PhotoImage(Image.open('S:/Codes/Python/PP/icon.jpg'))
r.iconphoto(False,icon)

def BB():
  BB.im=askopenfilename(filetypes=(('Images','*.png;*.jpg;*.jpeg;*.bmp;*.tif;*.jfif;*.tiff'),('All Files','*.*')) )
  photo = Image.open(BB.im)
  photo=photo.resize((305,305),Image.ANTIALIAS)
  photo.convert('L')
  render = ImageTk.PhotoImage(photo)
  C.create_image(0,0, anchor=NW, image= render)    
  mainloop()

def Pr(): 
  text = pytesseract.image_to_string(BB.im)
  ResultTextBox.insert(END,text)
  ResultTextBox.delete('end-2c','end')
  
def SS():
  webbrowser.register('chrome',	None,	webbrowser.BackgroundBrowser("C:/Program Files/Google/Chrome/Application/chrome.exe"))
  Sea = ResultTextBox.get('1.0','end-1c')
  if Sea:
   webbrowser.open('https://www.google.com.tr/search?q={}'.format(Sea))
  
def Cl():
  ResultTextBox.delete('1.0',END)

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

PD= tk.Button(r, text="Convert To PDF" ,command = PDF,bg='thistle2')
PD.grid(row=6,column=2,sticky=(E))

P=tk.Button(r ,text='Convert',command = Pr,bg='orange')
P.grid(row=3,column=1)

B= tk.Button(r, text="Select Image" ,command = BB,bg='snow3')
B.grid(row=2,column=1)

S= tk.Button(r, text="Search On Web" ,command = SS,bg='thistle2')
S.grid(row=6,column=2,sticky=(W))
  
Cr=tk.Button(r,text='Clear Data',command = Cl,bg='powder blue')
Cr.grid(row=6,column=1)

C=Canvas(r,width=300,height=300,bg='seashell')
C.grid(row=1,column=1)

DataLabel = Label(r,text = "Data From Image :",bg='light sea green')
DataLabel.grid(row = 4,column=1,sticky=(W))

ResultTextBox = Text(r,height = 10,bg='pale green')
ResultTextBox.grid(row = 5,column = 1,columnspan=2)

r.mainloop()
