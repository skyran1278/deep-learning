import math

import matplotlib.pyplot as plt
import numpy as np


def hw5_1_a(data, title):
    A = 15000e2  # mm2
    t = 5  # mm
    f = 0.303

    stress = (data[:, 2] / A)  # kN/mm2
    strain = (data[:, 1] / t)  # mm
    period = (data[:, 0])  # s

    tau_0 = ((np.amax(stress) - np.amin(stress)) / 2)
    gamma_0 = ((np.amax(strain) - np.amin(strain)) / 2)

    # normalize
    stress = stress / tau_0
    strain = strain / gamma_0

    plt.figure()
    plt.plot(period, stress, period, strain)
    plt.title(title + 'Time history of stress and strain')
    plt.legend(['stress', 'strain'], loc=1)
    plt.xlabel('time (sec)')
    plt.ylabel('normalize stress & strain')
    # print(argrelextrema(stress, np.greater))
    # print(stress[argrelextrema(stress, np.greater)[0]])
    # argrelmax(stress)
    delta_t = abs(data[np.argmax(stress), 0] - data[np.argmax(strain), 0])

    omega = 2 * math.pi * f
    delta = omega * delta_t

    G_1 = tau_0 / gamma_0 * math.cos(delta)
    G_2 = tau_0 / gamma_0 * math.sin(delta)
    eta = math.tan(delta)
    print(G_1, G_2, eta)
