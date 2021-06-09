
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

# Imported but not used. This loads the callback functions into the web page.
import apps.model_builder.atmos_cond_callbacks


atmos_cond_inputs = dbc.Card(
    dbc.CardBody(
        [
            html.H3("Define the atmospheric conditions.", className="card-text"),

            dbc.Row(
                [
                    dbc.Col(
                        [
                            # html.H5("Import Spreadsheet", className="card-title"),
                            html.H5("Import spreadsheet atomospheric conditions", className="card-title"),
                            html.P("Import spreadsheet atomospheric conditions."),
                            dcc.Upload(
                                id='wind-upload-data', 
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
                            html.Div(id='wind-table-data-output'),
                        ]
                    ),
                    dbc.Col(
                        [
                            dcc.Graph(id="wind-rose-chart")
                        ]
                    )
                ]
            )
        ]
    ),
    className="mt-3",
)

layout = html.Div([atmos_cond_inputs])