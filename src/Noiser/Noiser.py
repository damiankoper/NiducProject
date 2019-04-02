import numpy as np


class Noiser:
    snr = 1

    @staticmethod
    def normal(signal):
        signalAvgPower = np.mean(signal*signal)
        noise = (signalAvgPower / Noiser.snr) * np.random.randn(signal.size)

        return signal + noise
