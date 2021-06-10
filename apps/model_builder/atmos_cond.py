
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from pandas import DataFrame

# Imported but not used. This loads the callback functions into the web page.
import apps.model_builder.atmos_cond_callbacks


dummy_df = DataFrame({})

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
                            dash_table.DataTable(
                                id = 'wind-datatable-interactivity',
                                data=dummy_df.to_dict("rows"),
                                columns=[{"name": i, "id": i} for i in dummy_df.columns],
                                editable=True,
                                # cell_selectable=True,
                                # column_selectable="multi",  # allow users to select 'multi' or 'single' columns
                                # row_selectable="multi",     # allow users to select 'multi' or 'single' rows
                                # row_deletable=True,         # choose if user can delete a row (True) or not (False)
                                # selected_columns=[],        # ids of columns that user selects
                                # selected_rows=[],           # indices of rows that user selects
                                # page_action="none",         # all data is passed to the table up-front or not ('none')
                                style_table={'height': '300px', 'overflowY': 'auto'},
                            ),
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