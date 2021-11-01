import tkinter
from PIL import ImageTk, Image
import os

# creating main window
root = tkinter.Tk()

#loading the image
img = ImageTk.PhotoImage(Image.open("cars.jpg"))
