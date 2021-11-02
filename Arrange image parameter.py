import tkinter  
from PIL import ImageTk, Image  
root = tkinter.Tk()  


canvas = tkinter.Canvas(root, width = 500, height = 250)
canvas.pack() 

img = ImageTk.PhotoImage(Image.open("car.jpg"))  


canvas.create_image(135, 20, anchor = NW, image = img) 
