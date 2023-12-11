import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16}) # change plot font size

PATH = 'knot/rog/img/'

xdata = [40, 50, 55, 60, 80, 100, 120, 140]
ydata = [1.21, 1.62, 1.61, 1.059, 0.957, 1.24, 1.31, 1.324]
yerr = [0.02, 0.02, 0.02, 0.008, 0.004, 0.01, 0.01, 0.008]


plt.vlines(x=57.5, ymin=0.9, ymax=1.7, linestyle='--', color='black', alpha=0.4)
plt.vlines(x=80, ymin=0.9, ymax=1.7, linestyle='--', color='black', alpha=0.4)
plt.ylim(0.9,1.7)
plt.errorbar(xdata, ydata, yerr, marker='.', linestyle='none', label="Data")
plt.xlabel("Chain length (number of beads)")
plt.ylabel("Equilibrium radius of gyration (cm)")
plt.title("Equilibrium radius of gyration vs chain length")
plt.grid(alpha=0.5)
plt.savefig(PATH + "rog_v_N", dpi=300, bbox_inches='tight')
plt.show()