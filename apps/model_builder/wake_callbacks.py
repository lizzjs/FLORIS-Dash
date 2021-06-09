
import dash
from dash.dependencies import Input, Output, State

from app import app

@app.callback(
    Output('display-selected-values1', 'children'),
    Input('radioitems-input1', 'value'),
)
def wake_velocity_radio(selection):
    if selection is None:
        return ''
    else:
        return u'{} has been selected'.format(selection)

@app.callback(
    Output('display-selected-values2', 'children'),
    Input('radioitems-input2', 'value'),
)
def wake_velocity_radio(selection):
    if selection is None:
        return ''
    else:
        return u'{} has been selected'.format(selection)

@app.callback(
    Output('display-selected-values3', 'children'),
    Input('radioitems-input3', 'value'),
)
def wake_velocity_radio(selection):
    if selection is None:
        return ''
    else:
        return u'{} has been selected'.format(selection)

@app.callback(
    Output('display-selected-values4', 'children'),
    Input('radioitems-input4', 'value'),
)
def wake_velocity_radio(selection):
    if selection is None:
        return ''
    else:
        return u'{} has been selected'.format(selection)