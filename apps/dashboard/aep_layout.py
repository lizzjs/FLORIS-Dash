
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

# Imported but not used. This loads the callback functions into the web page.
import apps.dashboard.aep_callbacks


layout = dbc.Container(
    [
        html.Div(id="floris-compute-time", style={"hidden": "true"}),
        dbc.Row([
            dbc.Col(dcc.Graph(id='model-comparison-graph')),
            dbc.Col(dcc.Graph(id='compute-time-graph'))
        ]),
     
        # dbc.Row(
        #     dbc.Col(dcc.Graph(id='energy-gain-graph')
        # ),
        # justify="center"
        # ),
   
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id='aep-farm-graph')),
                dbc.Col(dcc.Graph(id='aep-windrose-graph'))
            ],
            justify="around"
        )
    ],
    fluid=True,
)