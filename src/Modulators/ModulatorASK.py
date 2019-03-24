import komm
import numpy as np
from .ModulatorBase import ModulatorBase

class ModulatorASK(ModulatorBase):
    def modulate(self, bits):
        psk = komm.ASKModulation(self.orders[0], self.amplitudes[0], self.phaseOffsets[0])
        return psk.modulate(bits)
        
    def demodulate(self, bods):
        symbols = self.getSymbolsFromSignal(bods)
        psk = komm.ASKModulation(self.orders[0], self.amplitudes[0], self.phaseOffsets[0])
        return psk.demodulate(symbols)
