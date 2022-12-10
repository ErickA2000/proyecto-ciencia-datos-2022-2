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
    frame_1 = Frame( window, bg='#ad3333' )
    frame_2 = Frame( window, bg="#ad3333" )

    title_graph = Entry(frame_1)

    combo_1 = ttk.Combobox( frame_1, state="readonly", values=columns_name_list)
    combo_2 = ttk.Combobox( frame_1, state="readonly", values=columns_name_list)
    combo_3 = ttk.Combobox( frame_1, state="readonly", values=columns_name_list)
    combo_4_type_graph = ttk.Combobox( frame_1, state="readonly", values=["Barras", "Dispersion", "Tarta"] )

    def config( window: Tk ):
        window.config(bg='white')
        window.geometry("600x400")
        window.minsize( width=600, height=400 )
        window.title("Datos a graficar")
        window.resizable(width=False, height=False)

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
        selection_type_graph = combo_4_type_graph.get()
        
        if( selection_1 == "" and selection_2 == "" ):
            messagebox.showerror(title="Error", message="Es necesario seleccionar las variables de x & y")
        else:
            if( selection_type_graph == "Barras" ):
                if( selection_1 and selection_2 and selection_3 ):
                    fig = px.bar(df, x=selection_1, y=selection_2, color=selection_3, barmode="group", title=title_graph.get() )
                    generarHtmlGrafica(fig)

                elif( selection_1 and selection_2 and selection_3 == "" ):
                    fig = px.bar(df, x=selection_1, y=selection_2, barmode="group", title=title_graph.get() )
                    generarHtmlGrafica(fig)
                    

            elif( selection_type_graph == "Dispersion" ):
                if( selection_1 and selection_2 and selection_3 ):
                    fig = px.scatter(df, x=selection_1, y=selection_2, color=selection_3, title=title_graph.get())
                    generarHtmlGrafica(fig)
                elif( selection_1 and selection_2 and selection_3 == "" ):
                    fig = px.scatter(df, x=selection_1, y=selection_2, title=title_graph.get())
                    generarHtmlGrafica(fig)

            elif( selection_type_graph == "Tarta" ):
                fig = px.pie(df, values=selection_1, names=selection_2, title=title_graph.get())
                generarHtmlGrafica(fig)
            else:
                messagebox.showerror(title="Error", message="Falta selectionar el tipo de grafica")

    def generarHtmlGrafica(fig):
        fig.write_html("graph.html")
        webbrowser.open_new_tab('graph.html')

    def configFrame( ):
        #Frame 1
        combo_1.place(relx=0.1, rely=0.1)
        combo_2.place(relx=0.6, rely=0.1)
        combo_3.place(relx=0.5, rely=0.25, anchor="c")
        combo_4_type_graph.place(relx=0.5, rely=0.5, width=100, anchor='c')

            #Labels
        label_combo_1 =Label( frame_1, text="X", background="gray" )
        label_combo_1.place(relx=0.25, rely=0.04)
        label_combo_2 =Label( frame_1, text="Y", background="gray" )
        label_combo_2.place(relx=0.75, rely=0.04)
        label_combo_3 =Label( frame_1, text="Color", background="gray" )
        label_combo_3.place(relx=0.5, rely=0.18, anchor="c")
        label_combo_4 =Label( frame_1, text="Tipo de gráfica disponible", background="gray" )
        label_combo_4.place(relx=0.35, rely=0.4)
        label_title = Label( frame_1, text="Titulo de gráfica", background="gray" )
        label_title.place( relx=0.5, rely=0.7, anchor="c" )

            #Entrada
        title_graph.place(relx=0.5, rely=0.8, width=200 , anchor="c")


        #Frame 2
        Button( frame_2, text="Crear Grafica", command=showSelection ).pack()

    config( window )