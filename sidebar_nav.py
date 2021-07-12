
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app import app
from apps.model_builder import turbine_layout, farm_layout, atmos_cond_layout, wake_layout, review_layout  
from apps.dashboard import aep_layout
import apps.floris_data
from apps import home_layout

SIDEBAR_STYLE = {
    # "position": "fixed",
    # "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

SIDEBAR_HIDDEN = {
    # "position": "fixed",
    # "width": "16rem",
    "left": "-20rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

CONTENT_STYLE = {
    # "margin-left": "18.5rem",
    # "margin-right": "0rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

CONTENT_STYLE1 = {
    "left": "-16rem",
    # "margin-right": "0rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

NAVIGATION_ITEMS = [
    "/",
    "/build/windrose",
    "/build/turbine",
    "/build/farm",
    "/build/wakemodel",
    "/build/review",
    "/aep-results"
]

@app.callback(
    Output("sidebar", "style"),
    Output("page-content", "style"),
    Output("side_click", "data"),
    Input("btn_sidebar", "n_clicks"),
    State("side_click", "data"),
)
def toggle_sidebar(n, nclick):
    if n:
        if nclick == "SHOW":
            sidebar_style = SIDEBAR_HIDDEN
            content_style = CONTENT_STYLE1
            cur_nclick = "HIDDEN"
        else:
            sidebar_style = SIDEBAR_STYLE
            content_style = CONTENT_STYLE
            cur_nclick = "SHOW"
    else:
        sidebar_style = SIDEBAR_STYLE
        content_style = CONTENT_STYLE
        cur_nclick = 'SHOW'

    return sidebar_style, content_style, cur_nclick

def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

for i in [1,2,3]:
    app.callback(
        Output(f"submenu-{i}-collapse", "is_open"),
        [Input(f"submenu-{i}", "n_clicks")],
        [State(f"submenu-{i}-collapse", "is_open")],
    )(toggle_collapse)


@app.callback(
    Output('page-content', 'children'),
    Output('next-button', 'href'),
    Output('back-button', 'href'),
    Input('url', 'pathname'),
)
def display_page(pathname):
    """
    Args:
        pathname (str): current url of the website

    Return:
        html.Div: layout of the current page
        str: url of the next page for navigation button
    """
    if pathname not in NAVIGATION_ITEMS:
        layout = dbc.Jumbotron([
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognized..."),
            ])
        back_nav = NAVIGATION_ITEMS[0]
        next_nav = NAVIGATION_ITEMS[0]
        return layout, next_nav, back_nav
    elif pathname == '/':
        layout = home_layout.layout
        back_nav = NAVIGATION_ITEMS[0]
        next_nav = NAVIGATION_ITEMS[ NAVIGATION_ITEMS.index(pathname) + 1 ]
        return layout, next_nav, back_nav
    elif pathname == '/aep-results':
        layout = aep_layout.layout
        back_nav = NAVIGATION_ITEMS[ NAVIGATION_ITEMS.index(pathname) - 1 ]
        next_nav = NAVIGATION_ITEMS[0]
        return layout, next_nav, back_nav

    # TODO: REMOVE THIS
    apps.floris_data.user_defined_dict = apps.floris_data.default_input_dict
    back_nav = NAVIGATION_ITEMS[ NAVIGATION_ITEMS.index(pathname) - 1 ]
    next_nav = NAVIGATION_ITEMS[ NAVIGATION_ITEMS.index(pathname) + 1 ]

    if pathname == '/build/turbine':
        layout = turbine_layout.layout
    elif pathname == '/build/farm':
        layout = farm_layout.layout
    elif pathname == '/build/windrose':
        layout = atmos_cond_layout.layout
    elif pathname == '/build/wakemodel':
        layout = wake_layout.layout
    elif pathname == '/build/review':
        layout = review_layout.layout
    
    return layout, next_nav, back_nav
