
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table

# Imported but not used. This loads the callback functions into the web page.
import apps.model_builder.turbine_callbacks

geometry_inputs = dbc.Card(
    [
        dbc.CardHeader("Geometry Inputs"),
        dbc.CardBody([
            dbc.FormGroup([
                dbc.Label("Rotor diameter"),
                dbc.Input(
                    id="input-rotor-diameter",
                    type="number",
                    min=0,
                    max=500,
                ),
            ]),

            dbc.FormGroup([
                dbc.Label("Hub height"),
                dbc.Input(
                    id="input-hub-height",
                    type="number",
                    min=0,
                    max=500,
                ),
            ]),
            
            dbc.FormGroup([
                dbc.Label("Yaw angle"),
                dbc.Input(
                    id="input-yaw-angle",
                    type="number",
                    min=0,
                    max=14,
                    step=0.01,
                ),
            ]),

            dbc.FormGroup([
                dbc.Label("Tilt angle"),
                dbc.Input(
                    id="input-tilt-angle",
                    type="number",
                    min=0,
                    max=14,
                    step=0.01,
                )
            ]),

            dbc.FormGroup([
                dbc.Label("Tip speed ratio"),
                dbc.Input(
                    id="input-tip-speed-ratio",
                    type="number",
                    min=0,
                    max=20,
                ),
            ]),

            dbc.FormGroup([
                dbc.Label("Generator efficiency"),
                dbc.Input(
                    id="input-generator-efficiency",
                    type="number",
                    min=0,
                    max=20,
                ),
            ]),

            dbc.FormGroup([
                dbc.Label("pP"),
                dbc.Input(
                    id="input-pP",
                    type="number",
                    min=0,
                    max=3,
                    step=0.01,
                ),
            ]),

            dbc.FormGroup([
                dbc.Label("pT"),
                dbc.Input(
                    id="input-pT",
                    type="number",
                    min=0,
                    max=3,
                    step=0.01,
                ),
            ]),

            dbc.FormGroup([
                dbc.Label("Turbine grid point count (ngrid)"),
                dcc.Slider(
                    id="slider-ngrid",
                    min=1,
                    max=9,
                    marks={i: '{}'.format(i) for i in range(10)},
                ),
            ]),

            dbc.FormGroup([
                dbc.Label("rloc"),
                dbc.Input(
                    id="input-rloc",
                    type="number",
                    min=0,
                    max=3,
                    step=0.01,
                ),
            ]),

            dbc.FormGroup([
                dbc.Checklist(
                    options=[{"label": "Use points on perimeter", "value": 1}],
                    id="switch-perimeter-points",
                    switch=True,
                ),
            ]),
        ]),
    ],
    className="mt-3",
)

performance_datatable = dash_table.DataTable(
    id='turbine-performance-datatable',
    editable=True,
    row_deletable=True,
    style_table={'height': '970px', 'overflowY': 'auto'},
)

performance_inputs = dbc.Row([
    dbc.Col(
        children=[
            performance_datatable,
        ],
        width=4
    ),
    dbc.Col(
        children=[
            dcc.Graph(id="CpU"),
            dcc.Graph(id="CtU"),
        ],
    )
])

layout = html.Div(
    children=[
        html.H3("Turbine Definition"),
        html.Br(),
        dbc.Card([
            dbc.CardBody(
                dbc.Row([
                    dbc.Col(
                        children=[
                            geometry_inputs
                        ],
                        width=3
                    ),
                    dbc.Col(
                        children=[
                            performance_inputs
                        ],
                        width=9
                    )
                ])
            )
        ])
    ]
)
