import math

import matplotlib.pyplot as plt
import numpy as np


def hw5_1_b(data, title):
    A = 15000e2  # mm2
    t = 5  # mm

    stress = (data[:, 2] / A)  # kN/mm2
    strain = (data[:, 1] / t)  # mm
    # period = (data[:, 0])  # s

    plt.figure()
    plt.plot(strain, stress)
    plt.title(title + 'stress-strain curve')
    plt.xlabel('strain')
    plt.ylabel('stress')

    G_1 = stress[np.argmax(strain)] / np.amax(strain)
    G_2 = stress[np.argmin(abs(strain))] / np.amax(strain)
    eta = G_2 / G_1
    print(G_1, G_2, eta)
