from tkinter import *
from tkinter import messagebox, ttk
import pandas as pd
import cufflinks as cf
import plotly.express as px
import webbrowser

cf.go_offline()
cf.set_config_file(sharing="public", theme="space")

def main(df: pd.DataFrame):
    window = Tk()


    columns_name = df.columns.values
    columns_name_list = list(columns_name)
    frame_1 = Frame( window, bg='gray' )
    frame_2 = Frame( window, bg="white" )

    combo_1 = ttk.Combobox( frame_1, state="readonly", values=columns_name_list)
    combo_2 = ttk.Combobox( frame_1, state="readonly", values=columns_name_list)
    combo_3 = ttk.Combobox( frame_1, state="readonly", values=columns_name_list)
    combo_3_type_graph = ttk.Combobox( frame_1, state="readonly", values=["Barras", "Dispersion", "Tarta"] )

    def config( window: Tk ):
        window.config(bg='white')
        window.geometry("600x400")
        window.minsize( width=600, height=400 )
        window.title("Datos a graficar")

        window.columnconfigure(0, weight=25)
        window.rowconfigure(0, weight=25)
        window.columnconfigure(0, weight=1)
        window.rowconfigure(0, weight=1)

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

        configFrame( )

    def showSelection( ):
        selection_1 = combo_1.get()
        selection_2 = combo_2.get()
        selection_3 = combo_3.get()
        selection_type_graph = combo_3_type_graph.get()
        
        if( selection_1 == "" and selection_2 == "" ):
            messagebox.showerror(title="Error", message="Es necesario seleccionar las variables de x & y")
        else:
            if( selection_type_graph == "Barras" ):
                if( selection_1 and selection_2 and selection_3 ):
                    fig = px.bar(df, x=selection_1, y=selection_2, color=selection_3, barmode="group" )
                    generarHtmlGrafica(fig)

                elif( selection_1 and selection_2 and selection_3 == "" ):
                    fig = px.bar(df, x=selection_1, y=selection_2, barmode="group" )
                    generarHtmlGrafica(fig)
                    

            elif( selection_type_graph == "Dispersion" ):
                if( selection_1 and selection_2 and selection_3 ):
                    fig = px.scatter(df, x=selection_1, y=selection_2, color=selection_3)
                    generarHtmlGrafica(fig)
                elif( selection_1 and selection_2 and selection_3 == "" ):
                    fig = px.scatter(df, x=selection_1, y=selection_2)
                    generarHtmlGrafica(fig)

            elif( selection_type_graph == "Tarta" ):
                fig = px.pie(df, values=selection_1, names=selection_2)
                generarHtmlGrafica(fig)
            else:
                messagebox.showerror(title="Error", message="Falta selectionar el tipo de grafica")

    def generarHtmlGrafica(fig):
        fig.write_html("graph.html")
        webbrowser.open_new_tab('graph.html')

  
    def configFrame( ):
        #Frame 1
        combo_1.place(x=30, y=30)
        combo_2.place(x=280, y=30)
        combo_3.place(x=100, y=60)
        combo_3_type_graph.place(relx=0.5, rely=0.5, width=100, anchor='c')

        #Frame 2
        Button( frame_2, text="Prueba", command=showSelection ).pack()

    

    config( window )