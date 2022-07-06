from cProfile import label
from tkinter import *
from tkinter.colorchooser import askcolor
import tkinter.messagebox
from tkinter import filedialog
import tkinter.filedialog
from typing_extensions import Self
import tkinter as ttk 
import sys
from tkinter import Toplevel
from PIL import Image
def on_closing():
    root = tkinter.Toplevel()  
    root.resizable(0,0)
    root.title("Confirm to exit the software:")
    root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='paint.png'))


    labelTitle = ttk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="Confirm to exit the software:")
    label = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="Are you sure you want to leave this software?")

    labelTitle.pack(side="top",fill="x",pady=1)
    label.pack(side="top", fill="x", pady=2)
    B1 = tkinter.Button(root, text="Yes",font=("ubuntu",28),bg="#3b8ee3",border=(1),activebackground="#20b58b", command = root.quit)

    B2 = tkinter.Button(root, text="No",font=("ubuntu",28),bg="#3b8ee3",border=(1),activebackground="#20b58b", command = root.destroy)
    B1.pack(side=tkinter.LEFT, anchor=CENTER)
    B2.pack(side=tkinter.RIGHT, anchor=CENTER)
def MadeBy():
    root = tkinter.Toplevel()  
    root.resizable(0,0)
    root.title("Who made this software?")
    root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='paint.png'))


    labelTitle = ttk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="Who made this software?")
    label = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="Jonathan Steadman has made this software.")
    labelTitle.pack(side="top",fill="x",pady=1)
    label.pack(side="top", fill="x", pady=2)
    B1 = tkinter.Button(root, text="Exit",font=("ubuntu",28),bg="#3b8ee3",border=(1),activebackground="#20b58b", command = root.destroy)
    B1.pack()
def WhatIsThis():
    root = tkinter.Toplevel()  
    root.resizable(0,0)
    root.title("What is this software?")
    root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='paint.png'))


    labelTitle = ttk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="What is this software?")
    label = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="This software is a free and open source basic paint software for FreeBSD and Linux.")

    labelTitle.pack(side="top",fill="x",pady=1)
    label.pack(side="top", fill="x", pady=2)


    B1 = tkinter.Button(root, text="Exit",font=("ubuntu",28),bg="#3b8ee3",border=(1),activebackground="#20b58b", command = root.destroy)
    B1.pack()    
class Paint(object):

    DEFAULT_PEN_SIZE = 60.0
    DEFAULT_COLOR = 'green'



    def __init__(self):
        self.root = Tk()
        self.root.resizable(0,0)
        self.root.configure(bg='pink')
        self.root.title("Basic Paint Software 3.0!") 
        self.root.tk.call('wm', 'iconphoto', self.root._w, tkinter.PhotoImage(file='paint.png'))
        my_menu= Menu(self.root)
        self.root.config(menu=my_menu)
        file_menu= Menu(my_menu,background="pink",activebackground="#20b58b")
        my_menu.add_cascade(label="About:",font=("Ubuntu",18),activebackground="#20b58b", menu=file_menu)
        file_menu.add_command(label="Who made this Software?",font=("Ubuntu",18),activebackground="#20b58b",background="pink",command=MadeBy) 
        file_menu.add_command(label="What is this software?",font=("Ubuntu",18),activebackground="#20b58b",background="pink",command=WhatIsThis) 
        self.color_button = Button(self.root, text='Change the color', font=("Ubuntu", 23, "bold"),bg="#3b8ee3",border=(1),activebackground="#20b58b", command=self.choose_color)
        self.color_button.grid(row=0, column=0)
        self.label = Label(self.root, text='Change The Size:',bg="pink",font=("ubuntu",23))
        self.label.grid(row=0,column=1)
        self.choose_size_button = Scale(self.root, from_=1, to=100, font=("Ubuntu", 30, "bold"),bg="#3b8ee3",border=(1),activebackground="#20b58b", orient=HORIZONTAL)
        self.choose_size_button.grid(row=0, column=2)
        self.color_button = Button(self.root, text='Save image', font=("Ubuntu", 23, "bold"),bg="#3b8ee3",border=(1),activebackground="#20b58b", command=self.saveimage)
        self.color_button.grid(row=0, column=3)
        self.c = Canvas(self.root, bg='white', width=1224, height=780)
        self.c.grid(row=1, columnspan=5)
        self.root.protocol("WM_DELETE_WINDOW", on_closing)

        self.setup()
        self.root.mainloop()

        
    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def saveimage(self):
        
        self.c.update()
        self.c.postscript(file="YourDrawing.ps", colormode='color')
        im = Image.open("YourDrawing.ps")
        rgb_im = im.convert("RGB")
        rgb_im.save("YourDrawing.jpg")
    
        
 
    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]



    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None





if __name__ == '__main__':
    Paint()
