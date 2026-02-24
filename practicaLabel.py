from tkinter import *

root = Tk()

miFrame = Frame(root, width=500, height= 400)

miFrame.pack()

#miImagen = PhotoImage(file="carrito.png")


miLabel = Label(miFrame, text="Hola Alumnos de Python")
miLabel.place(x=100, y=200)
Label(miFrame, text="Hola Alumnos de Python", fg="red", font=("comic Sans MS", 18 )).place(x=100, y=200)
#Label(miFrame, image=miImagen). place(x=100, y=200)

root.mainloop()