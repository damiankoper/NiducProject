import plotly
import plotly.graph_objs as go
import json
import math


class Plotter:

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

            order = sum(json.loads(res[2]))
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

            order = sum(json.loads(res[2]))
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

            order = sum(json.loads(res[2]))
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

            order = sum(json.loads(res[2]))
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
