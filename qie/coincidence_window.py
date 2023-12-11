import numpy as np
from scipy.optimize import curve_fit 
import matplotlib.pyplot as plt

# T = 2 # s  
# n1 = np.array([19553, 146961, 213710, 107925, 49942, 29835, 39147, 53680, 45013, 43671, 48519,
#                 50684, 81763, 30454, 35898, 49119, 44504, 184064, 401154, 193207, 11793, 18039], dtype=float)
# n2 = np.array([102167, 291071, 81106, 71895, 63354, 48076, 91327, 221865, 43020, 9911, 10447,
#                 10909, 78012, 73067, 92743, 151412, 119926, 267373, 414330, 298298, 224098, 20207], dtype=float)
# ydata = np.array([114, 521, 294, 113, 84, 30, 48, 171, 35, 7, 12, 9, 174, 28, 56, 9, 92, 939, 2659, 1214, 441, 12])

# T = 10 # s
# n1 = np.array([220044, 223322, 109982, 89342, 131964, 70465, 293019, 107710, 39961, 42109], dtype=float)
# n2 = np.array([457080, 989233, 260738, 105084, 98249, 114322, 65528, 36453, 28850, 32668], dtype=float)
# ydata = np.array([356, 797, 166, 29, 39, 34, 58, 32, 7, 8])

# T = 5 # s
# n1 = np.array([142760, 258279, 169757, 39913, 27787, 24742, 25651, 24711, 17565, 5821], dtype=float)
# n2 = np.array([221961, 334811, 438789, 712365, 403575, 154629, 196064, 134846, 72385, 34848], dtype=float)
# ydata = np.array([222, 554, 436, 191, 91, 27, 28, 25, 11, 2])

T = 5 # s
n1 = np.array([55112, 59738, 60022, 67441, 53016, 41287, 57559, 88656, 78627, 103641], dtype=float)
n2 = np.array([27384, 32670, 27422, 20589, 19789, 17792, 15768, 13142, 9929, 5638], dtype=float)
ydata = np.array([11, 14, 12, 5, 10, 9, 9, 9, 4, 10])

xdata = n1 * n2 / T

err = np.sqrt(ydata)

# print(err)

def f(x, tau):
    return tau * x 

def rcs(expected, observed, err, num_params=1):
    return np.sum((expected - observed) ** 2/ err ** 2) / (len(observed)-num_params)

popt, pcov = curve_fit(f, xdata, ydata, sigma = err)
tau = popt[0]
tau_err = np.sqrt(pcov[0][0])
print(tau * 10 ** 9, "+/-", tau_err * 10 ** 9, "ns")
print('RCS:', rcs(ydata, f(xdata, tau), err))
plt.errorbar(xdata, ydata, err,linestyle='none', marker='.')
# plt.plot(xdata, ydata, linestyle='none', marker='.')
plt.plot(xdata, f(xdata, tau))
plt.xlabel("Product of raw counts divided by sampling window ($s^{-1}$)")
plt.ylabel("Coincidence counts")
plt.title(f"Coincidence window $\\tau$ = {round(tau* 10 ** 9)} $\\pm$ {round(tau_err* 10 ** 9)} ns, RCS = {round(rcs(ydata, f(xdata, tau), err), 1)}")
plt.savefig("coincidence.pdf")
plt.show()