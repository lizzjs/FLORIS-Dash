
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import apps.floris_data

# Imported but not used. This loads the callback functions into the web page.
import apps.model_builder.turbine_callbacks

geometry_inputs = dbc.Card(
    dbc.CardBody([
        html.H3("Turbine geometry definition.", className="card-text"),

        dbc.FormGroup([
            dbc.Label("Rotor diameter"),
            dbc.Input(
                id="input-rotordiam",
                type="number",
                min=0,
                max=500,
                value=apps.floris_data.user_defined_dict["turbine"]["properties"]["rotor_diameter"]
            ),
        ]),

        dbc.FormGroup([
            dbc.Label("Hub height"),
            dbc.Input(
                id="input-hubheight",
                type="number",
                min=0,
                max=500,
                value=apps.floris_data.user_defined_dict["turbine"]["properties"]["hub_height"]
            ),
        ]),
        
        dbc.FormGroup([
            dbc.Label("Yaw angle"),
            dbc.Input(
                id="input-yawangle",
                type="number",
                min=0,
                max=14,
                step=0.01,
                value=apps.floris_data.user_defined_dict["turbine"]["properties"]["yaw_angle"]
            ),
        ]),

        dbc.FormGroup([
            dbc.Label("Tilt angle"),
            dbc.Input(
                id="input-tiltangle",
                type="number",
                min=0,
                max=14,
                step=0.01,
                value=apps.floris_data.user_defined_dict["turbine"]["properties"]["tilt_angle"]
            )
        ]),

        dbc.FormGroup([
            dbc.Label("Tip speed ratio"),
            dbc.Input(
                id="input-TSR",
                type="number",
                min=0,
                max=20,
                value=apps.floris_data.user_defined_dict["turbine"]["properties"]["TSR"]
            ),
        ]),

        dbc.FormGroup([
            dbc.Label("Generator efficiency"),
            dbc.Input(
                id="input-genEff",
                type="number",
                min=0,
                max=20,
                value=apps.floris_data.user_defined_dict["turbine"]["properties"]["generator_efficiency"]
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
                value=apps.floris_data.user_defined_dict["turbine"]["properties"]["pP"]
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
                value=apps.floris_data.user_defined_dict["turbine"]["properties"]["pT"]
            ),
        ]),

        dbc.FormGroup([
            dbc.Label("Turbine grid point count (ngrid)"),
            dcc.Slider(
                id="slider-ngrid",
                min=1,
                max=9,
                marks={i: '{}'.format(i) for i in range(10)},
                value=apps.floris_data.user_defined_dict["turbine"]["properties"]["ngrid"]
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
                value=apps.floris_data.user_defined_dict["turbine"]["properties"]["rloc"]
            ),
        ]),

        dbc.FormGroup([
            dbc.Checklist(
                options=[{"label": "Use points on perimeter", "value": 1}],
                id="switch-perimeter-points",
                switch=True,
                value=apps.floris_data.user_defined_dict["turbine"]["properties"]["use_points_on_perimeter"]
            ),
        ]),
    ]),
    className="mt-3",
)

table = dash_table.DataTable(
    id = 'turbine-performance-datatable',
    editable=True,
    style_table={'height': '800px', 'overflowY': 'auto'},
)

performance_inputs = dbc.Card(
    dbc.CardBody([
        dbc.Row(
            dbc.Col(
                html.H3("Turbine performance definition.", className="card-text mb-3")
            )
        ),

        dbc.Row([
            dbc.Col(
                table,
                width=4
            ),

            dbc.Col(
                [
                    dcc.Graph(id="CpU"),
                    dcc.Graph(id="CtU"),
                ],
                width=8
            )
        ])
    ]),
    className="mt-3",
)

layout = html.Div([
    dbc.Row([
        dbc.Col(geometry_inputs, width=3),
        dbc.Col(performance_inputs, width=9)
    ])
])
