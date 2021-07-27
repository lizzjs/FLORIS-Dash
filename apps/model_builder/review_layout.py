
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import apps.floris_data

# Imported but not used. This loads the callback functions into the web page.
import apps.model_builder.review_callbacks


submit_button = html.Div([
    dbc.ListGroupItem(
        dbc.Button("Submit", id="submit-floris-button", block=True, color="primary", href="/aep-results"),
    ),
])

layout = html.Div([
    dbc.Row([
        dbc.Col(
            children=[
                submit_button,
                dbc.Card(
                    dbc.CardBody(
                        html.Pre(id="json-preformatted")
                    ),
                    style={
                        # "maxHeight": "1587px",
                        "overflow": "scroll"
                    },
                ),
            ], width=4
        ),
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    dcc.Graph(id='review-windrose-graph'),
                    dcc.Graph(id='review-wind-farm-layout'),
                    dcc.Graph(id='review-cp-comparison-graph'),
                    dcc.Graph(id='review-ct-comparison-graph'),
                ]),
            ),
        ], width=6)
    ],justify="center")
])
