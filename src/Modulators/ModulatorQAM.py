import komm
import numpy as np
from .ModulatorBase import ModulatorBase

class ModulatorQAM(ModulatorBase):
    def modulate(self, bits):
        self.orderCountMethod = "mul"
        qam = komm.QAModulation(self.orders)
        return qam.modulate(bits)
        
    def demodulate(self, bods):
        self.orderCountMethod = "mul"
        symbols = self.getSymbolsFromSignal(bods)
        qam = komm.QAModulation(self.orders)
        return qam.demodulate(symbols)
