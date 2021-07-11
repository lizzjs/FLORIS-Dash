
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


import_json_card = dbc.Card(
    dbc.CardBody([
        html.H4("Import FLORIS input file", className="card-title"),
        html.P("Select a JSON file with turbine, farm, atomospheric conditions, and wake model definitions."),
        dcc.Upload(
            dbc.Button(
                "Select File",
                color="primary",
                id="jupload-button"
            ),
            id='json-upload-input-file',
        ),
        dbc.Spinner(
            html.Div(id="jloading-output")
        ),
    ]),
    className="mb-3",
)

continue_card = dbc.Card(
    dbc.CardBody([
        html.H4("Getting started", className="card-title"),
        html.P("Begin the Model Builder with no prepopulated data and enter all parameters directly."),
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
    dbc.Row( dbc.Col( import_json_card ) ),
    dbc.Row( dbc.Col( dashboard_card ) ),
    dbc.Row( dbc.Col( continue_card ) ),
])
