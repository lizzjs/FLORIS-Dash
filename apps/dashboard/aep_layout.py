
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Row import Row
import dash_core_components as dcc
import dash_html_components as html

# Imported but not used. This loads the callback functions into the web page.
import apps.dashboard.aep_callbacks

graph_layout = html.Div([
    dbc.Row(
        dbc.Col(
            html.Div(
                children=[
                    dbc.Spinner(),
                    "FLORIS simulation is running. AEP results will update here shortly.",
                ],
                id="loading-spinner"
            )
        )
    ),
    dbc.Row(
        children=[
            dbc.Col(
                html.Div(
                    # dbc.Spinner(),
                    id="model-comparison-graph-div"
                ),
                # dcc.Graph(id='model-comparison-graph')
            ),
            dbc.Col(
                html.Div(
                    # dbc.Spinner(),
                    id="compute-time-graph-div"
                ),
                # dcc.Graph(id='compute-time-graph')
            )
        ],
        justify="around"
    ),
    dbc.Row(
        children=[
            dbc.Col(
                html.Div(
                    # dbc.Spinner(),
                    id="aep-farm-graph-div"
                ),
                # dcc.Graph(id='aep-farm-graph')
            ),
            dbc.Col(
                html.Div(
                    # dbc.Spinner(),
                    id="aep-windrose-graph-div"
                ),
                # dcc.Graph(id='aep-windrose-graph')
            )
        ],
        justify="around"
    ),
    # dbc.Row(
    #     dbc.Col(dcc.Graph(id='energy-gain-graph')
    # ),
    # justify="center"
    # ),
])

layout = html.Div(
    children=[
        # This row will overlap the content below it in order to avoid having the download button included in the pdf export
        dbc.Row(
            children=[ 
                dbc.Col(width=11),
                dbc.Col(
                    dbc.Button(
                        children=[
                            html.Img(
                                src="/assets/file-download.png", 
                                style={'width':'30px', 'align':'center'}
                            )
                        ], 
                        className="btn-light",
                        id='js',
                        n_clicks=0
                    ), 
                    style={'margin':'25px 0px 0px 30px'}
                ),
            ],
            style={'height':'0px'}
        ),
        html.Div(
            children=[
                dbc.Row(
                    dbc.Col(html.H2("Annual Energy Production Dashboard")), 
                    style={'height':'55px'},
                ),
                html.Br(),
                dbc.Card(
                    children=[
                        dbc.CardBody(
                            children=[
                                graph_layout,
                            ]
                        )
                    ],
                    className='cardDesign'
                )
            ],
            id='print'
        )
    ],
    id='main'
)
