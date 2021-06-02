# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# import dash
# import dash_core_components as dcc
# import dash_html_components as html

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# app.layout = html.Div([
#     html.Label('Dropdown'),
#     dcc.Dropdown(
#         options=[
#             {'label': 'New York City', 'value': 'NYC'},
#             {'label': u'Montréal', 'value': 'MTL'},
#             {'label': 'San Francisco', 'value': 'SF'}
#         ],
#         value='MTL'
#     ),

#     html.Label('Multi-Select Dropdown'),
#     dcc.Dropdown(
#         options=[
#             {'label': 'New York City', 'value': 'NYC'},
#             {'label': u'Montréal', 'value': 'MTL'},
#             {'label': 'San Francisco', 'value': 'SF'}
#         ],
#         value=['MTL', 'SF'],
#         multi=True
#     ),

#     html.Label('Radio Items'),
#     dcc.RadioItems(
#         options=[
#             {'label': 'New York City', 'value': 'NYC'},
#             {'label': u'Montréal', 'value': 'MTL'},
#             {'label': 'San Francisco', 'value': 'SF'}
#         ],
#         value='MTL'
#     ),

#     html.Label('Checkboxes'),
#     dcc.Checklist(
#         options=[
#             {'label': 'New York City', 'value': 'NYC'},
#             {'label': u'Montréal', 'value': 'MTL'},
#             {'label': 'San Francisco', 'value': 'SF'}
#         ],
#         value=['MTL', 'SF']
#     ),

#     html.Label('Text Input'),
#     dcc.Input(value='MTL', type='text'),

#     html.Label('Slider'),
#     dcc.Slider(
#         min=0,
#         max=9,
#         marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
#         value=5,
#     ),
# ], style={'columnCount': 2})

# if __name__ == '__main__':
#     app.run_server(debug=True)

##############################################################
# Interactive slider with input that can control slider and vice versa
# import dash
# from dash.dependencies import Input, Output
# import dash_core_components as dcc
# import dash_html_components as html

# external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# app.layout = html.Div(
#     [
#         dcc.Slider(
#             id="slider-circular", min=0, max=20, 
#             marks={i: str(i) for i in range(21)}, 
#             value=3
#         ),
#         dcc.Input(
#             id="input-circular", type="number", min=0, max=20, value=3
#         ),
#     ]
# )
# @app.callback(
#     Output("input-circular", "value"),
#     Output("slider-circular", "value"),
#     Input("input-circular", "value"),
#     Input("slider-circular", "value"),
# )
# def callback(input_value, slider_value):
#     ctx = dash.callback_context
#     trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
#     value = input_value if trigger_id == "input-circular" else slider_value
#     return value, value

# if __name__ == '__main__':
#     app.run_server(debug=True)

##############################################################
# Simple slider without styling marks 
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output
# import dash

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# app.layout = html.Div([
#     dcc.Slider(id='slider-drag'),
#     html.Div(id='slider-drag-output', style={'margin-top': 20})
# ])


# @app.callback(Output('slider-drag-output', 'children'),
#               [Input('slider-drag', 'drag_value'), Input('slider-drag', 'value')])
# def display_value(drag_value, value):
#     return 'drag_value: {} | value: {}'.format(drag_value, value)


# if __name__ == '__main__':
#     app.run_server(debug=True)

##############################################################

#Drag slider + Input (Modified)
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output
# import dash

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# app.layout = html.Div([
#     dcc.Input(
#         id='num-multi',
#         type='number',
#         value=5
#     ),
#     dcc.Slider(id='slider-drag'),
#     html.Div(id='slider-drag-output', style={'margin-top': 20})
# ])


# @app.callback(Output('slider-drag-output', 'children'),
#             # Output('slider-drag', 'children'),
#               [Input('slider-drag', 'drag_value'), Input('slider-drag', 'value')])
#             #   [Input('slider-drag', 'drag_value')])

# def display_value(drag_value, value):            
# # def display_value(drag_value):
#     return 'drag_value: {} | value: {}'.format(drag_value, value)
#     # return 'drag_value: {}'.format(drag_value)


# if __name__ == '__main__':
#     app.run_server(debug=True)

##############################################################
# Tabs for Turbine Geometry and Cp/CT Table
# import dash
# import dash_html_components as html
# import dash_core_components as dcc

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# app.layout = html.Div([
#     dcc.Tabs([
#         dcc.Tab(label='Geometry', children=[
#             dcc.Graph(
#                 figure={
#                     'data': [
#                         {'x': [1, 2, 3], 'y': [4, 1, 2],
#                             'type': 'bar', 'name': 'SF'},
#                         {'x': [1, 2, 3], 'y': [2, 4, 5],
#                          'type': 'bar', 'name': u'Montréal'},
#                     ]
#                 }
#             )
#         ]),
#         dcc.Tab(label='Cp/Ct Table', children=[
#             dcc.Graph(
#                 figure={
#                     'data': [
#                         {'x': [1, 2, 3], 'y': [1, 4, 1],
#                             'type': 'bar', 'name': 'SF'},
#                         {'x': [1, 2, 3], 'y': [1, 2, 3],
#                          'type': 'bar', 'name': u'Montréal'},
#                     ]
#                 }
#             )
#         ]),
#     ])
# ])


# if __name__ == '__main__':
#     app.run_server(debug=True)

################################################################
#Combining Tabs with callback and slider (input and slider not interacting)
import dash
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Tabs(id='tabs-example', value='tab-1', children=[
        dcc.Tab(label='Geometry', children=[
            dcc.Slider(
                id="slider-circular", min=0, max=20, 
                marks={i: str(i) for i in range(21)}, 
                value=3
            ),
            dcc.Input(
                id="input-circular", type="number", min=0, max=20, value=3
            ),
        ]),
        dcc.Tab(label='Cp/Ct Table', children=[
            dcc.Graph(
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [1, 4, 1],
                            'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [1, 2, 3],
                         'type': 'bar', 'name': u'Montréal'},
                    ]
                }
            )
        ]),
    ]),
])

@app.callback(Output('input-circular', 'value'),
              Output('slider-circular', 'value'),
                Input('input-circular', 'value'),
                Input('slider-circular', 'value'))
            
def GeometryTab_output(input_value, slider_value):
    # if tab == 'Geometry':
            ctx = dash.callback_context
            trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
            value = input_value if trigger_id == "input-circular" else slider_value
            print(input_value, slider_value, value)
            print(ctx.triggered)
            return value, value
    # elif tab == 'Cp/Ct Table':
        # ])


if __name__ == '__main__':
    app.run_server(debug=True)
