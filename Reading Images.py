import tkinter
from PIL import ImageTk, Image
import os

# creating main window
root = tkinter.Tk()

#load
img = ImageTk.PhotoImage(Image.open("cars.jpg"))

# read
panel = tkinter.Label(root, image = img)

# setting the application
panel.pack(side = "top", fill = "both", expand = "yes")

root.mainloop()
