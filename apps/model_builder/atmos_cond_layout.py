
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table

# Imported but not used. This loads the callback functions into the web page.
import apps.model_builder.atmos_cond_callbacks

wind_rose_table = dash_table.DataTable(
    id = 'wind-rose-datatable',
    editable=True,
    row_deletable=True,
    style_table={'height': '600px', 'overflowY': 'auto'},
)

wind_rose_graph = dcc.Graph(id="wind-rose-graph")

layout = html.Div(
    children=[
        html.H3("Wind Rose"),
        html.Br(),
        dbc.Card([
            dbc.CardBody(
                dbc.Row([
                    dbc.Col(
                        children=[
                            wind_rose_table
                        ],
                        width=4
                    ),
                    dbc.Col(
                        children=[
                            wind_rose_graph
                        ],
                    )
                ])
            )
        ])
    ]
)
