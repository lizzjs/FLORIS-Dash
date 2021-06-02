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
                #Hub Height
                    dcc.Input(id="input-hubheight", type="number", min=0, max=20, value=3
                    ),
                    dcc.Slider(
                        id="slider-hubheight", min=0, max=20, 
                        marks={i: str(i) for i in range(21)}, 
                        value=3
                    ),
                #Rotor Diameter
                    dcc.Input(
                        id="input-rotordiam", type="number", min=0, max=20, value=3
                    ),
                    dcc.Slider(
                        id="slider-rotordiam", min=0, max=20, 
                        marks={i: str(i) for i in range(21)}, 
                        value=3
                    ),
                #Tilt Angle
                    dcc.Input(
                        id="input-tiltang", type="number", min=0, max=20, value=3
                    ),
                    dcc.Slider(
                        id="slider-tiltang", min=0, max=20, 
                        marks={i: str(i) for i in range(21)}, 
                        value=3
                    ), 
                #Yaw Angle
                    dcc.Input(
                        id="input-yawang", type="number", min=0, max=20, value=3
                    ),
                    dcc.Slider(
                        id="slider-yawang", min=0, max=20, 
                        marks={i: str(i) for i in range(21)}, 
                        value=3
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

@app.callback(Output('input-hubheight', 'value'),
              Output('slider-hubheight', 'value'),
                Input('input-hubheight', 'value'),
                Input('slider-hubheight', 'value'))
            
def GeomTab_hubheight_output(input_value1, slider_value1):
            ctx = dash.callback_context
            trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
            value1 = input_value1 if trigger_id == "input-hubheight" else slider_value1
            print(input_value1, slider_value1, value1)
            print(ctx.triggered)
            return value1, value1

@app.callback(Output('input-rotordiam', 'value'),
              Output('slider-rotordiam', 'value'),
                Input('input-rotordiam', 'value'),
                Input('slider-rotordiam', 'value'))

def GeomTab_rotordiam_output(input_value, slider_value):
            ctx = dash.callback_context
            trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
            value = input_value if trigger_id == "input-rotordiam" else slider_value
            print(input_value, slider_value, value)
            print(ctx.triggered)
            return value, value

@app.callback(Output('input-tiltang', 'value'),
              Output('slider-tiltang', 'value'),
                Input('input-tiltang', 'value'),
                Input('slider-tiltang', 'value'))

def GeomTab_tiltang_output(input_value, slider_value):
            ctx = dash.callback_context
            trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
            value = input_value if trigger_id == "input-tiltang" else slider_value
            print(input_value, slider_value, value)
            print(ctx.triggered)
            return value, value

@app.callback(Output('input-yawang', 'value'),
              Output('slider-yawang', 'value'),
                Input('input-yawang', 'value'),
                Input('slider-yawang', 'value'))

def GeomTab_yawang_output(input_value, slider_value):
            ctx = dash.callback_context
            trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
            value = input_value if trigger_id == "input-yawang" else slider_value
            print(input_value, slider_value, value)
            print(ctx.triggered)
            return value, value

if __name__ == '__main__':
    app.run_server(debug=True)