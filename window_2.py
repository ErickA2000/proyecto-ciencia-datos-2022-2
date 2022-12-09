from tkinter import *
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode, iplot
import plotly.express as px
import plotly.graph_objects as go
import webbrowser
#import dash

#init_notebook_mode(connected=True)
#pd.options.plotting.backend = "plotly"
cf.go_offline()
cf.set_config_file(sharing="public", theme="space")

def main(df: pd.DataFrame):
    window = Tk()


    columns_name = df.columns.values
    columns_name_list = list(columns_name)
    frame_1 = Frame( window, bg='gray' )
    frame_2 = Frame( window, bg="white" )

    combo_1 = ttk.Combobox( frame_1, state="readonly", values=columns_name_list)
    combo_1.place(x=30, y=30)

    combo_2 = ttk.Combobox( frame_1, state="readonly", values=columns_name_list)
    combo_2.place(x=280, y=30)

    combo_3 = ttk.Combobox( frame_1, state="readonly", values=columns_name_list)
    combo_3.place(x=90, y=60)
    
    #window_2.mainloop()

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

        #data_df = df[[ selection_1, selection_2, selection_3 ]]
        #print(data_df)
        #data_df = data_df.pivot(columns=selection_1, values=selection_2)
        
        #fig = px.bar(x=df[selection_1], y=df[selection_2], color=df[selection_3], barmode="group", )
        fig = px.bar(df, x=selection_1, y=selection_2, color=selection_3, barmode="group", )
        '''fig = go.Figure(
            go.Bar( y=df[selection_2], x=df[selection_1])
        )'''
        #graphHTML = fig.show()
        #dash.dash(fig, "Prueba grafica")
        '''html = open("graph.html", "w")
        html.write()
        html.close()'''
        fig.write_html("graph.html")
        webbrowser.open_new_tab('graph.html')

  
    def configFrame( ):
        
        #Frame 2
        Button( frame_2, text="Prueba", command=showSelection ).pack()

    

    config( window )