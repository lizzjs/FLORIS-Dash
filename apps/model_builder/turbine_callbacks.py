
import dash
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import io
import pandas as pd

from app import app, colors

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
    Input('input-hubheight', 'value'),
)
def GeomTab_hubheight_output(input_value):
    return input_value

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
    Output('slider-tiltang', 'value'),
    Input('slider-tiltang', 'value')
)
def GeomTab_tiltang_output(slider_value):
    return slider_value

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
    Output('slider-yawang', 'value'),
    Input('slider-yawang', 'value')
)
def GeomTab_yawang_output(slider_value):
    return slider_value

#TAB1-Rotor Diameter
@app.callback(
    Output('input-rotordiam', 'value'),
    Input('input-rotordiam', 'value'),
)
def GeomTab_rotordiam_output(input_value):
    return input_value

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
        #Web app initialization
        df = pd.DataFrame({
            "Wind Speed": [],
            "Cp": [],
            "Ct": [],
        })

    # FLORIS requires that the Cp and Ct table lengths be equal to the number of wind speed measurements.
    if len(df["Cp"]) != len(df["Wind Speed"]) or len(df["Ct"]) != len(df["Wind Speed"]):
        raise ValueError("Cp and Ct curves must contain equal number of points as wind speed measurements.")

    fig1, fig2 = plot_data(df)

    return fig1, fig2

def plot_data(df: pd.DataFrame) -> (go.Figure):
    fig1 = go.Figure(
        data=[
            go.Scatter(
                x=df['Wind Speed'],
                y=df['Cp'],
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
                x=df['Wind Speed'],
                y=df['Ct'],
                mode='lines+markers')],
            layout=go.Layout(
                plot_bgcolor=colors["graphBackground"],
            #     paper_bgcolor=colors["graphBackground"]
            )
    )
    return (fig1, fig2)