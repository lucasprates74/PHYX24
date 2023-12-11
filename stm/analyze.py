import numpy as np
import matplotlib.pyplot as plt

# height data set in angstroms
df = 10 ** 10 * np.loadtxt("graphite_lattice.csv", delimiter=';', dtype=float)  # angstroms
size = len(df)  # number of points per line
img_size = 42.7 # angstroms 

# test to make sure data is being read correctly
plt.contour(df, levels=300)
plt.colorbar()
plt.show()

df_fft = []
freq = []


freq = np.fft.rfftfreq(size, d=42.7 / size)

for j in range(size):
    df_fft.append(np.fft.rfft(df[j]))    

peaks = np.abs(df_fft[0])

print(freq[np.argmax(peaks)])
num_atoms = 0.5 * freq[np.argmax(peaks)] ** -1 # atmoic radius in angstrom
print(num_atoms)

plt.plot(freq, np.abs(df_fft[0]))   
plt.show()