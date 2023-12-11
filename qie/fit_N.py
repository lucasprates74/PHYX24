import numpy as np  
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def N(beta, theta, phi, A, C):
    """
    A model for the number of conincidence photons for polarizer angle beta
    and a fixed alpha
    """
    return A * ((np.sin(alpha) * np.sin(beta) * np.cos(theta)) ** 2 
              + (np.cos(alpha) * np.cos(beta) * np.sin(theta)) ** 2
              + np.sin(2 * (alpha)) * np.sin(2 * beta) * np.sin(2 * theta) * np.cos(phi)) + C

def N_2D(grid, theta, cos_phi, A, C):
    """
    A model for the number of conincidence photons for polarizer angles alpha and beta
    """
    alpha, beta = grid
    return_arr = []

    for i in range(len(alpha)):
        val = A * ((np.sin(alpha[i]) * np.sin(beta) * np.cos(theta)) ** 2 
              + (np.cos(alpha[i]) * np.cos(beta) * np.sin(theta)) ** 2
              + np.sin(2 * (alpha[i])) * np.sin(2 * beta) * np.sin(2 * theta) * cos_phi) + C
        return_arr.append(val)
    
    return np.array(return_arr).flatten()

def rcs(expected, observed, err, num_params=1):
    return np.sum((expected - observed) ** 2/ err ** 2) / (len(observed)-num_params)


if __name__ == '__main__':
    # alpha = 0
    # xdata = np.arange(0, 190, 10) * np.pi / 180
    # ydata = np.array([94, 88, 81, 69, 72, 62, 44, 22, 26, 22, 
    #                   12, 25, 28, 34, 41, 59, 80, 91, 79])
    # err = np.sqrt(ydata)

    # popt, pcov = curve_fit(N, xdata, ydata, sigma=err, p0=(45, 0, 100, 10))

    # theta, phi, A, C = popt 
    # err_theta, err_phi, err_A, err_C = np.sqrt(np.diag(pcov))

    # print("Theta:", theta, "+/-", err_theta)
    # print("Phi:", phi, "+/-", err_phi)
    # print("A:", A, "+/-", err_A)
    # print("C:", C, "+/-", err_C)
    # print("RCS:", rcs(N(xdata, theta, phi, A, C), ydata, err, num_params=4))

    # plt.errorbar(xdata, ydata, err, marker='.', linestyle='none')

    # beta = np.arange(0, 180, 1) * np.pi / 180
    # plt.plot(beta, N(beta, theta, phi, A, C))
    # plt.show()


    # alpha = 45
    # xdata = np.arange(0, 100, 10) * np.pi / 180
    # ydata = np.array([11, 21, 18, 15, 26, 22, 17, 16, 10, 8])
    # err = np.sqrt(ydata)

    # popt, pcov = curve_fit(N, xdata, ydata, sigma=err, p0=(45 * np.pi / 180, 0, 100, 10))

    # theta, phi, A, C = popt 
    # err_theta, err_phi, err_A, err_C = np.sqrt(np.diag(pcov))

    # print("Theta:", theta, "+/-", err_theta)
    # print("Phi:", phi, "+/-", err_phi)
    # print("A:", A, "+/-", err_A)
    # print("C:", C, "+/-", err_C)
    # print("RCS:", rcs(N(xdata, theta, phi, A, C), ydata, err, num_params=4))

    # plt.errorbar(xdata, ydata, err, marker='.', linestyle='none')

    # beta = np.arange(0, 180, 1) * np.pi / 180
    # plt.plot(beta, N(beta, theta, phi, A, C))
    # plt.show()

    # 2D curve fit
    alpha, beta = np.array([-45, 0, 45, 90]) * np.pi / 180, np.array([-22.5, 22.5, 67.5, 112.5])  * np.pi / 180
    xdata = (alpha, beta)
    ydata = np.array([[60, 43, 122, 160], [108, 72, 21, 92], [41, 82, 62, 21], [35, 58, 121, 88]])
    err = np.sqrt(ydata)
    popt, pcov = curve_fit(N_2D, xdata, ydata.flatten(), sigma=err.flatten(), p0=(45, 0, 100, 10))

    theta, phi, A, C = popt 
    err_theta, err_phi, err_A, err_C = np.sqrt(np.diag(pcov))

    print("Theta:", theta, "+/-", err_theta)
    print("Phi:", phi, "+/-", err_phi)
    print("A:", A, "+/-", err_A)
    print("C:", C, "+/-", err_C)
    print("RCS:", rcs(N_2D(xdata, theta, phi, A, C), ydata.flatten(), err.flatten(), num_params=4))

    # plt.errorbar(xdata, ydata, err, marker='.', linestyle='none')

    beta = np.arange(-22.5, 112.5, 1) * np.pi / 180

