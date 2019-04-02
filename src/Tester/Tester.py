import sqlite3 as sqlite3
import json


class Tester:
    conn = None

    def __init__(self):
        self.conn = sqlite3.connect('plots/db/results.db')
        self.conn.execute("DELETE FROM results")
        self.conn.commit()

    def writeResultToDB(self, modulator, snr, signal, ber, description=""):
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
                description
                ) VALUES (?,?,?,?,?,?,?,?,?)
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
                description
            ))
        self.conn.commit()

    def saveAndClose(self):
        self.conn.commit()
        self.conn.close()
