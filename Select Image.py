from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


class SelectImage(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        w, h = 650, 650
        master.minsize(width=w, height=h)
        master.maxsize(width=w, height=h)
        self.pack()

        self.file = Button(self, text='Browse', command=self.select)
        self.choose = Label(self, text="Choose file").pack()

        self.file = Button(self, text='Browse', command=self.select)
        self.file = Button(self, text='Browse', command=self.select)
        self.file = Button(self, text='Browse', command=self.select)


        # self.image = PhotoImage("img1.jpg")
        # self.label = Label(image=self.image)
        self.label = Label(image=None)

        self.file.pack()
        self.label.pack()

    def select(self):
        ifile = filedialog.askopenfile(parent=self, mode='rb', title='Choose a file')
        path = Image.open(ifile)

        self.image2 = ImageTk.PhotoImage(path)
        self.label.configure(image=self.image2)
        self.label.image = self.image2


root = Tk()
app = SelectImage(master=root)
app.mainloop()
