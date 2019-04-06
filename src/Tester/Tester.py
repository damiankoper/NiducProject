import sqlite3 as sqlite3
import json
import pickle
import numpy as np
class Tester:
    conn = None

    def __init__(self):
        self.conn = sqlite3.connect('plots/db/results.db')

    def clearSeries(self, description=""):
        self.conn.execute(
            """
            DELETE FROM results
            WHERE description = ?
            """, (description,)
        )

    def writeResultToDB(self, modulator, snr, signal, ber, description="", constellation=pickle.dumps(np.array([], dtype='complex128'))):
        self.conn.execute(
            """
            INSERT INTO results (
                samples,
                orders,
                amplitudes,
                phase_offsets,
                carr_freq,
                samp_freq,
                snr,
                ber,
                description,
                constellation
                ) VALUES (?,?,?,?,?,?,?,?,?,?)
            """,
            (
                signal.size,
                json.dumps(modulator.orders),
                json.dumps(modulator.amplitudes),
                json.dumps(modulator.phaseOffsets),
                modulator.carrierFreq,
                modulator.sampleFreq,
                snr,
                ber,
                description,
                constellation
            ))
        self.conn.commit()

    def saveAndClose(self):
        self.conn.commit()
        self.conn.close()
