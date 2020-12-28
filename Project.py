import cv2 as cv
import numpy as np
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


class SelectImage(Frame):
    img = None

    def __init__(self, master=None):
        Frame.__init__(self, master)
        w, h = 1920, 1024
        master.minsize(width=w, height=h)
        master.maxsize(width=w, height=h)
        self.pack()

        self.file = Button(self, text='Browse', command=self.select)
        self.choose = Label(self, text="Choose file").pack()
        self.label = Label(image=None)

        self.change_contrast = Button(self, text='Change contrast', command=self.change_contrast)
        self.log_transformation = Button(self, text='Log Transformation', command=self.log_transformation)
        self.negative_transformation = Button(self, text='Negative Transformation',
                                              command=self.negative_transformation)
        self.normalize_equation = Button(self, text='Normalize Equation', command=self.normalize_equation)
        self.reducing_gray_level = Button(self, text='Reducing Gray Level', command=self.reducing_gray_level)
        self.power_low_transformation = Button(self, text='Power Low Transformation',
                                               command=self.power_low_transformation)

        self.file.pack()
        self.label.pack()
        self.change_contrast.pack()
        self.log_transformation.pack()
        self.negative_transformation.pack()
        self.normalize_equation.pack()
        self.power_low_transformation.pack()
        self.reducing_gray_level.pack()

    def select(self):
        ifile = filedialog.askopenfile(parent=self, mode='rb', title='Choose a file')
        self.path = Image.open(ifile).convert('RGB')

        self.image = ImageTk.PhotoImage(self.path)
        self.label.configure(image=self.image)
        self.label.image = self.image
        self.img = np.array(self.path)
        self.img = self.img[:, :, ::-1].copy()

    def change_contrast(self):
        if not np.any(self.img):
            return
        img_after = change_contrast(self.img, 1.5, 10)
        img_after = ImageTk.PhotoImage(Image.fromarray(img_after))
        self.label.configure(image=img_after)
        self.label.image = img_after

    def log_transformation(self):
        if not np.any(self.img):
            return

        img_after = log_transformation(self.img)
        img_after = ImageTk.PhotoImage(Image.fromarray(img_after))
        self.label.configure(image=img_after)
        self.label.image = img_after

    def negative_transformation(self):
        if not np.any(self.img):
            return

        img_after = negative_transformation(self.img)
        img_after = ImageTk.PhotoImage(Image.fromarray(img_after))
        self.label.configure(image=img_after)
        self.label.image = img_after

    def normalize_equation(self):
        if not np.any(self.img):
            return

        img_after = normalize_equation(self.img)
        img_after = ImageTk.PhotoImage(Image.fromarray(img_after))
        self.label.configure(image=img_after)
        self.label.image = img_after

    def power_low_transformation(self):
        if not np.any(self.img):
            return

        img_after = power_low_transformation(self.img)
        img_after = ImageTk.PhotoImage(Image.fromarray(img_after))
        self.label.configure(image=img_after)
        self.label.image = img_after

    def reducing_gray_level(self):
        if not np.any(self.img):
            return

        img_after = reducing_gray_level(self.img)
        img_after = ImageTk.PhotoImage(Image.fromarray(img_after))
        self.label.configure(image=img_after)
        self.label.image = img_after


def change_contrast(img, alpha, beta):
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            for c in range(img.shape[2]):
                img[y, x, c] = np.clip(alpha * img[y, x, c] + beta, 0, 255)
    return img


def log_transformation(img):
    c = 255 / (np.log(1 + np.max(img)))
    log_transformed = c * np.log(1 + img)
    log_transformed = np.array(log_transformed, dtype=np.uint8)
    return log_transformed


def negative_transformation(img):
    height, width, _ = img.shape

    for i in range(0, height - 1):
        for j in range(0, width - 1):
            pixel = img[i, j]

            pixel[0] = 255 - pixel[0]
            pixel[1] = 255 - pixel[1]
            pixel[2] = 255 - pixel[2]

            img[i, j] = pixel
    return img


def normalize_equation(image):
    image_bw = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    clahe = cv.createCLAHE(clipLimit=5)
    final_img = clahe.apply(image_bw) + 30

    _, ordinary_img = cv.threshold(image_bw, 155, 255, cv.THRESH_BINARY)

    return final_img


def power_low_transformation(img):
    for gamma in [0.1, 0.5, 1.2, 2.2]:
        gamma_corrected = np.array(255 * (img / 255) ** gamma, dtype='uint8')

        # cv.imwrite('gamma_transformed'+str(gamma)+'.jpg', gamma_corrected)
    return gamma_corrected


def reducing_gray_level(img):
    width = int(img.shape[0])
    height = int(img.shape[1])

    for i in range(width):
        for j in range(height):
            img[i][j] = img[i][j] * 2;
    return img


root = Tk()
app = SelectImage(master=root)
app.mainloop()
