from Generators.AudioDataGenerator import AudioDataGenerator
from Modulators.ModulatorPSK import ModulatorPSK
from Modulators.ModulatorASK import ModulatorASK
import plotly.graph_objs as go

import numpy as np
import scipy
from Plotter.Plotter import Plotter

generator = AudioDataGenerator()
generator.setDataFromWav('assets/guitar.wav')
generator.plotData(filename="plots/guitar")

bits = generator.getBits()

modulatorPKS = ModulatorPSK()
signal = modulatorPKS.getSignal(bits)
#signal = signal + 10 * np.random.randn(signal.size)
#Plotter.scatter(y=signal[:1024], layout=go.Layout(title="Modulacja ASK 4 wartościowa, 64 próbki/symbol"))

 
symbols = modulatorPKS.getSymbolsFromSignal(signal)[:1024]
Plotter.scatter(y=symbols.imag, x=symbols.real, layout=go.Layout(
    xaxis=dict(
        scaleanchor='y'
    ),
    title="Modulacja PSK 4 wartościowa - konstelacja"
),
    mode="markers"
)
"""
demodulated = modulatorPKS.demodulate(signal)


print(bits)
print(demodulated)
print(np.nonzero(bits - demodulated))
print(np.nonzero(bits - demodulated)[0].size)
print("BER: ", np.nonzero(bits - demodulated)[0].size / bits.size)
 """