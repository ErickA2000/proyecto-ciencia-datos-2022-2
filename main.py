from tkinter import *
import os
from PIL import ImageTk, Image
import window_1 as w1

app = Tk()

frame_1 = Frame(app, bg='white')
frame_2 = Frame(app, bg= "#ad3333")

#Ruta de la imagen
carpeta_imagenes = os.path.join("img")
img_uni = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "escudo.jpeg")))
etiqueta = Label(frame_1, image = img_uni)
etiqueta.pack()

def config():
    app.config(bg="#DADADA")
    app.geometry("922x548")
    app.minsize(width=922, height=548)
    app.title("Proyecto de clase ciencia de datos")
    app.resizable(width=False, height=False)

    app.columnconfigure(0 , weight=25)
    app.rowconfigure(0, weight=25)
    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)
    
    frame_1.grid(column=0, row=0, sticky='nsew')
    
    frame_2.grid(column=0, row=1, sticky='nsew')

    frame_1.columnconfigure(0, weight=1)
    frame_1.rowconfigure(0, weight=1)

    frame_2.columnconfigure(0, weight=1)
    frame_2.rowconfigure(0, weight=1)
    frame_2.columnconfigure(1, weight=1)
    frame_2.rowconfigure(0, weight=1)

    frame_2.columnconfigure(2, weight=1)
    frame_2.rowconfigure(0, weight=1)

    frame_2.columnconfigure(3, weight=2)
    frame_2.rowconfigure(0, weight=1)    

    configFrame()

def configFrame():
    #Frame 2
    Button( frame_2 , text="Iniciar", command=openWindow,).pack()
    
def openWindow():
    #app.withdraw()
    w1.window1()
    
    
if __name__ == "__main__":
    config()
    app.mainloop()