import plotly.offline as py
import plotly.graph_objs as go
import pandas as pd

def chartDelay():

    # Read data from a csv
    z_data = pd.read_csv('data_delay.csv')

    data = [
        go.Surface(
            z=z_data.as_matrix()
        )
    ]
    layout = go.Layout(
        title='Delay',
        autosize=False,
        width=600,
        height=600,
        margin=dict(
            l=10,
            r=10,
            b=10,
            t=10
        ),
        scene={"xaxis": {'title':"Distance [μm]", "tickfont": {"size": 10}, 'type': "linear"},
                    "yaxis": {'title': "Frequency [x10 Hz]", "tickfont": {"size": 10},
                                "tickangle": 1},
                    "zaxis": {'title': "Delay [s]",
                                "tickfont": {"size": 10}},
                    "camera": {"eye": {"x": 2, "y": 1, "z": 1.25}},
                    "aspectmode": "cube",
                    }
    )
    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='delay_chart.html')



def chartGain():

    # Read data from a csv
    z_data = pd.read_csv('data_gain.csv')

    data = [
        go.Surface(
            z=z_data.as_matrix()
        )
    ]
    layout = go.Layout(
        title='Delay',
        autosize=False,
        width=600,
        height=600,
        margin=dict(
            l=10,
            r=10,
            b=10,
            t=10
        ),
        scene={"xaxis": {'title':"Distance [μm]", "tickfont": {"size": 10}, 'type': "linear"},
                    "yaxis": {'title': "Frequency [x10 Hz]", "tickfont": {"size": 10},
                                "tickangle": 1},
                    "zaxis": {'title': "Channel Attenuation [Db]",
                                "tickfont": {"size": 10}},
                    "camera": {"eye": {"x": 2, "y": 1, "z": 1.25}},
                    "aspectmode": "cube",
                    }
    )
    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='grain_chart.html')

