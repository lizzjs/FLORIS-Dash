
import dash
from dash.dependencies import Input, Output, State
import pandas as pd

from app import app
import apps.floris_data
from graph_generator import *


def dict_to_list(table_dict, key):
    l = [] 
    for row in table_dict:
        l.append(row[key])
    return l


def _get_farm_definition_layout(key, value, initial_input_store, farm_store):
    # On first load
    if value is None:
        if farm_store is not None:
            if key in farm_store:
                return farm_store[key]

        if initial_input_store is None:
            # TODO: Do we leave this? This handles the situation when the input store is not available for any reason.
            initial_input_store = apps.floris_data.default_input_dict
        return initial_input_store["farm"]["properties"][key]
    # On every other call, return the value in the field
    return dict_to_list(value, key)


@app.callback(
    Output('farm-layout-graph', 'figure'),
    Input('farm-layout-datatable', 'data'),
    Input('boundary-layout-datatable', 'data'),
)
def farm_layout_and_boundary_plot(farm_data, boundary_data):
    df = pd.DataFrame(farm_data)
    if boundary_data is not None: 
        df2 = pd.DataFrame(boundary_data)
        df2 = df2.append(df2.iloc[0,:], ignore_index=True)
    farm_layout_plot = create_farm_layout_plot(df, df2)
    farm_layout_plot.update_layout(
        title="",
        height=550,
        width=825
        )
    return farm_layout_plot


@app.callback(
    Output('farm-layout-datatable', 'data'),
    Output('farm-layout-datatable', 'columns'),
    Input('farm-layout-datatable', 'data'),
    Input('button-add-layout-row', 'n_clicks'),
    State('initial-input-store', 'data'),
    State('farm-input-store', 'data')
)
def get_layout_table_data(data, n_clicks, initial_input_store, farm_store):
    ctx = dash.callback_context
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]

    # Adding a row to the existing datatable
    if trigger_id == "button-add-layout-row":
        columns = [{"name": i, "id": i} for i in ["layout_x", "layout_y"]]
        data.append({c['id']: '' for c in columns})
        return data, columns
    
    # Getting the data from a data store
    layout_x_column = _get_farm_definition_layout('layout_x', data, initial_input_store, farm_store)
    layout_y_column = _get_farm_definition_layout('layout_y', data, initial_input_store, farm_store)

    rows = {
        'layout_x': layout_x_column,
        'layout_y': layout_y_column
    }

    df = pd.DataFrame(rows)
    columns = [{"name": i, "id": i} for i in df.columns]
    return df.to_dict("rows"), columns


@app.callback(
    Output('boundary-layout-datatable', 'data'),
    Output('boundary-layout-datatable', 'columns'),
    Input('boundary-layout-datatable', 'data'),
    State('initial-input-store', 'data'),
    State('farm-input-store', 'data')
)
def get_boundary_table_data(data, initial_input_store, farm_store):

    boundary_x_column = _get_farm_definition_layout('boundary_x', data, initial_input_store, farm_store)
    boundary_y_column = _get_farm_definition_layout('boundary_y', data, initial_input_store, farm_store)

    rows = {
        'boundary_x': boundary_x_column,
        'boundary_y': boundary_y_column
    }

    df = pd.DataFrame(rows)
    columns = [{"name": i, "id": i} for i in df.columns]
    return df.to_dict("rows"), columns


@app.callback(
    Output('farm-input-store', 'data'),
    Input('farm-layout-datatable', 'data'),
    Input('boundary-layout-datatable', 'data'),
)
def store_farm_data(farm_data_table, boundary_data_table):
    layout_x = dict_to_list(farm_data_table, "layout_x")
    layout_y = dict_to_list(farm_data_table, "layout_y")
    boundary_x = dict_to_list(boundary_data_table, "boundary_x")
    boundary_y = dict_to_list(boundary_data_table, "boundary_y")
    farm_data = {
        "layout_x": layout_x,
        "layout_y": layout_y,
        "boundary_x": boundary_x,
        "boundary_y": boundary_y,
    }
    return farm_data
