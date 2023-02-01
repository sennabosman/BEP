import matplotlib.pyplot as plt
import numpy as np
from matplotlib.transforms import Affine2D

drones = ['1', '2', '3', '4', '5', '6', '7']

vindtijdgow = [671.97, 251.24, 234, 214.26, 230.54, 1220.85, 146.44]
mingow = [238.97, 57.24, 4, 61.26, 0.54, 559.85, 64.44]
maxgow = [368.03, 156.76, 113, 17.74, 0.46, 1064.15, 15.56]

vindtijdgew = [746.2, 265.62, 297.93, 257.16, 315.84, 641.05, 115.15]
mingew = [172.2, 37.62, 11.93, 64.16, 47.84, 198.05, 47.15]
maxgew = [256.8, 59.38, 106.07, 104.84, 147.16, 381.95, 17.85]

vindtijdslw = [982.93, 746.59, 399.63, 327.76, 391.51, 895.43, 152.16]
minslw = [449.93, 314.59, 98.63, 55.76, 119.51, 322.43, 48.16]
maxslw = [371.07, 514.41, 119.37, 108.24, 46.49, 1107.57, 98.84]

fig, (ax1) = plt.subplots(nrows=1, ncols=1, figsize=(8, 5))

trans1 = Affine2D().translate(-0.18, 0.0) + ax1.transData
trans2 = Affine2D().translate(+0.18, 0.0) + ax1.transData

ax1.scatter(x=drones, y=vindtijdgow, color='#1ecc4c', label='Goed weer', transform=trans1)
ax1.scatter(x=drones, y=vindtijdgew, color='#ffca1b', label='Gemiddeld weer')
ax1.scatter(x=drones, y=vindtijdslw, color='#ff1b22', label='Slecht weer', transform=trans2)
ax1.errorbar(x=drones, y=vindtijdgow, yerr=[mingow, maxgow], color='#1ecc4c', ls='None', capsize=5, transform=trans1)
ax1.errorbar(x=drones, y=vindtijdgew, yerr=[mingew, maxgew], color='#ffca1b', ls='None', capsize=5)
ax1.errorbar(x=drones, y=vindtijdslw, yerr=[minslw, maxslw], color='#ff1b22', ls='None', capsize=5, transform=trans2)


ax1.yaxis.grid(True)
ax1.set_title('Experiment 2')
ax1.set_xlabel('Drone')
ax1.set_ylabel('Vindtijd [s]')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.legend()

ax1.tick_params(axis='both', which='both', length=0)
#plt.show()
plt.savefig(f'Data/EXP2.pdf')