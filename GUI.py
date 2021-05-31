from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import numpy as np
import cv2

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
    if filename != "":
        showinfo(
            title='Import background',
            message="Import background succeed"
        )
    else:
        showinfo(
            title='Error!',
            message="Please import again!"
        )

    filename = filename.replace("/","\\")
    back_ground = cv2.imread(filename)
    back_ground = cv2.resize(back_ground,(700,450))
    back_ground = cv2.cvtColor(back_ground,cv2.COLOR_BGR2RGB)

def ImportImage(canvas):    
    #import image
    global img
    global images
    filetypes = (
        ('jpg files', '*.jpg'),
        ("png files", "*.png"),
    )
    
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    if filename != "":
        showinfo(
            title='Import image',
            message="Import image succeed"
        )

    else:
        showinfo(
            title='Error!',
            message="Please import again!"
        )
        return

    filename = filename.replace("/","\\")
    images = cv2.imread(filename)
    images = cv2.resize(images, (700, 450))
    images = cv2.cvtColor(images,cv2.COLOR_BGR2RGB)
    img = ImageTk.PhotoImage(image=Image.fromarray(images))      
    canvas.create_image(50,50, anchor=NW, image=img) 

def Change_Background(canvas):
    global images
    global back_ground  
    global fg
    global img

    if images == []:
        (showinfo(
        title='Error',
        message="Please import your image"))
        return

    if back_ground == []:
        (showinfo(
        title='Error',
        message="Please import your background"))
        return

    #Thay background
    hsv = cv2.cvtColor(images,cv2.COLOR_RGB2HSV)
    lower_green = np.array([54,123,40])
    green = np.array([66,255,255])
    mask = cv2.inRange(hsv,lower_green,green)
    mask = cv2.dilate(mask, None)
    mask_inv = cv2.bitwise_not(mask)
    fg = cv2.bitwise_and(images,images, mask = mask_inv)
    fg = np.where(fg == 0,back_ground,fg)
    img = ImageTk.PhotoImage(image=Image.fromarray(fg))
    canvas.create_image(50,50, anchor=  NW, image=img) 


def CreateForm():

    window = Tk()
    window.geometry("918x610")
    window.resizable(0, 0)
    canvas = Canvas(window, width = 700, height = 450)      
    canvas.pack()
    #Configure Import button
    import_button = Button(window,text="Import Picture",bg='black', fg='white')
    import_button.config(command= lambda: ImportImage(canvas))
    import_button.config(height = 2,width=15)
    import_button.place(x=100,y=500)
    #Configure Change Background button
    Change_background_button = Button(window,text="Change Background",bg='black', fg='white')
    Change_background_button.config(command=lambda: Change_Background(canvas))
    Change_background_button.config(height = 2,width=15)
    Change_background_button.place(x=400,y=500)
    #Configure Import Background
    import_background_button = Button(window,text="Import Background",bg='black', fg='white')
    import_background_button.config(command=ImportBackground)
    import_background_button.config(height = 2,width=15)
    import_background_button.place(x=700,y=500)

    window.mainloop()

    

img = []
back_ground = []
images = []
fg = []

CreateForm()