
from typing import Text
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

# Imported but not used. This loads the callback functions into the web page.
import apps.home_callbacks

import_json_card = dbc.Card(
    dbc.CardBody([
        html.H4("Import FLORIS input file", className="card-title"),
        html.P("Select a JSON file to prepopulate the Model Builder."),
        dbc.Row([
            dbc.Col(
                dcc.Upload(
                    dbc.Button( "Select File", color="primary" ),
                    id='json-upload-input-file',
                ),
                width=3
            ),
            dbc.Col(
                dbc.Label(
                    "No input file selected.",
                    id="label-input-file"
                ),
                width=9
            )
        ]),
        html.Br(),
        dbc.Row([
            dbc.Col(
                dbc.Button(
                    "Continue",
                    id="button-start-model-builder",
                    color="primary",
                    href="/build/windrose",
                    disabled=True
                ),
                width=3
            ),
            dbc.Col(
                dbc.Button(
                    "Skip to Review",
                    id="button-skip-to-review",
                    color="primary",
                    href="/build/review",
                    disabled=True
                ),
                width=3
            )
        ]),
    ]),
    className="mb-3",
)

fresh_start_card = dbc.Card(
    dbc.CardBody([
        html.H4("Start with defaults", className="card-title"),
        html.P("Load example input data into the Model Builder."),
        dbc.Button("Continue", color="primary", href="/build/windrose"),
    ]),
    className="mb-3",
)

dashboard_card = dbc.Card(
    dbc.CardBody([
        html.H4("Review and analyze results", className="card-title"),
        html.P("After importing, skip model builder and view results."),
        dbc.Button("Continue", color="primary", href="/build/review"),
    ]),
    className="mb-3",
)

layout = html.Div([
    dbc.Row(
        dbc.Col(
            html.P(
                "FLORIS is a wake modeling software well suited for the investigation of wake \
                    effects in a wind farm. Some use cases are quickly comparing wake models, \
                    performing wind farm controls optimization for yaw settings, and studying \
                    layout optimizations during wind farm design. \
                This web-based interface allows users to create a basic FLORIS simulation, \
                execute the software, and inspect results via the browser. \
                "
            ),
        )
    ),
    
    dbc.Row([
        dbc.Col([
            fresh_start_card,
        ]),
        dbc.Col([
            import_json_card
        ])
    ]),
    # dbc.Row( dbc.Col( dashboard_card ) ),
])
