
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table

import apps.model_builder.home_callbacks
from pandas import DataFrame

import_spreadsheet_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Import Spreadsheet", className="card-title"),
            html.P("Import spreadsheet with turbine, farm, atomospheric conditions, and wake model parameters."),
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

import_json_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Import JSON file", className="card-title"),
            html.P("Import JSON file with turbine, farm, atomospheric conditions, and wake model parameters."),
            dcc.Upload(
                id='json-upload-data', 
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

cards = dbc.Row(
    [
        dbc.Col( children=[
            import_spreadsheet_card,
            import_json_card], 
            width=5
        ),
        dbc.Col(
            continue_card, width=7
        )
    ]
)

dummy_df = DataFrame({})
table =dbc.Row(
    [   
        dash_table.DataTable(
            id = 'homepage-datatable',
            data=dummy_df.to_dict("rows"),
            columns=[{"name": i, "id": i} for i in dummy_df.columns],
            style_table={'height': '300px', 'overflowY': 'auto'},
        )
    ]
)

layout = dbc.Card(
        dbc.CardBody(
            [
                html.Div([
                    cards,
                    table,
                    html.Div(id='editing-table-data-output'),
                ])
            ]
        )
    )