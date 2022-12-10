#Importaciones
from tkinter import *
import os
from PIL import ImageTk,Image

# Directorio de imágenes principal

# Directorio de imágenes
carpeta_imagenes = os.path.join("img")


#Creación de la ventana principal
root = Tk()
#Título de la ventana
root.title("Curso de Tkinter de Programación Fácil")
#Icono de la ventana
#root.iconbitmap(os.path.join(carpeta_imagenes, "icono.ico"))

#Carga de imagen
nieve = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "escudo.jpeg")))
etiqueta = Label(image=nieve)
etiqueta.pack()

#Bucle de ejecución
root.mainloop()