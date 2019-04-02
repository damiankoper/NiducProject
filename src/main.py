from Generators.AudioDataGenerator import AudioDataGenerator
from Modulators.ModulatorPSK import ModulatorPSK
from Modulators.ModulatorASK import ModulatorASK
from Noiser.Noiser import Noiser
from Tester.Tester import Tester

import plotly.graph_objs as go
import numpy as np
import scipy
from Plotter.Plotter import Plotter

tester = Tester()

generator = AudioDataGenerator()
generator.setDataFromWav('assets/guitar.wav')
bits = generator.getBits()[:32768]  # symulowana paczka po 4 KB

# PSK ORDERS x SNR

modulator = ModulatorPSK()
modulator.amplitudes = (1,)
modulator.phaseOffsets = (1,)
testOrders = (2, 64)
testOrder = testOrders[0]
testSNRs = np.linspace(1, 30, 100)
while(True):
    modulator.orders = (testOrder,)
    signal = modulator.getSignal(bits)
    alignedBits = modulator.getAlignedBits(bits)
    print("Processing PSK order:", testOrder, "SNR from", testSNRs[0], "to",testSNRs[-1])
    for testSNR in testSNRs:
        signalNoised = Noiser.normal(signal.copy(), snr=testSNR)
        demodulated = modulator.demodulate(signalNoised)
        BER = np.nonzero(alignedBits - demodulated)[0].size / alignedBits.size
        tester.writeResultToDB(modulator, testSNR, signal, BER, description="PSK - BER to (order, snr)")

    if testOrder == testOrders[1]:
        break
    else:
        testOrder *= 2
