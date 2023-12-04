import numpy as np


def get_data(day, year):
    data_raw = get_data(day=1, year=2023)
    with open("input.txt", "w") as f:
        f.write(data_raw)
    input = np.loadtxt("input.txt", dtype=str)
    return input
