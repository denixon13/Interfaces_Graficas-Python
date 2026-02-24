from tkinter import *

root= Tk()

miFrame= Frame(root, width= 1200, height=600)
miFrame.pack()

miNombre=StringVar()

cuadroNombre = Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=0, column=1)
cuadroNombre.config(fg="red", justify="center")

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=1, column=1)

cuadroCorreo = Entry(miFrame)
cuadroCorreo.grid(row=2, column=1)

cuadroPassword = Entry(miFrame)
cuadroPassword.grid(row=3, column=1)
cuadroPassword.config(show="*")

cuadroTexto = Text(miFrame, width=16, height=6)
cuadroTexto.grid(row=4, column=1, padx=10, pady=10)

scrollVert=Scrollbar(miFrame, command=cuadroTexto.yview)
scrollVert.grid(row=4, column=2, sticky="nsew")

cuadroTexto.config(yscrollcommand=scrollVert.set )


nombreLabel= Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

apellidoLabel= Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=1, column=0, sticky="e",padx=10, pady=10)

correoLabel= Label(miFrame, text="Correo:")
correoLabel.grid(row=2, column=0, sticky="e",padx=10, pady=10)

passwordLabel= Label(miFrame, text="Correo:")
passwordLabel.grid(row=3, column=0, sticky="e",padx=10, pady=10)

textoLabel= Label(miFrame, text="Comentarios:")
textoLabel.grid(row=4, column=0, sticky="e",padx=10, pady=10)

def codigoBoton():

    miNombre.set("Deni")

botonEnvio= Button(root, text="Enviar", command=codigoBoton)
botonEnvio.pack()

root.mainloop()
