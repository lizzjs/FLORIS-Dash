#Combining Tabs with callback and slider (input and slider not interacting)
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

from app import app
# from apps import model_builder #, app2
from apps.model_builder import turbine, farm

# floris_dictionary = {
#     "logging": {}
# }

# Initialize with the first page layout and dynamically set in routing table
# app.layout = main_layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return turbine.layout
    if pathname == '/builder/turbine':
        return turbine.layout
    elif pathname == '/builder/farm':
        return farm.layout
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)
