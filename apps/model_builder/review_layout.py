
import dash_bootstrap_components as dbc
import dash_html_components as html
import json

import apps.floris_data

# Imported but not used. This loads the callback functions into the web page.
import apps.model_builder.review_callbacks


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
        dbc.Button("Submit", id="submit-floris-button", block=True, color="primary", href="/aep-results"),
    )
    # dbc.Spinner(html.Div(id="loading-output")),
])

layout = dbc.Container([
    dbc.Card(
        dbc.CardBody(display_json),
        style={"maxHeight": "550px","overflow": "scroll"},
    ),
    submit_button,
])
