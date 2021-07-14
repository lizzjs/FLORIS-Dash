
import dash_bootstrap_components as dbc

import dash_core_components as dcc
import dash_html_components as html
import dash_table

# Imported but not used. This loads the callback functions into the web page.
import apps.model_builder.farm_callbacks

layout_table = dash_table.DataTable(
    id = 'farm-layout-datatable',
    editable=True,
    row_deletable=True,
    style_table={'overflowY': 'auto'},
)

boundary_table = dash_table.DataTable(
    id='boundary-layout-datatable',
    editable=True,
    row_deletable=True,
    style_table={'overflowY': 'auto'}
)

layout = html.Div(
    children=[
        html.H3("Farm definition"),
        html.Br(),
        dbc.Card([
            dbc.CardBody(
                dbc.Row([
                    dbc.Col(
                        children=[
                            html.H5("Wind turbine locations"),
                            dbc.Button("Add row", id="button-add-layout-row", n_clicks=0),
                            layout_table,
                        ],
                        width=3
                    ),
                    dbc.Col(
                        children=[
                            html.H5("Boundary points"),
                            boundary_table
                        ],
                        width=3
                    ),
                    dbc.Col(
                        children=[
                            dbc.Card([
                                dbc.CardHeader("Layout visualization"),
                                dbc.CardBody(dcc.Graph(id='farm-layout-graph')),
                            ])
                        ],
                        width=6
                    ),
                ])
            )
        ])
    ]
)
