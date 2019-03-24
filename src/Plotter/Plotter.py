import plotly
import plotly.graph_objs as go

class Plotter:

    @staticmethod
    def scatter(y, x = None, filename="temp-plot", layout=go.Layout(title="Plot"), mode=None):
        figure = go.Figure(
            layout= layout,
            data=[
                go.Scatter(
                    y=y,
                    x=x,
                    mode=mode
                )
            ]
        )
        plotly.offline.plot(figure, filename)