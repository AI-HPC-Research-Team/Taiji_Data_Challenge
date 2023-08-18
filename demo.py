try:
    import cupy as xp
except (ImportError, ModuleNotFoundError):
    import numpy as xp

from pathlib import Path

import h5py
import numpy as np
from tqdm import tqdm

from tdc.tdi import TDIWaveformGen
from utils.log_utils import MyLogger, TimerLog

mylogger = MyLogger(__name__)


def read_catalog(self, cat_path):
    if cat_path.suffix in [".txt", ".dat"]:
        par = np.loadtxt(cat_path)
    elif cat_path.suffix == ".npy":
        par = np.load(cat_path)
    permute = [
        self.key_idx["A"],
        self.key_idx["f"],
        self.key_idx["fdot"],
        self.key_idx["iota"],
        self.key_idx["phi0"],
        self.key_idx["psi"],
        self.key_idx["lambda"],
        self.key_idx["beta"],
    ]
    self.para_cat = par[:, permute]


@TimerLog(mylogger.logger, "Generating data.......")
def gen_data(self, cat_path, h5_path):
    cat_path = Path(cat_path)
    read_catalog(self.gb, cat_path)
    self.gb.data = xp.zeros([3, self.Nt])
    for i in tqdm(range(self.gb.para_cat.shape[0])):
        p = list(self.gb.para_cat[i])
        wave = self.gb_TDI(*p)
        wave = xp.array(wave)
        self.gb.data += wave
    mylogger.logger.info("Writing to file----> {}".format(h5_path))
    data = xp.vstack([self.sample_times, self.gb.data])
    with h5py.File(h5_path, "w") as f:
        f.create_dataset("TDIdata", data=data.get())


def main():
    VGB_cat = "catalog/VGB-catalog.txt"
    tdi_wg = TDIWaveformGen(T=2.0)
    tdi_wg.init_GB(VGB=True)
    gen_data(tdi_wg, VGB_cat, "test-VGB.hdf5")


if __name__ == "__main__":
    main()
