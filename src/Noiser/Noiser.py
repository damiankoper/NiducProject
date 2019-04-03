import numpy as np


class Noiser:
    @staticmethod
    def normal(signal, snr = 1):
        noise = np.random.normal(size=signal.size, scale=np.max(signal)) / snr

        return signal + noise
