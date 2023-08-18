try:
    import cupy as xp
except (ImportError, ModuleNotFoundError):
    import numpy as xp

from pathlib import Path

import bezier
import numpy as np
from bidict import bidict

from utils.constant import Constant
from utils.cosmology import Cosmology
# from pycbc.waveform import get_td_waveform
from utils.log_utils import MyLogger, TimerLog

mylogger = MyLogger(__name__)


class GB:
    def __init__(self, use_gpu=False, VGB=True):
        if use_gpu:
            self.xp = xp
        else:
            self.xp = np
        if VGB:
            self.key_idx = bidict(
                {
                    "f": 2,
                    "fdot": 3,
                    "beta": 4,
                    "lambda": 5,
                    "A": 1,
                    "iota": 6,
                    "psi": 7,
                    "phi0": 8,
                }
            )
        else:
            self.key_idx = bidict(
                {
                    "f": 0,
                    "fdot": 1,
                    "beta": 2,
                    "lambda": 3,
                    "A": 4,
                    "iota": 5,
                    "psi": 6,
                    "phi0": 7,
                }
            )
        self.idx_key = self.key_idx.inverse
        self.fore = None

    def __call__(self, A, f, fdot, iota, phi0, psi, T=1.0, dt=10.0):
        # get the t array
        t = self.xp.arange(0.0, T * Constant.YRSID_SI, dt)
        cos2psi = self.xp.cos(2.0 * psi)
        sin2psi = self.xp.sin(2.0 * psi)
        cosiota = self.xp.cos(iota)

        fddot = 11.0 / 3.0 * fdot**2 / f

        # phi0 is phi(t = 0) not phi(t = t0)
        phase = (
            2 * np.pi * (f * t + 1.0 / 2.0 * fdot * t**2 + 1.0 / 6.0 * fddot * t**3)
            - phi0
        )

        hSp = -self.xp.cos(phase) * A * (1.0 + cosiota * cosiota)
        hSc = -self.xp.sin(phase) * 2.0 * A * cosiota

        # from source frame to SSB frame
        hp = hSp * cos2psi - hSc * sin2psi
        hc = hSp * sin2psi + hSc * cos2psi

        return hp + 1j * hc
