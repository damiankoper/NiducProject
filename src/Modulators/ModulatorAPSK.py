import komm
import numpy as np
from .ModulatorBase import ModulatorBase

class ModulatorAPSK(ModulatorBase):
    def modulate(self, bits):
        apsk = komm.APSKModulation(orders=self.orders, amplitudes=self.amplitudes, phase_offsets=self.phaseOffsets)
        return apsk.modulate(bits)
        
    def demodulate(self, bods):
        symbols = self.getSymbolsFromSignal(bods)
        apsk = komm.APSKModulation(orders=self.orders, amplitudes=self.amplitudes, phase_offsets=self.phaseOffsets)
        return apsk.demodulate(symbols)
