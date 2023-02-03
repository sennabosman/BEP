import matplotlib.pyplot as plt
import numpy as np
from matplotlib.transforms import Affine2D

drones = ['1', '2', '3', '4', '5', '6', '7']

basisslecht = [982.93, 746.59, 399.63, 327.76, 391.51, 895.43, 152.16]
minslecht = [449.93, 314.59, 98.63, 55.76, 119.51, 322.43, 48.16]
maxslecht = [371.07, 514.41, 119.37, 108.24, 46.49, 1107.57, 98.84]

uitv3 = [1048.80, 450.74, 524.85, 413.89, 461.42, 1235.88, 180.44]
minuitv3 = [278.8, 122.74, 130.85, 145.89, 129.42, 564.88, 51.44]
maxuitv3 = [200.2, 258.26, 466.15, 159.11, 204.58, 842.12, 87.56]

uitv4 = [1163.43, 294.86, 327.43, 534.39, 642.68, 722.41, 124.54]
minuitv4 = [71.43, 69.86, 147.43, 102.39, 210.68, 310.41, 0.54]
maxuitv4 = [95.57, 125.14, 170.57, 256.61, 296.32, 365.59, 0.46]

fig, (ax1) = plt.subplots(nrows=1, ncols=1, figsize=(8, 5))

trans1 = Affine2D().translate(-0.18, 0.0) + ax1.transData
trans2 = Affine2D().translate(+0.18, 0.0) + ax1.transData

ax1.scatter(x=drones, y=uitv4, color='#1E90FF', label='Verzwakt slecht weer', transform=trans1)
ax1.scatter(x=drones, y=basisslecht, color='#ff1b22', label='Slecht weer')
ax1.scatter(x=drones, y=uitv3, color='#9400D3', label='Versterkt slecht weer', transform=trans2)

ax1.errorbar(x=drones, y=uitv4, yerr=[minuitv4, maxuitv4], color='#1E90FF', ls='None', capsize=5, transform=trans1)
ax1.errorbar(x=drones, y=basisslecht, yerr=[minslecht, maxslecht], color='#ff1b22', ls='None', capsize=5)
ax1.errorbar(x=drones, y=uitv3, yerr=[minuitv3, maxuitv3], color='#9400D3', ls='None', capsize=5, transform=trans2)

ax1.yaxis.grid(True)
ax1.set_title('Gevoeligheidsanalyse - Slecht weer')
ax1.set_xlabel('Drone')
ax1.set_ylabel('Vindtijd [s]')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.legend()

ax1.tick_params(axis='both', which='both', length=0)
#plt.show()
plt.savefig(f'Data/GVASLW.pdf')