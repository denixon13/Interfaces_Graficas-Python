from tkinter import *

raiz = Tk() #

raiz.title("Ventana de prueba")

# raiz.resizable(True, 2) #redimensionar ventana, ancho y largo

raiz.iconbitmap("pawPatrol.ico") #Icono 

#raiz.geometry("650x350") #Tamaño por defecto

raiz.config(bg="green")

miFrame = Frame()

#miFrame.pack(side="right", anchor="n")
miFrame.pack(fill="y", expand=True) #Se expande

miFrame.config(bg = "red")

miFrame.config(width="650", height="350")

miFrame.config(bd="35")

miFrame.config(relief="solid")

miFrame.config(cursor="hand2")

raiz.mainloop()  #Bucle infinito, o continua ejecucion
