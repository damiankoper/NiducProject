from Modulators.ModulatorAPSK import ModulatorAPSK
from Noiser.Noiser import Noiser
import numpy as np
import pickle

def OrderSnr(bits, tester):
    description = "APSK - BER to (order, snr)"
    tester.clearSeries(description)

    modulator = ModulatorAPSK()
    modulator.phaseOffsets = (0,)    
    testPhaseOffsets = [(0, np.pi/4), (0, np.pi/4, 0), (0, np.pi/4, 0, np.pi/4)]
    testOrders = [(4, 12), (4, 12, 16), (4, 12, 16, 32)]
    testAmplitudes = [(1, 2), (1, 2, 3), (1, 2, 3, 4)]
    testSNRs = np.linspace(1, 30, 100)
    for index, orders in enumerate(testOrders):
        modulator.orders = orders
        modulator.amplitudes = testAmplitudes[index]
        modulator.phaseOffsets = testPhaseOffsets[index]
        
        signal = modulator.getSignal(bits)
        alignedBits = modulator.getAlignedBits(bits)
        print("Processing APSK order:", orders, "amplitudes:", testAmplitudes[index], "SNR from",
              testSNRs[0], "to", testSNRs[-1], "times", 100)
        for testSNR in testSNRs:
            signalNoised = Noiser.normal(signal.copy(), snr=testSNR)

            symbols = modulator.getSymbolsFromSignal(signalNoised)[:1024]
            
            demodulated = modulator.demodulate(signalNoised)
            BER = np.nonzero(
                alignedBits - demodulated)[0].size / alignedBits.size
            tester.writeResultToDB(
                modulator, testSNR, signal, BER, description=description, constellation=pickle.dumps(symbols))


def OrderSampFreq(bits, tester):
    description = "APSK - BER to (order, sample frequency)"
    tester.clearSeries(description)

    modulator = ModulatorAPSK()
    modulator.amplitudes = (10,)
    testPhaseOffsets = [(0, 0), (0, 0, 0), (0, 0, 0, 0)]
    testOrders = [(4, 12), (4, 12, 16), (4, 12, 16, 32)]
    testAmplitudes = [(1, 2), (1, 2, 3), (1, 2, 3, 4)]
    testSampFreqs = range(4000, 16000, 100)
    for index, orders in enumerate(testOrders):
        modulator.orders = orders
        modulator.amplitudes = testAmplitudes[index]
        modulator.phaseOffsets = testPhaseOffsets[index]

        for testSampFreq in testSampFreqs:
            modulator.sampleFreq = testSampFreq
            signal = modulator.getSignal(bits)
            signalNoised = Noiser.normal(signal.copy(), snr=2)
            alignedBits = modulator.getAlignedBits(bits)

            print("Processing APSK order:", orders, "amplitudes", testAmplitudes[index],
                  "Sampling frequency:", testSampFreq, "SNR: 2")

            demodulated = modulator.demodulate(signalNoised)
            BER = np.nonzero(
                alignedBits - demodulated)[0].size / alignedBits.size
            tester.writeResultToDB(
                modulator, 2, signal, BER, description=description)
