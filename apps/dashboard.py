
# import dash_bootstrap_components as dbc
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output

# from app import app
# from apps.model_builder import turbine, farm, home, atmos_cond, wake, review
# from apps.floris_connection.run_floris import calculate_wake
# import apps.floris_data


# sidebar_style = {
#     # "position": "fixed",
#     "top": 200,
#     "left": 0,
#     "bottom": 0,
#     "width": "23.5rem",
#     "padding": "2rem 1rem",
#     "background-color": "#f8f9fa",
# }

# sidebar = html.Div(
#     [
#         dbc.Button("Back", id="back-button", color="primary", href="/calculate"),
#         html.H2("Parameters", className="display-4"),
#         html.Hr(),
        
#     ],
#     style=sidebar_style,
# )

# collapse_1=dbc.Card(
#         [
#             dbc.CardHeader(
#                     html.H2(
#                         dbc.Button(
#                             "Parameter 1",
#                             # color="link",
#                             id="collapse1-button",
#                         )
#                     )
#             ),
#             dbc.Collapse(
#                     dbc.CardBody(
#                         dbc.Row([
#                             html.Div("Some interactive sliders or inputs")
#                         ]),
#                     ),
#                     id="collapse1-contents",
#                     is_open=True,
#             ),
#         ]
# )

# tabs = dbc.Card(
#     [
#         dbc.CardHeader(
#             dbc.Tabs(
#                 [
#                     dbc.Tab([collapse_1],
#                         label="Tab 1", 
#                         tab_id="tab-1",
#                         ),
#                     dbc.Tab(label="Tab 2", tab_id="tab-2"),
#                 ],
#                 id="card-tabs",
#                 card=True,
#                 active_tab="tab-1",
#             )
#         ),
#         dbc.CardBody(html.P(id="card-content", className="card-text")),
#     ]
# )

# layout = dbc.Container(
#     [
#         dbc.Row(
#             dbc.Col(
#                 # dbc.Jumbotron( html.H1("FLORIS Dashboard", className="display-3") )
#             )
#         ),
#         dbc.Row([
#             # Progress tracker
#             dbc.Col([
                
#             ], width=2),

#             # Content area
#             dbc.Col(id="page-content")
#         ]),
#         dcc.Location(id='url', refresh=False),
#         dcc.Store(id='floris-inputs'),
#     ],
#     fluid=True,
# )