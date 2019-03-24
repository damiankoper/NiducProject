import scipy.io.wavfile as wavfile
import numpy as np
import plotly
import plotly.graph_objs as go
from Plotter.Plotter import Plotter
class AudioDataGenerator:
    # int[8|16|32|float] array
    data = np.array([])

    bitrate = 1
    dataSource = "None"

    def __init__(self):
        pass

    def setDataFromWav(self, filename):
        (self.bitrate, self.data) = wavfile.read(filename)
        dataType = self.data.dtype
        # Converting to mono
        self.data = np.average(self.data, axis=1).astype(dataType)
        self.dataSource = filename

    def getDataLengthInSec(self):
        return self.data.size / self.bitrate

    def plotData(self, filename="temp-plot"):
        xLinspace = np.linspace(0, self.getDataLengthInSec(), self.data.size)
        Plotter.scatter(
            x=xLinspace,
            y=self.data,
            layout=go.Layout(
                title=self.dataSource,
                xaxis=dict(
                    title='Czas trwania [s]'
                ),
                yaxis=dict(
                    title='Wartość próbki'
                )
            ),
            filename=filename
        )

    def getDataType(self):
        return self.data.dtype

    def getBits(self):
        return np.unpackbits(np.frombuffer(self.data.tobytes(), dtype=np.uint8))
