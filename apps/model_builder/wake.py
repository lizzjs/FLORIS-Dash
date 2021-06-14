
import dash_bootstrap_components as dbc
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
        value="crespo",
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

layout = html.Div([
    dbc.Card(
        dbc.CardBody([
            html.H3("Define the wake model.", className="card-text"),
            dbc.Row([
                dbc.Col( velocity_radio ),
                dbc.Col( deflection_radio ),
                dbc.Col( turbulance_radio ),
                dbc.Col( combination_radio )
            ]),
        ]),
        className="mt-3",
    )
])
