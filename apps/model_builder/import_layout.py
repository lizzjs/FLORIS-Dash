
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


import_json_card = dbc.Card(
    dbc.CardBody([
        html.H5("Import FLORIS input file", className="card-title"),
        html.P("Select a JSON file with turbine, farm, atomospheric conditions, and wake model definitions."),
        dcc.Upload(
            id='json-upload-input-file', 
            children=dbc.Button("Select File", color="primary", id="jupload-button"),
            style={
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
            },
        ),
        dbc.Spinner(html.Div(id="jloading-output")), #We can remove dbc.Spinner if we dont use it, and remove the time.sleep(1) in the callback
    ])
)

continue_card = dbc.Card(
    dbc.CardBody([
        html.H5("Getting started", className="card-title"),
        html.P("Begin the Model Builder with no prepopulated data and enter all parameters directly."),
        dbc.Button("Continue", color="primary", href="/build/windrose"),
    ])
)

layout = html.Div(
    dbc.Row([
        dbc.Col(import_json_card, width=6),
        dbc.Col(continue_card, width=6)
    ])
)