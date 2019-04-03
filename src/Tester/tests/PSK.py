from Modulators.ModulatorPSK import ModulatorPSK
from Noiser.Noiser import Noiser
import numpy as np


def OrderSnr(bits, tester):

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
        print("Processing PSK order:", testOrder, "SNR from",
              testSNRs[0], "to", testSNRs[-1], "times", 100)
        for testSNR in testSNRs:
            signalNoised = Noiser.normal(signal.copy(), snr=testSNR)
            demodulated = modulator.demodulate(signalNoised)
            BER = np.nonzero(
                alignedBits - demodulated)[0].size / alignedBits.size
            tester.writeResultToDB(
                modulator, testSNR, signal, BER, description="PSK - BER to (order, snr)")

        if testOrder == testOrders[1]:
            break
        else:
            testOrder *= 2


def OrderSampFreq(bits, tester):

    modulator = ModulatorPSK()
    modulator.amplitudes = (1,)
    modulator.phaseOffsets = (1,)
    testOrders = (2, 64)
    testOrder = testOrders[0]
    testSampFreqs = range(4000, 16000, 100)
    while(True):
        for testSampFreq in testSampFreqs:
            modulator.orders = (testOrder,)
            modulator.sampleFreq = testSampFreq
            signal = modulator.getSignal(bits)
            signalNoised = Noiser.normal(signal.copy(), snr=2)
            alignedBits = modulator.getAlignedBits(bits)

            print("Processing PSK order:", testOrder,
                  "Sampling frequency:", testSampFreq, "SNR: 2")

            demodulated = modulator.demodulate(signalNoised)
            BER = np.nonzero(
                alignedBits - demodulated)[0].size / alignedBits.size
            tester.writeResultToDB(
                modulator, 2, signal, BER, description="PSK - BER to (order, sample frequency)")

        if testOrder == testOrders[1]:
            break
        else:
            testOrder *= 2
