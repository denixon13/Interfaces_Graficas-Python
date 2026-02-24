from tkinter import *
from tkinter import messagebox

root = Tk()

def infoAdicional():
    messagebox.showinfo("Procesador de Juan", "Procesador de textos 2018")

def avisoLicencia():
    messagebox.showwarning("Licencia", "producto bajo licencia GNU")

def opcionSalir():
    #valor = messagebox.askquestion("Salir", "Deseas salir de la aplicacion")
    valor = messagebox.askokcancel("Salir", "Deseas salir de la aplicacion")

    if valor==True:
        root.destroy()

def cerrarDocumento():
    valor = messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento Bloqueado")

    if valor==True:
        root.destroy()

barraMenu = Menu(root)
root.config(menu=barraMenu, width=300,height=300 )

archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=opcionSalir)


edicionMenu = Menu(barraMenu, tearoff=0)
edicionMenu.add_command(label="Copiar")
edicionMenu.add_command(label="Cortar")
edicionMenu.add_command(label="Pegar")


toolsMenu = Menu(barraMenu, tearoff=0)

helpMenu = Menu(barraMenu, tearoff=0)
helpMenu.add_command(label="Licencia", command=avisoLicencia)
helpMenu.add_command(label="Acerca de..", command=infoAdicional)

barraMenu.add_cascade(label="Archivo", menu= archivoMenu)
barraMenu.add_cascade(label="Edicion", menu= edicionMenu)
barraMenu.add_cascade(label="Tools", menu= toolsMenu)
barraMenu.add_cascade(label="Help", menu= helpMenu)

root.mainloop()