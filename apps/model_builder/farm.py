
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

# Imported but not used. This loads the callback functions into the web page.
import apps.model_builder.farm_callbacks

farm_layout_inputs = dbc.Card(
    dbc.CardBody(
        [
            html.H3("Define the wind farm layout.", className="card-text"),

            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Textarea(
                                id='textarea-farm-layout',
                                placeholder='Paste farm layout points here',
                                style={'width': '100%', 'height': 300},
                            ),
                            html.Button('Submit', 
                                id='textarea-farm-layout-button', 
                                n_clicks=0,
                                style={'margin': '10px'}
                            ),
                        ],
                        width=3
                    ),

                    dbc.Col(
                        [
                            dcc.Graph(id="farm-graph")
                        ]
                    )
                    
                ]
            )
        ]
    ),
    className="mt-3",
)

layout = html.Div([farm_layout_inputs])
