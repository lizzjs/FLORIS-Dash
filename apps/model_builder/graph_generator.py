
import pandas as pd
import plotly.express as px


def wind_rose_plot(data):
    df = pd.DataFrame(data)
    fig = px.bar_polar(
        df,
        r="frequency",
        theta="direction",
        color="strength",
        template="seaborn",
        color_discrete_sequence=px.colors.sequential.Plasma_r,
        title="Wind Rose"
    )
    return fig

