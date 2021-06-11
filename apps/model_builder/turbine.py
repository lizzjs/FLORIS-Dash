
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from app import app, colors

# Imported but not used. This loads the callback functions into the web page.
import apps.model_builder.turbine_callbacks
import dash_table
from pandas import DataFrame

geometry_inputs = dbc.Card(
    dbc.CardBody(
        [
            html.H3("How does your wind turbine look?", className="card-text"),

            dbc.FormGroup(
                [
                    dbc.Label("Tip speed ratio"),
                    dbc.Input(id="input-TSR", type="number", min=0, max=20),
                ]
            ),

            dbc.FormGroup(
                [
                    dbc.Label("Blade count"),
                    dcc.Slider(id="slider-bladecount", min=1, max=9, marks={i: '{}'.format(i) for i in range(10)}, value=1),
                ]
            ),

            dbc.FormGroup(
                [
                    dbc.Label("Blade pitch"),
                    dbc.Input(id="input-bladepitch", type="number", min=0, max=20),
                ]
            ),

            dbc.FormGroup(
                [
                    dbc.Label("Generator efficiency"),
                    dbc.Input(id="input-genEff", type="number", min=0, max=20),
                ]
            ),

            dbc.FormGroup(
                [
                    dbc.Label("Hub height"),
                    dbc.Input(id="input-hubheight", type="number", min=0, max=500),
                ]
            ),

            dbc.FormGroup(
                [
                    dbc.Label("Turbine grid point count (ngrid)"),
                    dcc.Slider(id="slider-ngrid", min=1, max=9, marks={i: '{}'.format(i) for i in range(10)}, value=1),
                ]
            ),

            dbc.FormGroup(
                [
                    dbc.Label("pP"),
                    dbc.Input(id="input-pP", type="number", min=0, max=3, step=0.01),
                ]
            ),
            dbc.FormGroup(
                [
                    dbc.Label("pT"),
                    dbc.Input(id="input-pT", type="number", min=0, max=3, step=0.01),
                ]
            ),

            dbc.FormGroup(
                [
                    dbc.Label("rloc"),
                    dbc.Input(id="input-rloc", type="number", min=0, max=3, step=0.01),
                ]
            ),

            dbc.FormGroup(
                [
                    dbc.Label("Tilt angle"),
                    dcc.Slider(id="slider-tiltang", min=1, max=15, marks={i: '{}'.format(i) for i in range(15)}, value=1),
                ]
            ),

            dbc.FormGroup(
                [
                    dbc.Label("Yaw angle"),
                    dcc.Slider(id="slider-yawang", min=1, max=15, marks={i: '{}'.format(i) for i in range(15)}, value=1),
                ]
            ),

            dbc.FormGroup(
                [
                    dbc.Checklist(
                        options=[{"label": "Use points on perimeter", "value": 1}],
                        value=[],
                        id="switches-perimeter-points",
                        switch=True,
                    ),
                ]
            ),

            dbc.FormGroup(
                [
                    dbc.Label("Rotor diameter"),
                    dbc.Input(id="input-rotordiam", type="number", min=0, max=500),
                ]
            ),
        ]
    ),
    className="mt-3",
)

dbc.ListGroupItem( dbc.Button("Next", color="primary", href="/builder/farm") ),

dummy_df = DataFrame({})
table =dbc.Row(
    [   
        dash_table.DataTable(
            id = 'performance-datatable',
            data=dummy_df.to_dict("rows"),
            columns=[{"name": i, "id": i} for i in dummy_df.columns],
            style_table={'height': '300px', 'overflowY': 'auto'},
        )
    ]
)

performance_inputs = dbc.Card(
    dbc.CardBody(
        [
            html.H3("How does your wind turbine perform?", className="card-text"),

            dbc.Row(
                [
                    dbc.Col(
                        [
                            table,
                        ],
                        width=3
                    ),

                    dbc.Col(
                        [
                            dcc.Graph(id="Mygraph1"),
                            dcc.Graph(id="Mygraph2"),

                        ]
                    )
                    
                ]
            )
        ]
    ),
    className="mt-3",
)

tabs = dbc.Tabs(
    [
        dbc.Tab(
            dbc.Container(
                [
                    dbc.Row([dbc.Col(geometry_inputs, width=6)])
                ]
            ),
            label="Geometry"
        ),
        dbc.Tab( id="performance-tab", children=
            [
                dbc.Container(
                    [
                        dbc.Row([dbc.Col(performance_inputs, width=12)])
                    ]
                )
            ],
            label="Performance"
        ),
    ]
)

layout = html.Div([tabs])
