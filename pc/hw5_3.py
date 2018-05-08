import math

# step 1
A_over_t = 3.05 / 0.022

# step 2
period_s = 0.2792


fs_1 = 1 / period_s
f_1 = 1 / 0.3290  # HZ
T = 20  # c
gamma = 3
xi_c = 0.02

k_d = 8.57 * (f_1 ** 0.3) * (gamma ** (-0.24)) * \
    math.exp(-0.073 * T) * 1e1 * (A_over_t)  # tf / m

c_d = 2.18 * (f_1 ** (-0.53)) * (gamma ** (-0.089)) * \
    math.exp(-0.1 * T) * 1e1 * (A_over_t)  # tf / m

eta_v = 2 * math.pi * f_1 * c_d / k_d

omega_r_square = (2 * math.pi * f_1) ** 2

omega_sr_square = (2 * math.pi * fs_1) ** 2

xi_r = xi_c + (eta_v - 2 * xi_c) / 2 * (1 - omega_r_square / omega_sr_square)

print('Step 1')
print('Kd:', k_d)
print('Cd:', c_d)
print('eta_v:', eta_v)
print('')
print('Step 2')
print('xi_r:', xi_r)
print('')
