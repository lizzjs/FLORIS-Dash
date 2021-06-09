
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table

import apps.model_builder.home_callbacks

import_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Import Spreadsheet", className="card-title"),
            html.P("Import spreadsheet with turbine, farm, atomospheric conditions, and wake model parameters?"),
            dcc.Upload(
                id='home-upload-data', 
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
            html.P(
                "Here you can use the model builder to directly input"
                "the FLORIS parameters to populate the dictionary."
            ),
            dbc.Button("Continue", color="primary", href="/build/turbine"),
        ]
    )
)

cards = dbc.Row([dbc.Col(import_card, width=4), dbc.Col(continue_card, width=8)])

layout = html.Div([
            cards,
            html.Div(id='editing-table-data-output'),
        ])