
from dash.dependencies import Input, Output
import pandas as pd

from app import app
import apps.floris_data
from graph_generator import *


@app.callback(
    Output('farm-layout-graph', 'figure'),
    Input('farm-layout-datatable', 'data'),
    Input('boundary-layout-datatable', 'data'),
)
def farm_layout(farm_data, boundary_data):
    df = pd.DataFrame(farm_data)
    if boundary_data is not None: 
        df2 = pd.DataFrame(boundary_data)
        df2 = df2.append(df2.iloc[0,:], ignore_index=True)
    farm_layout_plot = create_farm_layout_plot(df, df2)
    farm_layout_plot.update_layout(title="")
    return farm_layout_plot

@app.callback(
    [Output('farm-layout-datatable', 'data'),
    Output('farm-layout-datatable', 'columns')],
    Input('farm-layout-datatable', 'data')
)
def get_layout_table_data(data):
    if data is None:
        df_farm = pd.DataFrame(
            {
                'layout_x': apps.floris_data.user_defined_dict["farm"]["properties"]["layout_x"],
                'layout_y': apps.floris_data.user_defined_dict["farm"]["properties"]["layout_y"]
            }
        )
    else:
        df_farm = pd.DataFrame(data)

    columns = [{"name": i, "id": i} for i in df_farm.columns]
    return df_farm.to_dict("rows"), columns

@app.callback(
    [Output('boundary-layout-datatable', 'data'),
    Output('boundary-layout-datatable', 'columns')],
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
