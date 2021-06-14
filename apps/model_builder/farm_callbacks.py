
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

from app import app, colors
import apps.floris_data


@app.callback(
    Output('farm-layout-graph', 'figure'),
    Input('farm-layout-datatable', 'data')
)
def create_farm_layout_plots(data):
    df = pd.DataFrame(data)
    fig = go.Figure(
        data=[
            go.Scatter(
                x=df['layout_x'],
                y=df['layout_y'],
                mode='markers'
            )
        ],
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
        df = pd.DataFrame(
            {
                'layout_x': apps.floris_data.user_defined_dict["farm"]["properties"]["layout_x"],
                'layout_y': apps.floris_data.user_defined_dict["farm"]["properties"]["layout_y"]
            }
        )
    else:
        df = pd.DataFrame(data)

    columns = [{"name": i, "id": i} for i in df.columns]
    return df.to_dict("rows"), columns
