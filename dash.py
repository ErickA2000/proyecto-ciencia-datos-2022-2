from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


def dash(fig, titulo: str):
    app = Dash(__name__)
    
    app.layout = html.Div(children=[
        html.H1(children=titulo.capitalize),

        dcc.Graph(
            id='graph',
            figure=fig
        )
    ])
    app.run_server(debug=True)
    