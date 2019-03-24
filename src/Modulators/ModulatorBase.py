from abc import ABC, abstractmethod
import numpy as np
from Plotter.Plotter import Plotter


class ModulatorBase(ABC):
    orders = (4, 12, )
    phaseOffsets = (0, 0, )
    amplitudes = (1, 2, )

    carrierFreq = 1000
    sampleFreq = 64000

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

    def getSignal(self, bits):
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
