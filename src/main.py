from Generators.AudioDataGenerator import AudioDataGenerator
from Modulators.ModulatorPSK import ModulatorPSK
from Modulators.ModulatorASK import ModulatorASK
from Noiser.Noiser import Noiser
import plotly.graph_objs as go
import numpy as np
import scipy
from Plotter.Plotter import Plotter

generator = AudioDataGenerator()
generator.setDataFromWav('assets/guitar.wav')
bits = generator.getBits()

# PSK ORDERS x SNR
testOrders = (2, 4)
testSNR = (1, 100)

modulatorPKS = ModulatorPSK()
testOrder = testOrders[0]
while(True):
    print(testOrder)
    if testOrder == testOrders[1]:
        break
    testOrder *= 2


signal = modulatorPKS.getSignal(bits)
Noiser.snr = 10
signal = Noiser.normal(signal)
Plotter.scatter(y=signal[:1024], layout=go.Layout(
    title="Modulacja ASK 4 wartościowa, 64 próbki/symbol"))


"""
demodulated = modulatorPKS.demodulate(signal)


print(bits)
print(demodulated)
print(np.nonzero(bits - demodulated))
print(np.nonzero(bits - demodulated)[0].size)
print("BER: ", np.nonzero(bits - demodulated)[0].size / bits.size)
"""
