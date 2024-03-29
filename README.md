# FLORIS Dash

Web-based interface to interact with NREL's [FLORIS] (https://github.com/nrel/floris)
wind turbine wake simulation software built with [Plotly Dash](https://plotly.com/dash/).

## Outline and References
The objective of this project is to design and build a set of tools for preprocessing
and postprocessing of FLORIS data. There are three major components:

- Input data creation and visualization
- Farm performance dashboard
- 3D flow field inspection


# Development Notes

We are interested in designing a model builder with step-by-step input/user-interaction

1. Turbine: (2 tabs, 'Geometry' & 'Cp/Ct Table')
    + Geometry: will have several interactive sliders and connected input/output values
        -TABS: Method 1 - content as callback (https://dash.plotly.com/dash-core-components/tabs)
        -SLIDER/INPUT: Synchronizing a Slider with a Text Input Example (https://dash.plotly.com/advanced-callbacks)

    + Cp/Ct Table: should have a text input for the Cp/Ct values or an option to load a table from a file

    These values should be stored into a hard coded dictionary, inputing values with respect to their key
        i.e. dictionary["Power"] = Cp_values


## app_060121.py

we can access prop_id's and values, it is stored as a dictionary and describes which id from the dcc.Slider and dcc.Input is 
being used so we can set both values to be equal, if not, it was tested that the input of one would not update until the next 
input was given (meaning the the dcc.input or dcc.slider output would not display the same output):

    ctx = dash.callback_context
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
    value = input_value if trigger_id == "input-circular" else slider_value
    return value, value