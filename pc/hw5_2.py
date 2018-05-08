import math

import matplotlib.pyplot as plt
import numpy as np

n = 2  # 看不懂

cos = 4 / 5

area = 0.09 * 0.11  # m2

thickness = 0.024  # m

mass = 10 * 9.81 * 1e6  # kN

T = 32  # c

G_1 = math.exp(10.17433) * (T ** (-3.10205)) * 1.34840758 * 1e6  # N / m2

eta_v = 1.2

kd = G_1 * area / thickness * n

kv = kd * (cos ** 2)

k_1 = 7e6  # N / m
k_2 = 6.6e6  # N / m
k_3 = 7e6  # N / m

k_1t = k_1 + kv
k_2t = k_2 + kv
k_3t = k_3 + kv

k_total = np.mat([[k_1t + k_2t, -k_2t, 0],
                  [-k_2t, k_3t + k_2t, -k_3t],
                  [0, -k_3t, k_3t]])
print(k_total)

k_e = np.mat([[k_1 + k_2, -k_2, 0],
              [-k_2, k_3 + k_2, -k_3],
              [0, -k_3, k_3]])

phi = np.mat([[0.4451],
              [0.8019],
              [1]])

r = 1

k_s = k_total

phi_r = np.power(phi, r)

xi_r = eta_v / 2 * (1 -
                    (np.transpose(phi_r) * k_e * (phi_r)) /
                    (np.transpose(phi_r) * k_s * (phi_r)))

print(xi_r)

omega_r_squre = np.linalg.eig(k_e)[0][0] / mass

omega_sr_squre = np.linalg.eig(k_s)[0][0] / mass

xi_r = eta_v / 2 * (1 - omega_r_squre / omega_sr_squre)

print(xi_r)
