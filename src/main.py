from Generators.AudioDataGenerator import AudioDataGenerator
import Tester.tests.PSK as pskTests
from Tester.Tester import Tester
from Plotter.Plotter import Plotter
import sqlite3 as sql
import json
import plotly as plotly
import plotly.graph_objs as go
import math

if input("Do you want to run tests? [y/n]:") in ['yes','y','ye']:
    generator = AudioDataGenerator()
    generator.setDataFromWav('assets/guitar.wav')
    bits = generator.getBits()[:32768]  # symulowana paczka po 4 KB
    tester = Tester()
    pskTests.OrderSnr(bits,tester)
    pskTests.OrderSampFreq(bits, tester)
else: print('No assumed') 



### Generowanie wykresów

conn = sql.connect('plots/db/results.db')

result = conn.execute(
    """
    SELECT * FROM results WHERE description=?
    """, ("PSK - BER to (order, snr)",)
).fetchall()

Plotter.OrderSnr(result, modType="PSK", filename="plots/PSK/OrderSnr.html")
Plotter.OrderSnr2D(result, modType="PSK", filename="plots/PSK/OrderSnr2D.html")
 

result = conn.execute(
    """
    SELECT * FROM results WHERE description=?
    """, ("PSK - BER to (order, sample frequency)",)
).fetchall()
Plotter.OrderSampFreq(result, modType="PSK", filename="plots/PSK/OrderSampleFreq.html")
Plotter.OrderSampFreq2D(result, modType="PSK", filename="plots/PSK/OrderSampleFreq2D.html")
