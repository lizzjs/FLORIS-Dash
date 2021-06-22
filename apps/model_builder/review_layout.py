import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table

import apps.model_builder.review_callbacks
import apps.floris_data
from pandas import DataFrame
import json

display_json = html.Div(
    json.dumps(
        apps.floris_data.user_defined_dict,
        indent = 4, 
        # sort_keys=True
        ),
    style={'whiteSpace': 'pre-line'}
)

submit_button = html.Div([
    dbc.ListGroupItem(
        dbc.Button("Submit", id="submit-button", block=True,color="primary", href="/dashboard/aep"),
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