from Generators.AudioDataGenerator import AudioDataGenerator
from Modulators.ModulatorPSK import ModulatorPSK
import plotly
import plotly.graph_objs as go
import numpy as np
import scipy

generator = AudioDataGenerator()
generator.setDataFromWav('assets/guitar.wav')
# generator.plotData(filename="plots/guitar")

modulatorPKS = ModulatorPSK()
signal = modulatorPKS.getSignal(generator.getBits()[:4])[:128]

modulatorPKS.demodulate(signal)

""" 
spectrum = np.fft.fft(signal)

figure = go.Figure(
    data=[
        go.Scatter(
            y = (spectrum/32).imag,
        )
    ]
)
plotly.offline.plot(figure, filename="phase")


figure = go.Figure(
    layout=go.Layout(
        xaxis=dict(
            scaleanchor='y'
        )

    ),
    data=[
        go.Scatter(
            y=signal,
        )
    ]
)
plotly.offline.plot(figure, filename="XD")
 """
""" 
figure = go.Figure(
    layout=go.Layout(
        xaxis=dict(
            scaleanchor='y'
        )
       
    ),
    data=[
        go.Scatter(
            x=modulated.real,
            y=modulated.imag,
            mode = 'markers'
        )
    ]
)
plotly.offline.plot(figure, filename="XD")
 """
