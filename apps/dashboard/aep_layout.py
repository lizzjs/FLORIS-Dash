
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
# from apps.model_builder.atmos_cond_layout import wind_rose_graph
# from apps.model_builder.farm_layout import farm_graph
from apps.floris_connection.run_floris import calculate_wake
import apps.floris_data

# Imported but not used. This loads the callback functions into the web page.
import apps.dashboard.aep_callbacks


layout = dbc.Container(
    [
        html.Div(id="floris-compute-time", style={"hidden": "true"}),
        dbc.Row([
            dbc.Col(id='model-comparison-grpah'),
            dbc.Col(dcc.Graph(id='compute-time-graph'))
        ]),
     
        dbc.Row(
            dbc.Col(
                [
                    dbc.Col(id='energy-gain-graph')
                ]  
            )
        ),
   
        dbc.Row(
            [
                # dbc.Col([farm_graph,]),
                # dbc.Col([wind_rose_graph,])
            ], justify="around"
        )
    ],
    fluid=True,
)
