import tkinter  
from PIL import ImageTk, Image  

root = tkinter.Tk()  

canvas = tkinter.Canvas(root, width = 500, height = 250)  
canvas.pack() 

img = ImageTk.PhotoImage(Image.open("cars.jpg"))

root.mainloop()
