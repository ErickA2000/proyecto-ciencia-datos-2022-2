from tkinter import *
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import cufflinks as cf
from IPython.display import display, HTML
import os.path

app = Tk()

frame_1 = Frame(app, bg='white')
frame_2 = Frame(app, bg='gray')

tabla = ttk.Treeview( frame_1, height=10 )

def abrirArchivo():
    archivo = filedialog.askopenfilename(title="Abrir", filetypes=(("Archivo de excel", "*.xlsx"),
    ("Archivos separados por coma", "*.csv"), ("Todos los archivos", "*.*")))

    nombre, extencion = os.path.splitext(archivo)
    if extencion == ".xlsx":
        df = pd.read_excel(archivo)
        generarTabla(df)
    elif extencion == ".csv":
        df = pd.read_csv(archivo)
        generarTabla(df)
    else:
        messagebox.showerror(title="Error", message="Formato de archivo no valido o archivo corrompido")
    
def generarTabla(df):
    tabla['column'] = list(df.columns)
    tabla['show'] = "headings"
    
    for columna in tabla['column']:
        tabla.heading(columna, text=columna)
    
    df_fila = df.to_numpy().tolist()
    for fila in df_fila:
        tabla.insert('', 'end', values=fila)

        
def config():
    app.config(bg="white")
    app.geometry("600x400")
    app.minsize(width=600, height=400)
    app.title("Analisis datos")

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
    #Frame 1    
    tabla.grid(column=0, row=0, sticky='nsew')

    Button( frame_2 , text="Abrir archivo", command=abrirArchivo ).pack()

if __name__ == "__main__":
    config()
    cf.set_config_file(sharing="public", theme="white", offline=True)
    app.mainloop()