from Generators.AudioDataGenerator import AudioDataGenerator
import Tester.tests.PSK as pskTests
import Tester.tests.ASK as askTests
import Tester.tests.APSK as apskTests
import Tester.tests.QAM as  qamTests

from Tester.Tester import Tester
from Plotter.Plotter import Plotter
import sqlite3 as sql
import json
import plotly as plotly
import plotly.graph_objs as go
import math

generator = AudioDataGenerator()
generator.setDataFromWav('assets/guitar.wav')

if input("Do you want to run tests? [y/n]:") in ['yes', 'y', 'ye']:

    bits = generator.getBits()[:32768]  # symulowana paczka po 4 KB
    tester = Tester()

    pskTests.OrderSnr(bits,tester)
    pskTests.OrderSampFreq(bits, tester)

    askTests.OrderSnr(bits,tester)
    askTests.OrderSampFreq(bits, tester)

    apskTests.OrderSnr(bits, tester)
    apskTests.OrderSampFreq(bits, tester)

    qamTests.OrderSnr(bits, tester)
    qamTests.OrderSampFreq(bits, tester)
else:
    print('No assumed')


# Generowanie wykresów
if input("Do you want to generate charts? [y/n]:") not in ['no', 'n', 'nah']:
    
    generator.plotData(filename="plots/guitar.html")
    conn = sql.connect('plots/db/results.db')

    ### PSK
    result = conn.execute(
        """
        SELECT * FROM results WHERE description=?
        """, ("PSK - BER to (order, snr)",)
    ).fetchall()

    Plotter.OrderSnr(result, modType="PSK", filename="plots/PSK/OrderSnr.html")
    Plotter.OrderSnr2D(result, modType="PSK",
                        filename="plots/PSK/OrderSnr2D.html")

    result = conn.execute(
        """
        SELECT * FROM results WHERE description=?
        """, ("PSK - BER to (order, sample frequency)",)
    ).fetchall()
    Plotter.OrderSampFreq(result, modType="PSK",
                            filename="plots/PSK/OrderSampleFreq.html")
    Plotter.OrderSampFreq2D(result, modType="PSK",
                            filename="plots/PSK/OrderSampleFreq2D.html")

    # PSK - konstelacje

    result = conn.execute(
        """
        SELECT constellation, snr, orders FROM results WHERE description=? and orders="[8]" ORDER BY snr
        """, ("PSK - BER to (order, snr)",)
    ).fetchall()
    Plotter.constellation(result, 5, "PSK", filename="plots/PSK/Constellation(8).html")


    ### ASK

    result = conn.execute(
        """
        SELECT * FROM results WHERE description=?
        """, ("ASK - BER to (order, snr)",)
    ).fetchall()

    Plotter.OrderSnr(result, modType="ASK", filename="plots/ASK/OrderSnr.html")
    Plotter.OrderSnr2D(result, modType="ASK",
                        filename="plots/ASK/OrderSnr2D.html")

    result = conn.execute(
        """
        SELECT * FROM results WHERE description=?
        """, ("ASK - BER to (order, sample frequency)",)
    ).fetchall()
    Plotter.OrderSampFreq(result, modType="ASK",
                            filename="plots/ASK/OrderSampleFreq.html")
    Plotter.OrderSampFreq2D(result, modType="ASK",
                            filename="plots/ASK/OrderSampleFreq2D.html")

    # ASK - konstelacje

    result = conn.execute(
        """
        SELECT constellation, snr, orders FROM results WHERE description=? and orders="[8]" ORDER BY snr
        """, ("ASK - BER to (order, snr)",)
    ).fetchall()
    Plotter.constellation(result, 5, "ASK", filename="plots/ASK/Constellation(8).html")

    ### APSK

    result = conn.execute(
        """
        SELECT * FROM results WHERE description=?
        """, ("APSK - BER to (order, snr)",)
    ).fetchall()

    Plotter.OrderSnr(result, modType="APSK",
                        filename="plots/APSK/OrderSnr.html")
    Plotter.OrderSnr2D(result, modType="APSK",
                        filename="plots/APSK/OrderSnr2D.html")

    result = conn.execute(
        """
        SELECT * FROM results WHERE description=?
        """, ("APSK - BER to (order, sample frequency)",)
    ).fetchall()
    Plotter.OrderSampFreq(result, modType="APSK",
                            filename="plots/APSK/OrderSampleFreq.html")
    Plotter.OrderSampFreq2D(result, modType="APSK",
                            filename="plots/APSK/OrderSampleFreq2D.html")
    # APSK - konstelacje

    result = conn.execute(
        """
        SELECT constellation, snr, orders FROM results WHERE description=? and orders="[4, 12]" ORDER BY snr
        """, ("APSK - BER to (order, snr)",)
    ).fetchall()
    Plotter.constellation(result, 6, "APSK", filename="plots/APSK/Constellation(4-12).html")

    result = conn.execute(
        """
        SELECT constellation, snr, orders FROM results WHERE description=? and orders="[4, 12, 16]" ORDER BY snr
        """, ("APSK - BER to (order, snr)",)
    ).fetchall()
    Plotter.constellation(result, 6, "APSK", filename="plots/APSK/Constellation(4-12-16).html")

    result = conn.execute(
        """
        SELECT constellation, snr, orders FROM results WHERE description=? and orders="[4, 12, 16, 32]" ORDER BY snr
        """, ("APSK - BER to (order, snr)",)
    ).fetchall()
    Plotter.constellation(result, 6, "APSK", filename="plots/APSK/Constellation(4-12-16-32).html")

    ### QAM

    result = conn.execute(
        """
        SELECT * FROM results WHERE description=?
        """, ("QAM - BER to (order, snr)",)
    ).fetchall()

    Plotter.OrderSnr(result, modType="QAM",
                        filename="plots/QAM/OrderSnr.html")
    Plotter.OrderSnr2D(result, modType="QAM",
                        filename="plots/QAM/OrderSnr2D.html")

    result = conn.execute(
        """
        SELECT * FROM results WHERE description=?
        """, ("QAM - BER to (order, sample frequency)",)
    ).fetchall()
    Plotter.OrderSampFreq(result, modType="QAM",
                            filename="plots/QAM/OrderSampleFreq.html")
    Plotter.OrderSampFreq2D(result, modType="QAM",
                            filename="plots/QAM/OrderSampleFreq2D.html")
    # QAM - konstelacje

    result = conn.execute(
        """
        SELECT constellation, snr, orders FROM results WHERE description=? and orders="[2, 2]" ORDER BY snr
        """, ("QAM - BER to (order, snr)",)
    ).fetchall()
    Plotter.constellation(result, 6, "QAM", filename="plots/QAM/Constellation(4).html")

    result = conn.execute(
        """
        SELECT constellation, snr, orders FROM results WHERE description=? and orders="[4, 4]" ORDER BY snr
        """, ("QAM - BER to (order, snr)",)
    ).fetchall()
    Plotter.constellation(result, 6, "QAM", filename="plots/QAM/Constellation(16).html")

    result = conn.execute(
        """
        SELECT constellation, snr, orders FROM results WHERE description=? and orders="[8, 8]" ORDER BY snr
        """, ("QAM - BER to (order, snr)",)
    ).fetchall()
    Plotter.constellation(result, 9, "QAM", filename="plots/QAM/Constellation(64).html")
