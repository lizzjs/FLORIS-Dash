
import dash_bootstrap_components as dbc
import dash_table as dt
import dash_html_components as html

# Imported but not used. This loads the callback functions into the web page.
import apps.model_builder.wake_callbacks


velocity_radio = dbc.FormGroup([
    dbc.Label("Velocity deficit"),
    dbc.RadioItems(
        options=[
            {"label": "Jensen", "value": "jensen"},
            {"label": "Multizone", "value": "multizone"},
            {"label": "Gauss", "value": "gauss"},
        ],
        value="jensen",
        id="radio-deficit",
    ),
])

deflection_radio = dbc.FormGroup([
    dbc.Label("Deflection"),
    dbc.RadioItems(
        options=[
            {"label": "Jimenez", "value": "jimenez"},
            {"label": "Gauss", "value": "gauss"},
        ],
        value="jimenez",
        id="radio-deflection",
    ),
])

turbulance_radio = dbc.FormGroup([
    dbc.Label("Turbulence"),
    dbc.RadioItems(
        options=[
            {"label": "Crespo-Hernandez", "value": "crespo_hernandez"},
        ],
        value="crespo_hernandez",
        id="radio-turbulence",
    ),
])

combination_radio = dbc.FormGroup([
    dbc.Label("Combination"),
    dbc.RadioItems(
        options=[
            {"label": "SOSFS", "value": "sosfs"},
            {"label": "FLS", "value": "fls"},
        ],
        value="sosfs",
        id="radio-combination",
    ),
])

velocity_datatable = dt.DataTable(
    id = 'velocity-parameter-datatable',
    editable=True,
    style_cell={'overflow': 'hidden','textOverflow': 'ellipsis','maxWidth': 0}
)

deflection_datatable = dt.DataTable(
    id = 'deflection-parameter-datatable',
    editable=True,
    style_cell={'overflow': 'hidden','textOverflow': 'ellipsis','maxWidth': 0}
)

turbulence_datatable = dt.DataTable(
    id = 'turbulence-parameter-datatable',
    editable=True,
    style_cell={'overflow': 'hidden','textOverflow': 'ellipsis','maxWidth': 0}
)

layout = html.Div(
    dbc.Card(
        [
            dbc.CardHeader(
                    html.H2(
                        dbc.Button(
                            "Define the wake model:",
                            color="link",
                            id="collapse-model-button",
                        )
                    )
            ),
            dbc.Collapse(
                    dbc.CardBody(
                        dbc.Row([
                            dbc.Col( velocity_radio),
                            dbc.Col( deflection_radio),
                            dbc.Col( turbulance_radio ),
                            dbc.Col( combination_radio),
                        ]),
                    ),
                    id="collapse-models",
                    is_open=True,
            ),
            dbc.CardHeader(
                    html.H2(
                        dbc.Button(
                            "Wake model parameters:",
                            color="link",
                            id="collapse-parameter-button",
                        )
                    )
            ),
            dbc.Collapse(
                    dbc.CardBody(
                        dbc.Row([
                            dbc.Col( velocity_datatable, width=3,),
                            dbc.Col( deflection_datatable, width=3),
                            dbc.Col( turbulence_datatable, width=3),
                            dbc.Col( width=3,),
                        ]),
                    ),
                    id="collapse-parameters",
                    is_open=True,
            ),
        ],
        className="mt-3",
    )
)
