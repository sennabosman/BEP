import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

all_data = pd.DataFrame({'1': [900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900],
                         '2': [819, 821, 1078, 1081, 821, 821, 821, 1078, 819, 821, 1137, 822, 1079, 1079, 1137, 822, 822, 1076, 1081, 1078, 1079, 1081, 1076, 821, 1079, 1078, 819, 1078, 817, 819, 1078, 1079, 819, 1079, 1076, 1076, 817, 822, 1078, 1139, 822, 1078, 1079, 1079, 822, 822, 821, 1079, 1079, 1077, 816, 822, 821, 1078, 1078, 821, 1079, 1078, 1078, 1079, 1078, 819, 1079, 821, 819, 819, 821, 1076, 1076, 1079, 1078, 822, 821, 1078, 822, 827, 819, 819, 1079, 1081, 763, 819, 819, 1079, 1078, 817, 1135, 1078, 819, 1078, 819, 1079, 1079, 819, 821, 1081, 825, 819, 819, 817],
                         '3': [1370, 1368, 1370, 1438, 1446, 1374, 1368, 1368, 1770, 1448, 1366, 1449, 1366, 1368, 1370, 1770, 1370, 1448, 1446, 1368, 1045, 1368, 1366, 1448, 1448, 1372, 1446, 1368, 1372, 1046, 1370, 1364, 1370, 1446, 1368, 1450, 1370, 1370, 1774, 1772, 1446, 1366, 1368, 1770, 1370, 1772, 1370, 1450, 1370, 1372, 1372, 1370, 1370, 1368, 1776, 1368, 1370, 1368, 1368, 1368, 1368, 1446, 1448, 1446, 1372, 1370, 1368, 1448, 1364, 1370, 1446, 1774, 1776, 1774, 1370, 1770, 1774, 1366, 1370, 1448, 1044, 1368, 1372, 1770, 1368, 1376, 1446, 1372, 1776, 1448, 1458, 1370, 1448, 1370, 1372, 1448, 1370, 1370, 1366, 1368],
                         '4': [1596, 1551, np.NaN, 1546, 1550, 1547, 1547, np.NaN, 1546, np.NaN, np.NaN, 1354, 1548, 1547, 1350, np.NaN, np.NaN, 1551, 1352, np.NaN, np.NaN, 1548, 1546, 1352, np.NaN, 1548, np.NaN, np.NaN, np.NaN, np.NaN, 1550, np.NaN, 1547, np.NaN, 1546, 1547, 1308, np.NaN, np.NaN, 1548, np.NaN, 1357, 1545, np.NaN, np.NaN, np.NaN, np.NaN, 1353, 1356, np.NaN, np.NaN, np.NaN, 1546, 1594, 1550, 1550, np.NaN, 1353, 1546, np.NaN, np.NaN, np.NaN, np.NaN, 1354, 1548, 1353, 1550, 1353, 1550, 1352, 1353, 1354, 1311, np.NaN, 1547, 1550, 1352, 1548, np.NaN, np.NaN, 1548, 1546, 1546, 1595, 1353, np.NaN, np.NaN, 1352, 1546, np.NaN, np.NaN, np.NaN, 1547, np.NaN, 1546, np.NaN, np.NaN, 1306, 1551, np.NaN],
                         '5': [np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, 1690, np.NaN, np.NaN, np.NaN, np.NaN, 1689, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, 1474, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, 1687, np.NaN, np.NaN, np.NaN, np.NaN, 1686, np.NaN, np.NaN, np.NaN, np.NaN, 1690, np.NaN, 1690, np.NaN, np.NaN, np.NaN, 1689, np.NaN, np.NaN, 1477, 1685, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, 1474, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, 1691, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, 1689, np.NaN, np.NaN, np.NaN, np.NaN, 1473, np.NaN, np.NaN, np.NaN, np.NaN, 1685, np.NaN, np.NaN],
                         '6': [900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900],
                         '7': [728, 486, 728, 726, 728, 728, 726, 726, 728, 726, 726, 728, 725, 791, 725, 726, 726, 726, 728, 487, 726, 728, 726, 726, 728, 726, 725, 485, 485, 485, 725, 729, 496, 726, 726, 728, 728, 726, 726, 729, 731, 726, 728, 726, 728, 485, 485, 726, 726, 728, 726, 728, 728, 726, 729, 726, 725, 728, 728, 484, 485, 790, 728, 728, 726, 484, 729, 726, 726, 791, 726, 728, 726, 791, 728, 726, 790, 725, 791, 726, 728, 728, 790, 726, 728, 729, 726, 726, 728, 726, 726, 729, 728, 729, 728, 791, 726, 728, 725, 791]})

data_dict_filtered = {}

for column in all_data:
    column_list = list(all_data[column])
    column_filtered = [int(x) for x in column_list if str(x) != 'nan']
    data_dict_filtered[column] = column_filtered

labels, data = [*zip(*data_dict_filtered.items())]

#labels = ['1', '2', '3', '4', '5', '6', '7']
colors = ['#c718e2', '#fb7b31', '#ffd716', '#ff1d16', '#1683ff', '#00e207', '#fb1983']

#'#43baff'

fig, (ax1) = plt.subplots(nrows=1, ncols=1, figsize=(8, 5))

violin = ax1.violinplot(data, vert=True)

violin['cmaxes'].set_color('#717171')
violin['cmins'].set_color('#717171')
violin['cbars'].set_color('#717171')

for patch, color in zip(violin['bodies'], colors):
    patch.set_facecolor(color)
    patch.set_edgecolor(color)

"""for median in box['medians']:
    median.set_color('dodgerblue')"""

"""for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.3)
    patch.set_edgecolor(color)
    patch.set_linewidth(1)"""

ax1.yaxis.grid(True)
ax1.set_title('Experiment 1 - Slecht weer')
ax1.set_xlabel('Drone')
ax1.set_ylabel('Vindtijd [s]')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.spines['left'].set_visible(False)

ax1.tick_params(axis='both', which='both', length=0)

plt.savefig(f'Data/EXP1SLW.pdf')