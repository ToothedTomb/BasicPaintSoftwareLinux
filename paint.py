from cProfile import label
from tkinter import *
from tkinter.colorchooser import askcolor
import tkinter.messagebox


class Paint(object):

    DEFAULT_PEN_SIZE = 100.0
    DEFAULT_COLOR = 'purple'

    def __init__(self):
        self.root = Tk()
        self.root.resizable(0,0)
        self.root.configure(bg='pink')
        self.root.title("Basic Paint Software 1.0. (BETA)") 
        self.root.tk.call('wm', 'iconphoto', self.root._w, tkinter.PhotoImage(file='paint.png'))

        self.color_button = Button(self.root, text='Change the color', font=("Ubuntu", 23, "bold"),bg="#3b8ee3",border=(1),activebackground="#20b58b", command=self.choose_color)
        self.color_button.grid(row=0, column=0)
        self.label = Label(self.root, text='Change The Size:',bg="pink",font=("ubuntu",23))
        self.label.grid(row=0,column=1)
        self.choose_size_button = Scale(self.root, from_=1, to=100, font=("Ubuntu", 30, "bold"),bg="#3b8ee3",border=(1),activebackground="#20b58b", orient=HORIZONTAL)
        self.choose_size_button.grid(row=0, column=2)
        self.color_button = Button(self.root, text='Save image', font=("Ubuntu", 23, "bold"),bg="#3b8ee3",border=(1),activebackground="#20b58b", command=self.saveimage)
        self.color_button.grid(row=0, column=3)

        self.c = Canvas(self.root, bg='white', width=1024, height=700)
        self.c.grid(row=1, columnspan=5)

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
        tkinter.messagebox.showinfo("Coming out soon.",  "This is still being worked on but when done. I will update this software. For now you can just take a screenshot. ;)")



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