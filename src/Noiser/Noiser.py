import numpy as np


class Noiser:
    @staticmethod
    def normal(signal, snr = 1):
        signalAvgPower = np.mean(signal*signal)
        noise = (signalAvgPower / snr) * np.random.randn(signal.size)

        return signal + noise
