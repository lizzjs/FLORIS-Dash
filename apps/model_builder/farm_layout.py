
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Card import Card
import dash_core_components as dcc
import dash_html_components as html
import dash_table

# Imported but not used. This loads the callback functions into the web page.
import apps.model_builder.farm_callbacks

layout_table = dash_table.DataTable(
    id = 'farm-layout-datatable',
    editable=True,
    style_table={'height': '300px', 'overflowY': 'auto'},
)

boundary_table = dash_table.DataTable(
    id = 'boundary-layout-datatable',
    editable=True,
    style_table={'height': '300px', 'overflowY': 'auto'}
)

farm_layout_inputs = dbc.Card(
    dbc.CardBody([
        html.H3("Wind farm layout.", className="card-text"),
        dbc.Row([
            dbc.Col(
                [
                    html.H6("Boundary data", className="card-text"),
                    boundary_table,
                    html.H6("Farm data", className="card-text"),
                    layout_table
                ], width=3
            ),
            dbc.Col([dcc.Graph(id="farm-layout-graph")], )
        ])
    ]),
    className="mt-3",
)

layout = html.Div([farm_layout_inputs])
