from Modulators.ModulatorQAM import ModulatorQAM
from Noiser.Noiser import Noiser
import numpy as np
import pickle


def OrderSnr(bits, tester):
    description = "QAM - BER to (order, snr)"
    tester.clearSeries(description)

    modulator = ModulatorQAM()
    testOrders = [(2,2), (4,4), (8,8)]
    testSNRs = np.linspace(1, 30, 100)
    for orders in testOrders:
        modulator.orders = orders
        signal = modulator.getSignal(bits)
        alignedBits = modulator.getAlignedBits(bits)
        print("Processing QAM order:", orders, "SNR from",
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
    description = "QAM - BER to (order, sample frequency)"
    tester.clearSeries(description)

    modulator = ModulatorQAM()
    modulator.amplitudes = (10,)
    testOrders = [(2,2), (4,4), (8,8)]
    testSampFreqs = range(4000, 16000, 100)
    for orders in testOrders:
        modulator.orders = orders

        for testSampFreq in testSampFreqs:
            modulator.sampleFreq = testSampFreq
            signal = modulator.getSignal(bits)
            signalNoised = Noiser.normal(signal.copy(), snr=2)
            alignedBits = modulator.getAlignedBits(bits)

            print("Processing APSK order:", orders,
                  "Sampling frequency:", testSampFreq, "SNR: 2")

            demodulated = modulator.demodulate(signalNoised)
            BER = np.nonzero(
                alignedBits - demodulated)[0].size / alignedBits.size
            tester.writeResultToDB(
                modulator, 2, signal, BER, description=description)
