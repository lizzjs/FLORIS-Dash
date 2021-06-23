
from dash.dependencies import Input, Output, State
from floris.simulation import floris
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import numpy as np

from app import app
import apps.floris_data


@app.callback(
    # Output('model-comparison-grpah', 'figure'),
    Output('compute-time-graph', 'figure'),
    Output('aep-farm-graph', 'figure'),
    Output('aep-windrose-graph', 'figure'),
    Input("floris-outputs", "data")
)
def create_dashboard_plots(floris_output_data):

    # FLORIS AEP with and without wake steering
    # columns = ["Real AEP"] #, "Ideal AEP", "Optimal AEP"]
    # model_name = apps.floris_data.default_input_dict["wake"]["properties"]["velocity_model"] #change this
    # values = [[model_name, floris_output_data[model_name]]]
    # df = pd.DataFrame(values, columns=columns)

    # fig1 = px.scatter(
    #     df,
    #     x=columns[0],
    #     y=columns[1],
    #     template="seaborn",
    #     title="FLORIS AEP with and without Wake Steering"
    # )

    # Compute time
    columns_ct = ["Model Name", "Compute Time"]
    model_name_ct = apps.floris_data.default_input_dict["wake"]["properties"]["velocity_model"]
    values = [[model_name_ct, floris_output_data[model_name_ct]]]
    df2 = pd.DataFrame(values, columns=columns_ct)
    fig2 = px.bar(
        df2,
        x=columns_ct[0],
        y=columns_ct[1],
        template="seaborn",
        title="Compute Time"
    )

    #Wind farm
    df_wf = pd.DataFrame(
            {
                'layout_x': apps.floris_data.user_defined_dict["farm"]["properties"]["layout_x"],
                'layout_y': apps.floris_data.user_defined_dict["farm"]["properties"]["layout_y"]
            }
        )
    figure_data = [
        go.Scatter(
            x=df_wf['layout_x'],
            y=df_wf['layout_y'],
            mode='markers'
        )
    ]
    boundary_data = pd.DataFrame(
            {
                'boundary_x': apps.floris_data.farm_boundary["boundary_x"],
                'boundary_y': apps.floris_data.farm_boundary["boundary_y"]
            }
        )
    print("type: ", type(boundary_data), "contents: ")
    print(boundary_data)
    if boundary_data is not None:
        df_bf = boundary_data.append(boundary_data.iloc[0,:], ignore_index=True)
        figure_data.append(
            go.Line(
                x=df_bf['boundary_x'],
                y=df_bf['boundary_y'],
            )
        )
    fig4 = go.Figure(
        data=figure_data,
        layout=go.Layout(
            # plot_bgcolor=colors["graphBackground"],
            # paper_bgcolor=colors["graphBackground"]
        )
    )
    

    # Windrose
    df = pd.DataFrame(apps.floris_data.wind_rose_data)
    fig5 = px.bar_polar(
        df,
        r="frequency",
        theta="direction",
        color="strength",
        template="seaborn",
        color_discrete_sequence=px.colors.sequential.Plasma_r,
        title="Wind Rose"
    )

    return fig2, fig4, fig5 #fig1, 

