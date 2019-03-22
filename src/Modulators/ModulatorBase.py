from abc import ABC, abstractmethod
import numpy as np


class ModulatorBase(ABC):
    orders = (4,)
    phaseOffsets = (0,)
    amplitudes = (50,)

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

    def getSignal(self, bits):
        modulated = self.modulate(bits)
        modulatedRepeated = np.repeat(
            modulated, self.sampleFreq / self.carrierFreq)
        carrierLinspace = np.linspace(
            0, 2*np.pi * modulated.size, modulatedRepeated.size)

        return (modulatedRepeated.real * np.cos(carrierLinspace)) + (modulatedRepeated.imag * np.sin(carrierLinspace))

    def getSymbolsFromSignal(self, signal):
        signal = signal.reshape((-1,np.int(self.sampleFreq / self.carrierFreq)))
        signal = np.fft.fft(signal,axis=1)
        return signal