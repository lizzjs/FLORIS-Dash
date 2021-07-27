
from dash.dependencies import Input, Output, State
import pandas as pd

from app import app
import apps.floris_data
from apps.graph_generator import *


def _get_wind_rose_data(key, value, wind_rose_store):
    # On first load
    if value is None:
        if wind_rose_store is not None:
            if key in wind_rose_store:
                return wind_rose_store[key]

        return apps.floris_data.wind_rose_data

    # On every other call, return the values in the table
    return value


@app.callback(
    Output('wind-rose-datatable', 'data'),
    Output('wind-rose-datatable', 'columns'),
    Input('wind-rose-datatable', 'data'),
    State('wind-rose-input-store', 'data')
)
def get_wind_rose_table_data(data, wind_rose_store):
    key = "wind_rose_table"
    table = _get_wind_rose_data(key, data, wind_rose_store)
    df = pd.DataFrame(table)
    columns = [{"name": i, "id": i} for i in df.columns]
    return df.to_dict("rows"), columns


@app.callback(
    Output('wind-rose-graph', 'figure'),
    Input('wind-rose-datatable', 'data')
)
def atmos_cond_wind_rose_plot(data):
    df_windrose = pd.DataFrame(data)
    wind_rose_figure = create_windrose_plot(df_windrose)
    wind_rose_figure.update_layout(
        title="",
        height=600,
        width=750
    )
    return wind_rose_figure


## Wind rose store

@app.callback(
    Output('wind-rose-input-store', 'data'),
    Input('wind-rose-datatable', 'data'),
)
def store_wind_rose(wind_rose_table):
    wind_rose_data = {
        "wind_rose_table": wind_rose_table,
    }
    return wind_rose_data
