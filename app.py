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
            dcc.Input(
                id="input-hubheight", type="number", min=0, max=20, value=3
            ),
            dcc.Slider(
                id="slider-hubheight", min=0, max=20, 
                marks={i: str(i) for i in range(21)}, 
                value=3
            ),
            dcc.Input(
                id="input-rotordiam", type="number", min=0, max=20, value=3
            ),
            dcc.Slider(
                id="slider-rotordiam", min=0, max=20, 
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
@app.callback(Output('input-rotordiam', 'value'),
              Output('slider-rotordiam', 'value'),
                Input('input-rotordiam', 'value'),
                Input('slider-rotordiam', 'value'))
            
def GeomTab_hubheight_output(input_value, slider_value):
    # if tab == 'Geometry':
            ctx = dash.callback_context
            trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
            value = input_value if trigger_id == "input-hubheight" else slider_value
            print(input_value, slider_value, value)
            print(ctx.triggered)
            return value, value
    # elif tab == 'Cp/Ct Table':
        # ])
def GeomTab_rotordiam_output(input_value, slider_value):
    # if tab == 'Geometry':
            ctx = dash.callback_context
            trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
            value = input_value if trigger_id == "input-rotordiam" else slider_value
            print(input_value, slider_value, value)
            print(ctx.triggered)
            return value, value
    # elif tab == 'Cp/Ct Table':
        # ])


if __name__ == '__main__':
    app.run_server(debug=True)