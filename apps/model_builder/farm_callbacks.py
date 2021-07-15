
import dash
from dash.dependencies import Input, Output, State
import pandas as pd

from app import app
import apps.floris_data
from graph_generator import *


@app.callback(
    Output('farm-layout-graph', 'figure'),
    Input('farm-layout-datatable', 'data'),
    Input('boundary-layout-datatable', 'data'),
)
def plot_layout_and_boundary(farm_data, boundary_data):
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
    State('farm-layout-datatable', 'data'),
    State('farm-layout-datatable', 'columns')
)
def get_layout_table_data(data, n_clicks, rows, columns):
    # On page load
    if data is None:
        df_farm = pd.DataFrame(
            {
                'layout_x': apps.floris_data.user_defined_dict["farm"]["properties"]["layout_x"],
                'layout_y': apps.floris_data.user_defined_dict["farm"]["properties"]["layout_y"]
            }
        )
        columns = [{"name": i, "id": i} for i in df_farm.columns]
        return df_farm.to_dict("rows"), columns

    # Otherwise, handle add row and data change
    ctx = dash.callback_context
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if trigger_id == "farm-layout-datatable":
        df_farm = pd.DataFrame(data)
        columns = [{"name": i, "id": i} for i in df_farm.columns]
        return df_farm.to_dict("rows"), columns

    elif trigger_id == "button-add-layout-row":
        rows.append({c['id']: '' for c in columns})
        return rows, columns


@app.callback(
    Output('boundary-layout-datatable', 'data'),
    Output('boundary-layout-datatable', 'columns'),
    Input('boundary-layout-datatable', 'data')
)
def get_boundary_table_data(boundary_data):
    if boundary_data is None:
        df_boundary = pd.DataFrame(
            {
                'boundary_x': apps.floris_data.boundary_data["boundary_x"],
                'boundary_y': apps.floris_data.boundary_data["boundary_y"]
            }
        )
    else:
        df_boundary = pd.DataFrame(boundary_data)

    columns = [{"name": i, "id": i} for i in df_boundary.columns]
    return df_boundary.to_dict("rows"), columns
