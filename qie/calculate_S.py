import numpy as np

N = np.array([[60, 43, 122, 160], [108, 72, 21, 92], [41, 82, 62, 21], [35, 58, 121, 88]])
N_err = np.sqrt(N)

def E(alpha, beta):
    # get the indeces corresponding to alpha and beta
    i = 1 + int(alpha // 45)
    j = 1 + int((beta-22.5) // 45)

    # get the indeces corresponding to alpha + 90 and beta + 90
    i_perp = i + 2
    j_perp = j + 2
    numerator = N[i, j] + N[i_perp, j_perp] - N[i, j_perp] - N[i_perp, j]
    denominator = N[i, j] + N[i_perp, j_perp] + N[i, j_perp] + N[i_perp, j]
    return numerator / denominator

def E_err(alpha, beta):
    # get the indeces corresponding to alpha and beta
    i = 1 + int(alpha // 45)
    j = 1 + int((beta-22.5) // 45)

    # get the indeces corresponding to alpha + 90 and beta + 90
    i_perp = i + 2
    j_perp = j + 2
    numerator = N[i, j] + N[i_perp, j_perp] - N[i, j_perp] - N[i_perp, j]
    denominator = N[i, j] + N[i_perp, j_perp] + N[i, j_perp] + N[i_perp, j]
    E = numerator / denominator
    # since err_N = sqrt(N)
    numerator_err = np.sqrt(numerator)
    denominator_err = np.sqrt(denominator)
    E_err = (numerator / denominator) * np.sqrt((numerator_err / numerator) ** 2 + (denominator_err / denominator) ** 2)
    return E_err

S = E(-45, -22.5) - E(-45, 22.5) + E(0, -22.5) + E(0, 22.5)
S_err = np.sqrt(E(-45, -22.5) ** 2 + E(-45, 22.5) ** 2 + E(0, -22.5) ** 2 + E(0, 22.5) ** 2)
print(S, "+/-", S_err)