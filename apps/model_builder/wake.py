
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

# Imported but not used. This loads the callback functions into the web page.
import apps.model_builder.atmos_cond_callbacks


velocity_radio = dbc.FormGroup(
    [
        dbc.Label("Velocity deficit"),
        dbc.RadioItems(
            options=[
                {"label": "Jensen", "value": 1},
                {"label": "Multizone", "value": 2},
                {"label": "Gauss", "value": 3},
            ],
            value=1,
            id="radioitems-input1",
        ),
    ]
)

deflection_radio = dbc.FormGroup(
    [
        dbc.Label("Deflection"),
        dbc.RadioItems(
            options=[
                {"label": "Jimenez", "value": 1},
                {"label": "Gauss", "value": 2},
            ],
            value=1,
            id="radioitems-input2",
        ),
    ]
)

turbulance_radio = dbc.FormGroup(
    [
        dbc.Label("Turbulence"),
        dbc.RadioItems(
            options=[
                {"label": "Crespo-Hernandez", "value": 1},
            ],
            value=1,
            id="radioitems-input3",
        ),
    ]
)
combination_radio = dbc.FormGroup(
    [
        dbc.Label("Combination"),
        dbc.RadioItems(
            options=[
                {"label": "SOSFS", "value": 1},
                {"label": "FLS", "value": 2},
            ],
            value=1,
            id="radioitems-input4",
        ),
    ]
)

layout = html.Div([
    dbc.Card(
    dbc.CardBody(
        [
            html.H3("Define the wake model.", className="card-text"),

            dbc.Row(
                [
                    dbc.Col( children=[
                        velocity_radio,
                        html.Div(id='display-selected-values1')]
                    ),
                    dbc.Col( children=[
                        deflection_radio,
                        html.Div(id='display-selected-values2')]
                    ),
                    dbc.Col( children=[
                        turbulance_radio,
                        html.Div(id='display-selected-values3')]
                    ),
                    dbc.Col( children=[
                        combination_radio,
                        html.Div(id='display-selected-values4')]
                    ),
                ]
            ),
        ]
    ),
    className="mt-3",
)

])