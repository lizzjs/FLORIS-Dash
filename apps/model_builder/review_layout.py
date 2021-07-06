
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import json

import apps.floris_data

# Imported but not used. This loads the callback functions into the web page.
import apps.model_builder.review_callbacks


display_json = html.Pre(
    json.dumps(
        apps.floris_data.user_defined_dict,
        indent = 2, 
        # sort_keys=True
    ),
    # style={'whiteSpace': 'pre-line'}
)

submit_button = html.Div([
    dbc.ListGroupItem(
        dbc.Button("Submit", id="submit-floris-button", block=True, color="primary", href="/aep-results"),
    ),
    dbc.Spinner(html.Div(id="loading-output")),
])

layout = dbc.Container([
    dbc.Row([
        dbc.Col(
            [
                dbc.Card(
                    dbc.CardBody(display_json),
                    style={"maxHeight": "1785px","overflow": "scroll"},
                ),
                submit_button,
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
        ], width=7)
    ],justify="center")
])
