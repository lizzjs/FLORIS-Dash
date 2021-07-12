
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

CONTENT_STYLE = {
    # "margin-left": "18.5rem",
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
