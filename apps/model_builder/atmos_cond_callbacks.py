
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

from app import app
import apps.floris_data
from graph_generator import *


@app.callback(
    Output('wind-rose-graph', 'figure'),
    Input('wind-rose-datatable', 'data')
)
def atmos_cond_wind_rose_plot(data):
    df_windrose = pd.DataFrame(data)
    wind_rose_figure = create_windrose_plot(df_windrose)
    wind_rose_figure.update_layout(
        height=400,
        width=550
    )
    return wind_rose_figure

@app.callback(
    Output('wind-rose-datatable', 'data'),
    Output('wind-rose-datatable', 'columns'),
    Input('wind-rose-datatable', 'data')
)
def get_wind_rose_table_data(data):
    if data is None:
        df = pd.DataFrame(apps.floris_data.wind_rose_data)
    else:
        df = pd.DataFrame(data)

    columns = [{"name": i, "id": i} for i in df.columns]
    return df.to_dict("rows"), columns
