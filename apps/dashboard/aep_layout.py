
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

# Imported but not used. This loads the callback functions into the web page.
import apps.dashboard.aep_callbacks

graph_layout = html.Div([
    dbc.Row([
            dbc.Col(dcc.Graph(id='model-comparison-graph')),
            dbc.Col(dcc.Graph(id='compute-time-graph'))
        ],
        justify="around"
    ),
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
    ),
    

])

layout = html.Div(
    children=[
        html.H2("Annual Energy Production Dashboard"),
        html.Br(),
        dbc.Card([
            dbc.CardBody(
                [
                    dbc.Spinner(
                        [
                            graph_layout
                        ],
                        id="results-spinner",
                        type="circle"
                    ),
                    # dbc.Row(
                    #     [
                    #         dbc.Button("Export to PDF", className="mb-3",style={'margin':'5rem'},id='js',n_clicks=0) 
                    #     ],
                    #     justify="center",
                    # ),
                ]
            )
        ])
    ]
)