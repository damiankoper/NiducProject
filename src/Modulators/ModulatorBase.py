from abc import ABC, abstractmethod
import numpy as np
from Plotter.Plotter import Plotter
import math


class ModulatorBase(ABC):
    orders = (4, 12, )
    phaseOffsets = (0, 0, )
    amplitudes = (1, 2, )

    carrierFreq = 1000
    sampleFreq = 4000

    @abstractmethod
    # Zwraca tablicę postaci wykładniczych dla wszystkich bodów
    def modulate(self, bits):
        pass

    @abstractmethod
    # Zwraca tablicę bitów
    def demodulate(self, signal):
        pass

    def getSamplesPerSymbol(self):
        return np.int(np.round(self.sampleFreq/self.carrierFreq))

    def getAlignedBits(self, bits):
        m = math.log2(sum(self.orders))
        if bits.size % m != 0:
            bits = np.resize(bits, (np.int(bits.size + m-(bits.size % m))))
        return bits

    def getSignal(self, bits):
        bits = self.getAlignedBits(bits)
        modulated = self.modulate(bits)
        modulatedRepeated = np.repeat(modulated, self.getSamplesPerSymbol())
        carrierLinspace = np.linspace(
            0, 2*np.pi*modulated.size, modulatedRepeated.size, endpoint=False)

        return (modulatedRepeated.real * np.cos(carrierLinspace)) + (modulatedRepeated.imag * np.sin(carrierLinspace))

    def getSymbolsFromSignal(self, signal):
        signal = signal.reshape((-1, self.getSamplesPerSymbol()))
        signal = np.fft.fft(signal, axis=1)
        signal = np.divide(signal, self.getSamplesPerSymbol()/2)
        signal.imag *= -1  # nie wiem czemu ale działa
        return signal[:, 1]
