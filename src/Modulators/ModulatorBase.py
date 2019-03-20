from abc import ABC, abstractmethod


class ModulatorBase(ABC):
    orders = (2,)
    phaseOffsets = (0,)
    amplitudes = (1,)

    carrierFreq = 1

    @abstractmethod
    # Zwraca tablicę postaci wykładniczych dla wszystkich bodów
    def modulate(self, bits):
        pass

    def getSignal(self):
        pass

