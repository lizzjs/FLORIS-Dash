#Combining Tabs with callback and slider (input and slider not interacting)
from os import path
import dash
# import dash_daq as daq
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import pandas as pd
import dash_table as dt
import plotly.express as px
import base64
import io
import plotly.graph_objs as go


from layout import main_layout

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {"graphBackground": "#F5F5F5", "background": "#ffffff", "text": "#000000"}

app.layout = main_layout

#TAB1-TSR
@app.callback(
    Output('TSR-numeric-input-output', 'children'),
    Input('input-TSR', 'value')
)
def GeomTab_TSR_output(input_value):
    # print(input_value)
    return input_value

#TAB1-Blade count
@app.callback(
    Output('updatemode-output-bladecount', 'children'),
    Input('slider-bladecount', 'value')
)
def GeomTab_bladecount_display_value(value):
    return 'Blades: {}'.format(value)

#TAB1-Blade pitch
@app.callback(
    Output('bladepitch-numeric-input-output', 'children'),
    Input('input-bladepitch', 'value')
)
def GeomTab_Bladepitch_output(input_value):
    # print(input_value)
    return input_value

#TAB1-Generator efficiency
@app.callback(
    Output('genEff-numeric-input-output', 'children'),
    Input('input-genEff', 'value')
)
def GeomTab_genEff_output(input_value):
    # print(input_value)
    return input_value

#TAB1-Hub height
@app.callback(
    Output('input-hubheight', 'value'),
    Output('slider-hubheight', 'value'),
    Input('input-hubheight', 'value'),
    Input('slider-hubheight', 'value')
)
def GeomTab_hubheight_output(input_value, slider_value):
    ctx = dash.callback_context
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
    value = input_value if trigger_id == "input-hubheight" else slider_value
    # print(input_value, slider_value, value)
    # print(ctx.triggered)
    return value, value

#TAB1-ngrid
@app.callback(
    Output('updatemode-output-ngrid', 'children'),
    Input('slider-ngrid', 'value')
)
def GeomTab_bladecount_display_value(value):
    return 'ngrid: {}'.format(value)

#TAB1-pP
@app.callback(
    Output('pP-numeric-input-output', 'children'),
    Input('input-pP', 'value')
)
def GeomTab_pP_output(input_value):
    # print(input_value)
    return input_value

#TAB1-pT
@app.callback(
    Output('pT-numeric-input-output', 'children'),
    Input('input-pT', 'value')
)
def GeomTab_pT_output(input_value):
    # print(input_value)
    return input_value

#TAB1-rloc
@app.callback(
    Output('rloc-numeric-input-output', 'children'),
    Input('input-rloc', 'value')
)
def GeomTab_rloc_output(input_value):
    # print(input_value)
    return input_value

#TAB1-Tilt angle
@app.callback(
    Output('input-tiltang', 'value'),
    Output('slider-tiltang', 'value'),
    Input('input-tiltang', 'value'),
    Input('slider-tiltang', 'value')
)
def GeomTab_tiltang_output(input_value, slider_value):
    ctx = dash.callback_context
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
    value = input_value if trigger_id == "input-tiltang" else slider_value
    # print(input_value, slider_value, value)
    # print(ctx.triggered)
    return value, value

#TAB1-Points on Perimeter
@app.callback(
    Output('radio-output', 'children'),
    [Input('radio-input', 'value')]
)
def GeomTab_radiobutton_value(value):
    if value == 1:
        value = True
    else:
        value = False
    # print(value)

#TAB1-Yaw angle
@app.callback(
    Output('input-yawang', 'value'),
    Output('slider-yawang', 'value'),
    Input('input-yawang', 'value'),
    Input('slider-yawang', 'value')
)
def GeomTab_yawang_output(input_value, slider_value):
    ctx = dash.callback_context
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
    value = input_value if trigger_id == "input-yawang" else slider_value
    # print(input_value, slider_value, value)
    # print(ctx.triggered)
    return value, value

#TAB1-Rotor Diameter
@app.callback(
    Output('input-rotordiam', 'value'),
    Output('slider-rotordiam', 'value'),
    Input('input-rotordiam', 'value'),
    Input('slider-rotordiam', 'value')
)
def GeomTab_rotordiam_output(input_value, slider_value):
    ctx = dash.callback_context
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
    value = input_value if trigger_id == "input-rotordiam" else slider_value
    # print(input_value, slider_value, value)
    # print(ctx.triggered)
    return value, value

#TAB2-Text input
@app.callback(
    Output('Mygraph1', 'figure'),
    Output('Mygraph2', 'figure'),
    Input('textarea-state-example-button', 'n_clicks'),
    Input('upload-data', 'filename'),
    State('textarea-state-example', 'value'),
)
def textinput_graphs(n_clicks, filename, value):

    # TODO: Why check for clicks?
    # if n_clicks > 0:

    ctx = dash.callback_context
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if filename is not None and trigger_id == "upload-data":
        filename = filename[0]
        df = pd.read_csv(filename)

    elif value is not None and trigger_id == "textarea-state-example-button":
        data = io.StringIO(value)
        df = pd.read_csv(data, sep=",")

    else:
        df = pd.DataFrame({
            "Wind Speed": [],
            "Cp": [],
            "Ct": [],
        })

    fig1, fig2 = plot_data(df)

    return fig1, fig2

def plot_data(df: pd.DataFrame) -> (go.Figure):
    x = df['Wind Speed']
    y1 = df['Cp']
    y2 = df['Ct']
    fig1 = go.Figure(
        data=[
            go.Scatter(
                x=x, 
                y=y1, 
                mode='lines+markers')
            ],
            layout=go.Layout(
                plot_bgcolor=colors["graphBackground"],
            #     paper_bgcolor=colors["graphBackground"]
            )
    )
    fig2 = go.Figure(
        data=[
            go.Scatter(
                x=x, 
                y=y2, 
                mode='lines+markers')],
            layout=go.Layout(
                plot_bgcolor=colors["graphBackground"],
            #     paper_bgcolor=colors["graphBackground"]
            )
    )
    return (fig1, fig2)


def parse_contents(filepath) -> pd.DataFrame:
    if 'csv' in filepath:
        df = pd.read_csv(filepath)
    elif 'xls' in filepath:
        df = pd.read_excel(filepath=filepath)
    elif "txt" in filepath:
        df = pd.read_csv(filepath, delimiter=",")
    else:
        # TODO @Lizz
        # maybe raise ValueError?
        pass
    return df





if __name__ == '__main__':
    app.run_server(debug=True)