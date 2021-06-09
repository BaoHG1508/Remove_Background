import tkinter as tk, threading
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from imageio.core.util import image_as_uint
import numpy as np
import cv2
import imageio

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
        return

    filename = filename.replace("/","\\")
    back_ground = cv2.imread(filename)
    back_ground = cv2.resize(back_ground,(700,450))
    back_ground = cv2.cvtColor(back_ground,cv2.COLOR_BGR2RGB)

def ImportImage(label,import_video):    
    #import image
    global img
    global images
    global video
    
    filetypes = (
        ('jpg files', '*.jpg'),
        ("png files", "*.png"),
        ("mp4", "*.mp4")
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
        video = []
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
    label.config(image=img)
    label.image = img

def Change_Background(label,import_button,import_video,window):
    global images
    global back_ground  
    global fg
    global img
    global video
    global thread
    global stop
    stop = False
    if images == [] and video == []:
        (showinfo(
        title='Error',
        message="Please import your image"))
        return

    if images == [] and video != "":
        #Stop video
        Stop_button = Button(window,text="Stop",bg='black', fg='white')
        Stop_button.config(height = 2,width=15)
        Stop_button.config(command=lambda: StopVideo(import_video))
        Stop_button.place(x=400,y=400)
        import_video['state'] = "disable"
    if back_ground == []:
        (showinfo(
        title='Error',
        message="Please import your background"))
        return

    #Thay background
    if images != []:
        hsv = cv2.cvtColor(images,cv2.COLOR_BGR2HSV)
        lower_green = np.array([42, 180, 39])
        green = np.array([77,255,255])
        mask = cv2.inRange(hsv,lower_green,green)
        mask_inv = cv2.bitwise_not(mask)
        mask = cv2.cvtColor(mask,cv2.COLOR_GRAY2RGB)
        mask = np.where(mask == 0,mask,back_ground)
        mask_inv = cv2.cvtColor(mask_inv,cv2.COLOR_GRAY2RGB)
        mask_inv = np.where(mask_inv == 0,mask_inv,images)
        img = ImageTk.PhotoImage(image=Image.fromarray(mask_inv+mask))
        label.config(image=img)
        label.image = img
    elif video != []:
        thread = threading.Thread(target=stream_bg_changed, args=(label,Stop_button,))
        thread.daemon = 1
        thread.start()

def StopVideo(import_video):
    global stop
    import_video['state'] = "normal"
    stop = True


def stream_bg_changed(label,StopButton):
    global back_ground
    back_ground = cv2.resize(back_ground,(700,450))
    for image in video.iter_data():
        image = cv2.resize(image,(700,450))
        hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        lower_green = np.array([42, 180, 39])
        green = np.array([77,255,255])
        mask = cv2.inRange(hsv,lower_green,green)
        mask_inv = cv2.bitwise_not(mask)
        mask = cv2.cvtColor(mask,cv2.COLOR_GRAY2RGB)
        mask = np.where(mask == 0,mask,back_ground)
        mask_inv = cv2.cvtColor(mask_inv,cv2.COLOR_GRAY2RGB)
        mask_inv = np.where(mask_inv == 0,mask_inv,image)
        frame_image = ImageTk.PhotoImage(Image.fromarray(mask_inv+mask))
        label.config(image=frame_image)
        label.image = frame_image
        if stop == True:
            break
    if stop == False:
        stream_bg_changed(label)
    StopButton.destroy()
    
def ImportVideo(my_label,import_button):
    global video
    global thread
    global img
    global images
    filetypes = (
        ('mp4 files', '*.mp4'),
    )
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    if filename != "":
        showinfo(
            title='Import video',
            message="Import video succeed"
        )
        images = []
    else:
        showinfo(
            title='Error!',
            message="Please import again!"
        )
        return
    
    filename = filename.replace("/","\\")
    video = imageio.get_reader(filename)
    for imagez in video.iter_data():
        imagez = np.array(imagez,dtype=np.uint8)
        imagez = cv2.resize(imagez, (700, 450))
        img = ImageTk.PhotoImage(image=Image.fromarray(imagez))      
        my_label.config(image=img)
        my_label.image = img
        return
     
def CreateForm():

    window = Tk()
    window.geometry("918x610")
    window.resizable(0, 0)
    my_label = tk.Label(window, width = 700, height = 450)
    my_label.pack()
    
    #Configure Import button
    import_button = Button(window,text="Import Picture",bg='black', fg='white')
    import_button.config(command= lambda: ImportImage(my_label,import_video))
    import_button.config(height = 2,width=15)
    import_button.place(x=100,y=500)
    #Configure Change Background button
    Change_background_button = Button(window,text="Change Background",bg='black', fg='white')
    Change_background_button.config(command=lambda: Change_Background(my_label,import_button,import_video,window))
    Change_background_button.config(height = 2,width=15)
    Change_background_button.place(x=300,y=500)
    #Configure Import Background
    import_background_button = Button(window,text="Import Background",bg='black', fg='white')
    import_background_button.config(command=ImportBackground)
    import_background_button.config(height = 2,width=15)
    import_background_button.place(x=500,y=500)
    #Configure Import Video
    import_video = Button(window,text="Import Video",bg='black', fg='white')
    import_video.config(command=lambda: ImportVideo(my_label,import_button))
    import_video.config(height = 2,width=15)
    import_video.place(x=700,y=500)
    
    #Play video button
    window.mainloop()

    

img = []
back_ground = []
images = []
fg = []
video = []
thread = []
stop = False
CreateForm()