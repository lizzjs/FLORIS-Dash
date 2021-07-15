
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
    style_table={'overflowY': 'auto', 'maxHeight':'550px'},
)

boundary_table = dash_table.DataTable(
    id='boundary-layout-datatable',
    editable=True,
    row_deletable=True,
    style_table={'overflowY': 'auto', 'maxHeight':'550px'}
)

layout = html.Div(
    children=[
        html.H3("Farm Definition"),
        html.Br(),
        dbc.Card([
            dbc.CardBody(
                dbc.Row([
                    dbc.Col(
                        children=[
                            html.H5("Wind turbine locations"),
                            dbc.Button("Add row", id="button-add-layout-row", className='mb-3 btn-sm', n_clicks=0),
                            layout_table,
                        ],
                    ),
                    dbc.Col(
                        children=[
                            html.H5("Boundary points"),
                            html.Br(),
                            boundary_table
                        ],
                    ),
                    dbc.Col(
                        children=[
                            dbc.Card([
                                dbc.CardHeader("Layout Visualization"),
                                dbc.CardBody(dcc.Graph(id='farm-layout-graph')),
                            ])
                        ],
                        width=7
                    ),
                ])
            )
        ])
    ]
)
