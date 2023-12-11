import numpy as np
from uncertainties import ufloat

N_0_0, N_0_90, N_90_90, N_45_45 = 74, 24, 81, 72

C = N_0_90
A = N_0_0 + N_90_90 - 2 * C
Aerr = np.sqrt(N_0_0 + N_90_90 + 2 * C)

# remember to convert to degrees
def dff_arctan_sqrt(x):
    return (180 / np.pi) / (np.sqrt(x) * (2*x+2))

def diff_arccos(x):
    return - (180 / np.pi) / np.sqrt(1-x**2)
theta = (180 / np.pi) * np.arctan(np.sqrt((N_90_90 - C)/(N_0_0 - C)))

theta_err = np.abs(dff_arctan_sqrt((N_90_90 - C)/(N_0_0 - C))) * np.sqrt( N_90_90 * (1 / (N_0_0 - C)) ** 2
 + N_0_0 * ((N_90_90 - C)/(N_0_0 - C) ** 2) ** 2 + C * ((- N_0_0 + N_90_90 ) / (N_0_0 - C) **2) ** 2)


#  the program didn't like uncertainty in arccos, it is not well behaved
# phi = (180 / np.pi) * np.arccos(((4 / A) * (N_45_45 - C) - 1) / np.sin(2 * theta))
# print(np.abs(diff_arccos(((4 / A) * (N_45_45 - C) - 1) / np.sin(2 * theta))))
# phi_err = np.abs(diff_arccos(((4 / A) * (N_45_45 - C) - 1) / np.sin(2 * theta))) * np.sqrt(
#     ((4 *Aerr/ A ** 2 / np.sin(2 * theta)) * (N_45_45 - C)) ** 2 + N_45_45 * (4 / A / np.sin(2 * theta)) ** 2 
#     + C * (4 / A / np.sin(2 * theta)) ** 2 
#     + (theta_err * (2 * np.cos(2 * theta)) * ((4 / A) * (N_45_45 - C) - 1) / np.sin(2 * theta) ** 2) ** 2)

cos_phi = ((4 / A) * (N_45_45 -C) - 1) / np.sin(2 * theta)

cos_phi_err = np.abs(cos_phi) * np.sqrt( 1 / (N_45_45 + C) + (Aerr / A) ** 2 + (theta_err * 2 * np.cos(2 * theta) / np.sin(2 * theta) ** 2) ** 2)
print("theta:", theta, "+/-", theta_err)
print("cos(phi):", cos_phi, "+/-", cos_phi_err)

print(theta_err * 2 * np.cos(2 * theta) / np.sin(2 * theta) ** 2)