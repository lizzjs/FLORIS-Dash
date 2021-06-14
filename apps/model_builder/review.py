import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table

import apps.model_builder.review_callbacks
from apps.floris_inputs import default_input_dict
from pandas import DataFrame
import json

display_json = html.Div(
    json.dumps(
        default_input_dict, 
        indent = 4, 
        # sort_keys=True
        ),
    style={'whiteSpace': 'pre-line'}
)

submit_button = html.Div([
    dbc.ListGroupItem(
        dbc.Button("Submit", id="loading-button", block=True,color="primary", href="/calculate"),
    )
    # dbc.Spinner(html.Div(id="loading-output")),
])

# dbc.ListGroupItem( dbc.Button("Submit", color="primary", href="/builder/farm") ),

layout = dbc.Container([
    dbc.Card(
        dbc.CardBody(
            [
            display_json,
        ]),
        style={"maxHeight": "550px","overflow": "scroll"},
    ),

        submit_button,

])