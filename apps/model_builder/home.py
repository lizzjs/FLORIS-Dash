
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table

from pandas import DataFrame


import_json_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Import JSON file", className="card-title"),
            html.P("Import JSON file with turbine, farm, atomospheric conditions, and wake model parameters."),
            dcc.Upload(
                id='json-upload-input-file', 
                children=[dbc.Button("Select File", color="primary")],
                style={
                    # 'width': '20%',
                    # 'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    # 'margin': '10px'
                },
                # Allow multiple files to be uploaded
                multiple=True #change to true if you want multiple files 
            ),
            
        ]
    )
)

continue_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Getting started", className="card-title"),
            html.P("Begin the Model Builder with no prepopulated data and enter all parameters directly."),
            dbc.Button("Continue", color="primary", href="/build/turbine"),
        ]
    )
)

cards = dbc.Row(
    [
        dbc.Col(import_json_card, width=5),
        dbc.Col(continue_card, width=7)
    ]
)

datatable=dbc.Row(
    [   
        dash_table.DataTable(
            id = 'homepage-datatable',
            data=[],
            columns=[],
            style_table={'height': '300px', 'overflowY': 'auto'},
        )
    ]
)

layout = dbc.Card(
        dbc.CardBody(
            [
                html.Div([
                    cards,
                    datatable,
                ])
            ]
        )
    )