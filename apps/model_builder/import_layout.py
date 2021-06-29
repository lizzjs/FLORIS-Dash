
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


import_json_card = dbc.Card(
    dbc.CardBody([
        html.H4("Import FLORIS input file", className="card-title"),
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
        dbc.Spinner(html.Div(id="jloading-output")), 
    ]), className="mb-3", style={'height': "160px", 'padding': '5px'}
)

continue_card = dbc.Card(
    dbc.CardBody([
        html.H4("Getting started", className="card-title"),
        html.P("Begin the Model Builder with no prepopulated data and enter all parameters directly."),
        dbc.Button("Continue", color="primary", href="/build/windrose"),
    ]), style={'height': "150px", 'padding': '20px'}
)

dashboard_card = dbc.Card(
    dbc.CardBody([
        html.H4("Review and analyze results", className="card-title"),
        html.P("After importing, skip model builder and view results."),
        dbc.Button("Continue", color="primary", href="/build/review"),
    ]), style={'height': "150px", 'padding': '20px'}
)

layout = html.Div(
    dbc.Row([
        dbc.Col(
            [   
                import_json_card,
                dashboard_card,
            ], width=6),
        dbc.Col(continue_card, width=6)
    ])
)