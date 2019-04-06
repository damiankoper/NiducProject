import plotly
import plotly.graph_objs as go
import json
import math
import pickle
import numpy as np
class Plotter:

    @staticmethod
    def getOrder(order, modType):
        if modType=="QAM":
            return int(np.prod(order))
        else:
            return sum(order)

    @staticmethod
    def scatter(y, x=None, filename="temp-plot", layout=go.Layout(title="Plot"), mode=None):
        figure = go.Figure(
            layout=layout,
            data=[
                go.Scatter(
                    y=y,
                    x=x,
                    mode=mode
                )
            ]
        )
        plotly.offline.plot(figure, filename)

    @staticmethod
    def OrderSnr(result, modType, filename="temp-plot"):
        x = []
        y = []
        z = []
        for res in result:
            snr = res[7]
            try:
                x.index(snr)
            except ValueError as e:
                x.append(snr)

            order = Plotter.getOrder(json.loads(res[2]) ,modType)
            try:
                posOrder = y.index(order)
                z[posOrder].append(res[8])
            except ValueError as e:
                y.append(order)
                z.append([res[8]])

        layout = go.Layout(
            title=modType+' - BER od wartościowości modulacji i SNR sygnału demodulowanego',
            scene=dict(
                xaxis=dict(title="SNR"),
                yaxis=dict(title="Wartościowość", type="log",
                           tick0=0, dtick=math.log10(2)),
                zaxis=dict(title="BER")
            )
        )
        figure = go.Figure(
            data=[
                go.Surface(
                    x=x,
                    y=y,
                    z=z
                )
            ],
            layout=layout
        )
        plotly.offline.plot(figure, filename=filename)

    @staticmethod
    def OrderSnr2D(result, modType, filename="temp-plot"):
        x = []
        y = []
        z = []
        for res in result:
            snr = res[7]
            try:
                x.index(snr)
            except ValueError as e:
                x.append(snr)

            order = Plotter.getOrder(json.loads(res[2]) ,modType)
            try:
                posOrder = y.index(order)
                z[posOrder].append(res[8])
            except ValueError as e:
                y.append(order)
                z.append([res[8]])

        data = []
        for index, order in enumerate(y):
            scatter = go.Scatter(
                y=z[index],
                x=x,
                name=order,
                mode='lines+markers'
            )
            data.append(scatter)

        layout = go.Layout(
            title=modType+" - BER od wartościowości modulacji i SNR sygnału demodulowanego",
            xaxis=dict(
                title="SNR"
            ),
            yaxis=dict(
                title="BER"
            )
        )
        figure = go.Figure(
            layout=layout,
            data=data
        )
        plotly.offline.plot(figure, filename=filename)

    @staticmethod
    def OrderSampFreq(result, modType, filename="temp-plot"):
        x = []
        y = []
        z = []

        for res in result:
            snr = res[6]
            try:
                x.index(snr)
            except ValueError as e:
                x.append(snr)

            order = Plotter.getOrder(json.loads(res[2]) ,modType)
            try:
                posOrder = y.index(order)
                z[posOrder].append(res[8])
            except ValueError as e:
                y.append(order)
                z.append([res[8]])

        layout = go.Layout(
            title=modType + ' - BER od wartościowości i częstotliwości próbkowania sygnału, SNR: ' +
            str(round(result[0][7], 2)),
            scene=dict(
                yaxis=dict(title="Wartościowość", type="log",
                           tick0=0, dtick=math.log10(2)),
                xaxis=dict(title="Częstotliwość próbkowania"),
                zaxis=dict(title="BER")
            )
        )
        figure = go.Figure(
            data=[
                go.Surface(
                    x=x,
                    y=y,
                    z=z
                )
            ],
            layout=layout
        )
        plotly.offline.plot(figure, filename=filename)

    @staticmethod
    def OrderSampFreq2D(result, modType, filename="temp-plot"):
        x = []
        y = []
        z = []
        for res in result:
            snr = res[6]
            try:
                x.index(snr)
            except ValueError as e:
                x.append(snr)

            order = Plotter.getOrder(json.loads(res[2]) ,modType)
            try:
                posOrder = y.index(order)
                z[posOrder].append(res[8])
            except ValueError as e:
                y.append(order)
                z.append([res[8]])

        data = []
        for index, order in enumerate(y):
            scatter = go.Scatter(
                y=z[index],
                x=x,
                name=order,
                mode='lines+markers'
            )
            data.append(scatter)

        layout = go.Layout(
            title=modType+" - BER od wartościowości i częstotliwości próbkowania sygnału, SNR: " +
            str(round(result[0][7], 2)),
            xaxis=dict(
                title="Częstotliwość próbkowania"
            ),
            yaxis=dict(
                title="BER"
            )
        )
        figure = go.Figure(
            layout=layout,
            data=data
        )
        plotly.offline.plot(figure, filename=filename)

    @staticmethod
    def constellation(result, ymax, modType=None, filename="temp-plot"):
        data = []
        for res in result:
            constellation = pickle.loads(res[0])
            scatter = go.Scatter(
                y=constellation.imag,
                x=constellation.real,
                name=res[1],
                mode='markers',
                visible=False
            )
            data.append(scatter)

        steps = []
        for i in range(len(data)):
            step = dict(
                method='restyle',
                args=['visible', [False] * len(data)],
                label=str(round(result[i][1], 2))
            )
            step['args'][1][i] = True
            steps.append(step)

        sliders = [dict(
            active=0,
            currentvalue={"prefix": "SNR: "},
            pad={"t": 50},
            steps=steps
        )]
        data[0]['visible'] = True

        title = "Konstelacja dla wartościowości "+result[0][2] if modType is None else modType+" - Konstelacja dla wartościowości "+result[0][2]
        layout = go.Layout(
            title=title,
            sliders=sliders,
            xaxis=dict(
                scaleanchor='y'
            ),
            yaxis=dict(
                range=[-ymax, ymax]
            )
        )

        figure = go.Figure(
            layout=layout,
            data=data,

        )
        plotly.offline.plot(figure, filename=filename)

