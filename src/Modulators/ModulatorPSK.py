import komm
import numpy as np
from .ModulatorBase import ModulatorBase

class ModulatorPSK(ModulatorBase):
    def modulate(self, bits):
        psk = komm.PSKModulation(self.orders[0], self.amplitudes[0], self.phaseOffsets[0])
        return psk.modulate(bits)
        