
import dash
from dash.dependencies import Input, Output, State
import io
import pandas as pd
import plotly.graph_objs as go

from app import app, colors
import apps.floris_data


@app.callback(
    Output('farm-layout-graph', 'figure'),
    Input('farm-layout-datatable', 'data'),
    Input('boundary-layout-datatable', 'data'),
)
def create_farm_layout_plots(farm_data, boundary_data):
    df = pd.DataFrame(farm_data)

    figure_data = [
        go.Scatter(
            x=df['layout_x'],
            y=df['layout_y'],
            mode='markers',
            name='Wind turbines'
        )
    ]

    if boundary_data is not None: 
        df2 = pd.DataFrame(boundary_data)
        df2 = df2.append(df2.iloc[0,:], ignore_index=True)
        figure_data.append(
            go.Line(
                x=df2['boundary_x'],
                y=df2['boundary_y'],
                name='Boundary'
            )
        )

    fig = go.Figure(
        data=figure_data,
        layout=go.Layout(
            plot_bgcolor=colors["graphBackground"],
            # paper_bgcolor=colors["graphBackground"]
        )
    )
    return fig


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
