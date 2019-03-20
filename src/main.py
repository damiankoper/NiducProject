from Generators.AudioDataGenerator import AudioDataGenerator
from Modulators.ModulatorPSK import ModulatorPSK
import plotly
import plotly.graph_objs as go
import numpy as np

generator = AudioDataGenerator()
generator.setDataFromWav('assets/guitar.wav')
# generator.plotData(filename="plots/guitar")

modulatorPKS = ModulatorPSK()
modulated = modulatorPKS.modulate(generator.getBits())[0:1000]





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
