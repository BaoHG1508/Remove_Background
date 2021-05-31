from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from functools import partial
import numpy as np
import cv2

img = []
back_ground = []
image = []

def ImportBackground():
    #import back_ground
    global back_ground
    filetypes = (
        ('jpg files', '*.jpg'),
        ("png files", "*.png"),
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    showinfo(
        title='Import Background thành công',
        message=filename
    )
    filename = filename.replace("/","\\")
    back_ground = cv2.imread(filename)


def ImportImage(canvas):
    #import image
    global img
    global image
    filetypes = (
        ('jpg files', '*.jpg'),
        ("png files", "*.png"),
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    showinfo(
        title='Selected File',
        message=filename
    )
    #Resize anh to lai cho fit vao 700 x 450 canvas
    filename = filename.replace("/","\\")
    images = cv2.imread(filename)
    images = cv2.resize(images, (700, 450))
    img = ImageTk.PhotoImage(image=Image.fromarray(images))      
    canvas.create_image(50,50, anchor=NW, image=img) 

def CreateForm():

    window = Tk()
    window.geometry("918x610")
    window.resizable(0, 0)
    canvas = Canvas(window, width = 700, height = 450)      
    canvas.pack()
    #Configure Import button
    import_button = Button(window,text="Import image")
    import_button.config(command= lambda: ImportImage(canvas))
    import_button.config(height = 2,width=15)
    import_button.place(x=100,y=500)
    #Configure Change Background button
    Change_background_button = Button(window,text="Change Background")
    Change_background_button.config(command=lambda: ImportImage(window))
    Change_background_button.config(height = 2,width=15)
    Change_background_button.place(x=400,y=500)
    #Configure Import Background
    import_background_button = Button(window,text="Import Background")
    import_background_button.config(command=ImportBackground)
    import_background_button.config(height = 2,width=15)
    import_background_button.place(x=700,y=500)

    window.mainloop()

    

CreateForm()