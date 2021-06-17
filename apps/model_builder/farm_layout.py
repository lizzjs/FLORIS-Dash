
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table

# Imported but not used. This loads the callback functions into the web page.
import apps.model_builder.farm_callbacks

layout_table = dash_table.DataTable(
    id = 'farm-layout-datatable',
    editable=True,
    style_table={'height': '600px', 'overflowY': 'auto'},
)

boundary_input = html.Div(
    children=[
        dcc.Textarea(
            id='textarea-boundary',
            placeholder='Insert boundary points here',
            style={'width': '100%', 'height': 200},
        ),
        html.Button('Submit', 
            id='textarea-boundary-button', 
            n_clicks=0,
            style={'margin': '10px'}
        ),
    ]
)

farm_layout_inputs = dbc.Card(
    dbc.CardBody([
        html.H3("Wind farm layout.", className="card-text"),
        dbc.Row([
            dbc.Col(
                [
                    boundary_input,
                    layout_table
                ],width=3 
            ),
            dbc.Col( dcc.Graph(id="farm-layout-graph") )
        ])
    ]),
    className="mt-3",
)

layout = html.Div([farm_layout_inputs])
