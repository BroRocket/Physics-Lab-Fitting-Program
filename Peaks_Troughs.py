from scipy import signal
from pylab import loadtxt
import matplotlib.pyplot as plt
import numpy as np

filename = "FrankHertzData.txt"

data = loadtxt(filename, usecols=(1,3), skiprows=0, unpack=True)
xdata = data[1]
ydata = data[0]

peaks, _ = signal.find_peaks(ydata, distance=100)
troughs, _ = signal.find_peaks(x=-ydata, distance=100)

Vmax = [[],[]]
Vmin = [[],[]]

print(peaks)
print(troughs)
for i in peaks: Vmax[0].append(xdata[i]), Vmax[1].append(ydata[i])
for i in troughs: Vmin[0].append(xdata[i]), Vmin[1].append(ydata[i])
print(Vmax)
print(Vmin)

plt.plot(xdata, ydata, label="Data")
plt.scatter(Vmax[0], Vmax[1], label="Peaks", color="red")
plt.scatter(Vmin[0], Vmin[1], label="Troughs", color="green")
plt.legend(loc='lower right')
plt.xlabel("Accelerating Voltage (V)")
plt.ylabel("Current (A)")
plt.title("Current Vs. Voltage Peaks and Troughs")
plt.show()

Vmax_diff = np.diff(Vmax[0])
Vmin_diff = np.diff(Vmin[0])
print(Vmax_diff)
print(Vmin_diff)

Vmax_mean = Vmax_diff.mean()
Vmin_mean = Vmin_diff.mean()
print(Vmax_mean)
print(Vmin_mean)

Vmax_std = Vmax_diff.std() / np.sqrt(len(peaks))
Vmin_std = Vmin_diff.std() / np.sqrt(len(troughs))
print(Vmax_std)
print(Vmin_std)

joint = []
for i in range(len(Vmax_diff)): joint.append(Vmax_diff[i])
for i in range(len(Vmin_diff)): joint.append(Vmin_diff[i])
joint_mean = np.mean(joint)
joint_std = np.std(joint) / np.sqrt(len(joint))
print(joint_mean, "+/-", joint_std)


