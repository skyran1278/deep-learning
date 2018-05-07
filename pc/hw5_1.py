import math

import matplotlib.pyplot as plt
import numpy as np
from openpyxl import load_workbook

# ================= initialize =============================
WB = load_workbook(
    filename='pc/VE damper properties test.xlsx', read_only=True)

WS_25 = WB['0.303Hz_2.5mm']

WS_75 = WB['0.303Hz_7.5mm']


def get_data_byexcel(ws, min_row, min_col, max_row, max_col):
    data = np.array([])
    for row in ws.iter_rows(min_row=min_row, min_col=min_col, max_row=max_row, max_col=max_col):
        for cell in row:
            data = np.append(data, [cell.value])
    return np.reshape(data, (max_row - min_row + 1, max_col - min_col + 1))


TDF_25 = get_data_byexcel(
    ws=WS_25, min_row=3, min_col=1, max_row=3747, max_col=3)
TDF_75 = get_data_byexcel(
    ws=WS_75, min_row=3, min_col=1, max_row=4817, max_col=3)

A = 15000  # cm2

stress_25 = TDF_25[:, 2] / A  # kN/cm2
strain_25 = TDF_25[:, 1] / 2.5  # mm

stress_25 = stress_25 / np.amax(stress_25)

strain_25 = strain_25 / np.amax(strain_25)

plt.figure()
plt.plot(TDF_25[:, 0], stress_25, TDF_25[:, 0], strain_25)
plt.title('2.5mm Time history of stress and strain')
plt.legend(['stress', 'strain'], loc=1)
plt.xlabel('time (sec)')
plt.ylabel('normalize stress & strain')

stress_75 = TDF_75[:, 2] / A  # kN/cm2
strain_75 = TDF_75[:, 1] / 2.5  # mm

stress_75 = stress_75 / np.amax(stress_75)

strain_75 = strain_75 / np.amax(strain_75)

plt.figure()
plt.plot(TDF_75[:, 0], stress_75, TDF_75[:, 0], strain_75)
plt.title('7.5mm Time history of stress and strain')
plt.legend(['stress', 'strain'], loc=1)
plt.xlabel('time (sec)')
plt.ylabel('normalize stress & strain')
plt.show()

delta_t = TDF_75[np.argmax(stress_75), 0] - TDF_75[np.argmax(strain_75), 0]

omega = 2 * math.pi * 0.303
delta = omega * delta_t

G_a =
