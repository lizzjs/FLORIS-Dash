import dash
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import io
import pandas as pd

from app import app, colors

#FARM LAYOUT CALLBACKS
@app.callback(
    Output('farm-graph', 'figure'),
    # Output('textarea-farm-output'),
    Input('textarea-farm-layout-button', 'n_clicks'),
    State('textarea-farm-layout', 'value'),
)
def textinput_graphs(n_clicks, value):
    ctx = dash.callback_context
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if value is not None and trigger_id == "textarea-farm-layout-button":
        data = io.StringIO(value)
        df2 = pd.read_csv(data, sep=",")
        print(df2)

    else:
        df2 = pd.DataFrame({
            "x": [],
            "y": [],
        })
    fig = plot_farm(df2)

    return fig

def plot_farm(df2: pd.DataFrame) -> (go.Figure):
    x = df2['x']
    y = df2['y']
    fig = go.Figure(
        data=[
            go.Scatter(
                x=x, 
                y=y,
                mode='markers')
            ],
            layout=go.Layout(
                plot_bgcolor=colors["graphBackground"],
            #     paper_bgcolor=colors["graphBackground"]
            )
    )
    return fig
