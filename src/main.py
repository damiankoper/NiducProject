from Generators.AudioDataGenerator import AudioDataGenerator
import Tester.tests.PSK as pskTests
from Tester.Tester import Tester
from Plotter.Plotter import Plotter
import sqlite3 as sql
import json
import plotly as py
import plotly.graph_objs as go
import math

generator = AudioDataGenerator()
generator.setDataFromWav('assets/guitar.wav')
bits = generator.getBits()[:32768]  # symulowana paczka po 4 KB

tester = Tester()



pskTests.OrderSnr(bits,tester)
conn = sql.connect('plots/db/results.db')
result = conn.execute(
    """
    SELECT * FROM results WHERE description=?
    """, ("PSK - BER to (order, snr)",)
).fetchall()

Plotter.OrderSnr(result, modType="PSK")




pskTests.OrderSampFreq(bits, tester)
result = conn.execute(
    """
    SELECT * FROM results WHERE description=?
    """, ("PSK - BER to (order, sample frequency)",)
).fetchall()
Plotter.OrderSampFreq(result, modType="PSK")
