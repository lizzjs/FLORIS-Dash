
# import dash
# import dash_bootstrap_components as dbc
# import dash_html_components as html
# from dash.dependencies import Input, Output, State
# from app import app
# import apps.floris_data
# from floris.tools.floris_interface import FlorisInterface

# @app.callback(
#     Output("card-content", "children"), [Input("card-tabs", "active_tab")]
# )
# def dashboard_redirecting(active_tab):
#     pass

# @app.callback(
#     Output("card-content", "children"), [Input("card-tabs", "active_tab")]
# )
# def tab_content(active_tab):
#     return "This is tab {}".format(active_tab)

# @app.callback(
#     Output("collapse1-contents", "is_open"),
#     Input("collapse1-button", "n_clicks"),
#     State("collapse1-contents", "is_open"),
# )
# def toggle_accordion(n1, is_open1):
#     ctx = dash.callback_context
#     trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
#     if trigger_id == "collapse1-button":
#         is_open1 = not is_open1

#     return is_open1