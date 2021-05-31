from tkinter import *
from PIL import ImageTk, Image
import cv2

def ImportImage():
    pass

def CreateForm():
    window = Tk()
    window.geometry("918x610")
    window.resizable(0, 0)
    #Create image box

    canvas = Canvas(window, width = 700, height = 450)      
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open("CS231/img/green_cat.jpg"))  
    img = image.resize((250, 250), Image.ANTIALIAS) 
    canvas.create_image(20,20, anchor=NW, image=img) 

    #Configure Import button

    import_button = Button(window,text="Import image")
    import_button.config(command=ImportImage)
    import_button.config(height = 2,width=15)
    import_button.place(x=100,y=500)
    #Configure Change Background button
    
    Change_background_button = Button(window,text="Change Background")
    Change_background_button.config(command=ImportImage)
    Change_background_button.config(height = 2,width=15)
    Change_background_button.place(x=400,y=500)

    #Configure Import Background

    import_background_button = Button(window,text="Import Background")
    import_background_button.config(command=ImportImage)
    import_background_button.config(height = 2,width=15)
    import_background_button.place(x=700,y=500)

    window.mainloop()

def Import_image():
    pass

CreateForm()