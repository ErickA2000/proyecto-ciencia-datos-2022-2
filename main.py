from tkinter import *
#from functools import partial
#from tkinter import filedialog, messagebox, ttk
#import pandas as pd
#import cufflinks as cf
#from IPython.display import display, HTML
#import os.path

import window_1 as w1

app = Tk()

frame_1 = Frame(app, bg='white')
frame_2 = Frame(app, bg='gray')


def config():
    app.config(bg="white")
    app.geometry("600x400")
    app.minsize(width=600, height=400)
    app.title("Proyecto de clase ciencia de datos")

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
    Button( frame_2 , text="Iniciar", command=openWindow ).pack()
    
def openWindow():
    #app.withdraw()
    w1.window1()
    
if __name__ == "__main__":
    config()
    #cf.set_config_file(sharing="public", theme="white", offline=True)
    app.mainloop()