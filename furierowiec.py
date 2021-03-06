from enum import Enum
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
import scipy.fftpack
import numpy as np


class DATASET(Enum):
    OKE_CCl4 = 1
    OKE_chloroform = 2
    Raman_CCl4 = 3
    Raman_chloroform = 4


class Series(object):
    def __init__(self, dataset, x_col, y_col, label="signal"):
        self.dataset = dataset
        self.x_col = x_col
        self.y_col = y_col
        self.label = label


DATA_LOCATION = "data/csv"
DATASET_FILENAMES = {
    DATASET.OKE_CCl4: "OKE_CCl4.csv",
    DATASET.OKE_chloroform: "OKE_chloroform.csv",
    DATASET.Raman_CCl4: "Raman_CCl4.csv",
    DATASET.Raman_chloroform: "Raman_chloroform.csv"
}


class Label:
    wavenumber = "Liczba falowa [cm^-1]"
    time = "Opóźnienie [fs]"
    amplitude = "Amplituda"


# freq - frequency in fs^-1 = 10^15 Hz
def wavenumber_from_freq(freq):
    freq_hz = (10 ** 15) * freq  # Hz
    lightspeed = 30000000000.0  # cm per sec
    return freq_hz / lightspeed


def read_dataset(dataset):
    filename = f"{DATA_LOCATION}/{DATASET_FILENAMES[dataset]}"
    return pd.read_csv(filename)


def fourier(xs, ys):
    n_records = len(xs) // 2
    ys_fourier = np.abs(sp.fftpack.fft(ys))
    frate = (xs[1] - xs[0])
    freq = 1.0 / frate
    xs_fourier = [wavenumber_from_freq(x) for x in np.linspace(0, freq / 2, n_records, endpoint=True)]
    return xs_fourier, ys_fourier


def add_series(
    dataset,
    x_col,
    y_col,
    label,
    in_x_min,
    in_x_max,
    res_x_min,
    res_x_max,
    normalized,
    fourierized
):
    full_df = read_dataset(dataset)
    df = full_df[np.logical_and(full_df[x_col] >= in_x_min, full_df[x_col] <= in_x_max)]

    xs = df[x_col].values
    ys = df[y_col].values

    if fourierized:
        xs, ys = fourier(xs, ys)

    # cut off results out of bounds and their values
    xs, ys = zip(*[(a, b) for a, b in zip(xs, ys) if res_x_min <= a <= res_x_max])

    if normalized:
        ys = [y / max(ys[:]) for y in ys]

    plt.plot(xs, ys, label=label)


def plot_stuff(
    *serieses,
    x_label=Label.time,
    y_label=Label.amplitude,
    in_x_min=-1000000.,     # the max and min values
    in_x_max=1000000.,      # could be set to some kind of infinity
    res_x_min=-1000000.,    # or system max/min
    res_x_max=1000000.,     # but these are good enough for this task
    normalized=False,
    fourierized=False,
    show_legend=False,
    y_scale="linear",
    y_limits=None
):
    for series in serieses:
        add_series(
            series.dataset,
            series.x_col,
            series.y_col,
            series.label,
            in_x_min,
            in_x_max,
            res_x_min,
            res_x_max,
            normalized,
            fourierized
        )
    plt.yscale(y_scale)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    if y_limits is not None:
        plt.ylim(y_limits)
    if show_legend:
        plt.legend(loc='upper right')
    plt.grid()
    plt.show()
