
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
    Input('textarea-boundary-button', 'n_clicks'),
    State('textarea-boundary', 'value'),
)
def create_farm_layout_plots(farm_data, n, boundary_data):
    df = pd.DataFrame(farm_data)

    ctx = dash.callback_context
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]

    figure_data = [
        go.Scatter(
            x=df['layout_x'],
            y=df['layout_y'],
            mode='markers'
        )
    ]
    
    #TODO connect boundary input data to floris_data
    if boundary_data is not None and trigger_id == "textarea-boundary-button":
        boundary_data = io.StringIO(boundary_data)
        df_b = pd.read_csv(boundary_data, sep=",")
        df2 = pd.DataFrame(df_b) #df_b does not have .append attribute
        df2 = df2.append(df2.iloc[0,:], ignore_index=True)
        figure_data.append(
            go.Line(
                x=df2['boundary_x'],
                y=df2['boundary_y'],
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
