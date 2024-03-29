
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_table as dt
import dash_html_components as html

# Imported but not used. This loads the callback functions into the web page.
import apps.model_builder.wake_callbacks


velocity_radio = dbc.FormGroup([
    dbc.Label("Velocity deficit"),
    dbc.RadioItems(
        options=[
            {"label": "Jensen", "value": "jensen"},
            {"label": "Multizone", "value": "multizone"},
            {"label": "Gauss", "value": "gauss"},
        ],
        value="jensen",
        id="radio-deficit",
    ),
])

deflection_radio = dbc.FormGroup([
    dbc.Label("Deflection"),
    dbc.RadioItems(
        options=[
            {"label": "Jimenez", "value": "jimenez"},
            {"label": "Gauss", "value": "gauss"},
        ],
        value="jimenez",
        id="radio-deflection",
    ),
])

turbulance_radio = dbc.FormGroup([
    dbc.Label("Turbulence"),
    dbc.RadioItems(
        options=[
            {"label": "Crespo-Hernandez", "value": "crespo_hernandez"},
        ],
        value="crespo_hernandez",
        id="radio-turbulence",
    ),
])

combination_radio = dbc.FormGroup([
    dbc.Label("Combination"),
    dbc.RadioItems(
        options=[
            {"label": "SOSFS", "value": "sosfs"},
            {"label": "FLS", "value": "fls"},
        ],
        value="sosfs",
        id="radio-combination",
    ),
])

velocity_datatable = html.Div(
    [
        dbc.Label(id="velocity-param-label"),
        dt.DataTable(
            id = 'velocity-parameter-datatable',
            editable=True,
            style_cell={'overflow': 'hidden','textOverflow': 'ellipsis','maxWidth': 0}
        )
    ]
)

deflection_datatable = html.Div(
    [
        dbc.Label(id="deflection-param-label"),
        dt.DataTable(
            id = 'deflection-parameter-datatable',
            editable=True,
            style_cell={'overflow': 'hidden','textOverflow': 'ellipsis','maxWidth': 0}
         )
    ]
)

turbulence_datatable = html.Div(
    [
        dbc.Label(id="turbulence-param-label"),
        dt.DataTable(
            id = 'turbulence-parameter-datatable',
            editable=True,
            style_cell={'overflow': 'hidden','textOverflow': 'ellipsis','maxWidth': 0}
        )
    ]
)

wake_options_collapse = dbc.Collapse(
    dbc.CardBody(
        dbc.Row([
            dbc.Col( velocity_radio),
            dbc.Col( deflection_radio),
            dbc.Col( turbulance_radio),
            dbc.Col( combination_radio),
        ]),
    ),
    id="collapse-models",
    is_open=True,
)
wake_parameters_collapse = dbc.Collapse(
    dbc.CardBody(
        dbc.Row(
            [
                dbc.Col( velocity_datatable, width=3),
                dbc.Col( deflection_datatable, width=3),
                dbc.Col( turbulence_datatable, width=3),
                dbc.Col(width=3)
            ], 
        ),
    ),
    id="collapse-parameters",
    is_open=True,
)

flow_field_preview_collapse = dbc.Collapse(
    dbc.CardBody(
        dbc.Row(
            dbc.Col( dcc.Graph(id="wake-model-preview-graph") )
        )
    ),
    id="collapse-preview",
    is_open=True,
)

collapse_layout = html.Div([
    dbc.Row(
        dbc.Col(
            dbc.Card([
                dbc.CardHeader(
                    [
                        dbc.Label("Model Options", className='mr-1'),
                        dbc.Button(
                            children=[
                                html.Img(
                                    src="/assets/carrot-arrow.png", 
                                    style={'width':'10px', 'align':'center'}
                                )
                            ], 
                            className="btn-light btn-sm", 
                            style={'width':'30px', 'height':'30px'},
                            id="collapse-model-button",
                        )
                    ]
                ),
                wake_options_collapse
            ])
        )
    ),
    html.Br(),
    dbc.Row(
        dbc.Col(
            dbc.Card([
                dbc.CardHeader(
                    [
                        dbc.Label("Model Paramters", className='mr-1'),
                        dbc.Button(
                            children=[
                                html.Img(
                                    src="/assets/carrot-arrow.png", 
                                    style={'width':'10px', 'align':'center'}
                                )
                            ], 
                            className="btn-light btn-sm", 
                            style={'width':'30px', 'height':'30px'},
                            id="collapse-parameter-button",
                        )
                    ]
                ),
                wake_parameters_collapse
            ])
        )
    ),
    html.Br(),
    dbc.Row(
        dbc.Col(
            dbc.Card([
                dbc.CardHeader(
                    [
                        dbc.Label("Flow Field Preview", className='mr-1'),
                            # dbc.Button(
                            #     children=[
                            #         html.Img(
                            #             src="/assets/carrot-arrow.png", 
                            #             style={'width':'10px', 'align':'center'}
                            #         )
                            #     ], 
                            #     className="btn-light btn-sm", 
                            #     style={'width':'30px', 'height':'30px'},
                            #     id="collapse-preview-button",
                            # )
                    ]
                ),
                flow_field_preview_collapse
            ])
        )
    )
])

layout = html.Div(
    children=[
        html.H3("Model Definition"),
        html.Br(),
        dbc.Card([
            dbc.CardBody(
                collapse_layout
            )
        ])
    ]
)