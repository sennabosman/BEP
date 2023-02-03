import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

all_data = pd.DataFrame({'1': [np.NaN, np.NaN, 1092, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, 1092, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, 1092, np.NaN, np.NaN, np.NaN, np.NaN, 1092, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, 1092, 1092, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, 1259, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, 1259, 1259, np.NaN, 1092, np.NaN, 1092, 1257, np.NaN, np.NaN, np.NaN, 1259, np.NaN, np.NaN, np.NaN, np.NaN, 1259, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN],
                         '2': [225, 313, 315, 226, 313, 225, 313, 225, 315, 315, 313, 313, 315, 313, 311, 315, 315, 315, 315, 313, 313, 225, 315, 315, 313, 313, 313, 225, 313, 313, 225, 315, 313, 315, 313, 315, 225, 315, 225, 315, 225, 420, 313, 225, 315, 226, 313, 419, 315, 315, 313, 313, 315, 313, 313, 225, 225, 315, 313, 225, 313, 316, 313, 315, 313, 315, 313, 417, 313, 225, 315, 315, 313, 315, 311, 311, 225, 225, 225, 315, 315, 315, 313, 315, 225, 225, 225, 225, 225, 315, 313, 315, 225, 315, 315, 313, 313, 315, 313, 315],
                         '3': [374, 268, 374, 372, 270, 374, 372, 374, 374, 268, 372, 376, 270, 374, 374, 374, 270, 268, 270, 268, 372, 374, 372, 270, 270, 374, 374, 268, 270, 270, 270, 268, 372, 376, 372, 180, 268, 374, 370, 270, 373, 372, 374, 270, 268, 268, 270, 498, 270, 270, 268, 270, 270, 374, 374, 374, 372, 270, 270, 372, 268, 372, 372, 268, 496, 268, 372, 270, 270, 268, 372, 374, 270, 498, 370, 268, 372, 372, 372, 268, 268, 268, 270, 266, 266, 498, 270, 374, 374, 374, 498, 268, 270, 374, 268, 270, 372, 374, 270, 374],
                         '4': [540, 541, 541, 661, 540, 540, 540, 541, 541, 433, 541, 433, 433, 540, 659, 432, 541, 541, 540, 540, 541, 433, 433, 659, 540, 540, 541, 661, 540, 541, 541, 540, 541, 540, 433, 541, 540, 541, 540, 540, 540, 541, 539, 541, 540, 541, 432, 540, 433, 540, 433, 541, 540, 540, 540, 541, 539, 541, 433, 540, 659, 541, 540, 540, 541, 540, 660, 433, 540, 541, 660, 540, 541, 540, 540, 539, 432, 540, 433, 433, 433, 433, 541, 540, 539, 660, 791, 541, 540, 540, 542, 540, 540, 539, 433, 541, 660, 660, 433, 541],
                         '5': [660, 793, 661, 660, 541, 661, 661, 661, 541, 541, 660, 541, 541, 791, 541, 661, 541, 793, 661, 541, 541, 660, 541, 789, 660, 661, 660, 541, 661, 661, 792, 660, 541, 792, 661, 660, 541, 660, 661, 660, 432, 661, 661, 791, 541, 541, 792, 661, 541, 541, 661, 793, 793, 661, 792, 661, 661, 661, 541, 541, 661, 539, 541, 661, 660, 662, 541, 660, 661, 541, 789, 432, 793, 541, 660, 660, 661, 661, 661, 541, 660, 661, 661, 791, 541, 661, 791, 539, 541, 660, 939, 541, 539, 661, 661, 661, 660, 791, 541, 661],
                         '6': [1088, 600, 826, 826, 826, 711, 602, 707, 602, 828, 604, 828, 826, 826, 600, 604, 1088, 602, 826, 503, 504, 828, 602, 602, 604, 603, 604, 602, 604, 604, 829, 828, 604, 505, 604, 602, 1088, 604, 828, 602, 602, 824, 826, 824, 828, 829, 826, 712, 604, 602, 711, 829, 1088, 709, 1084, 828, 604, 604, 604, 709, 826, 828, 602, 826, 828, 604, 604, 503, 709, 824, 602, 602, 709, 604, 956, 828, 604, 412, 602, 829, 602, 602, 602, 828, 828, 604, 600, 829, 604, 828, 823, 602, 602, 602, 824, 826, 828, 1084, 712, 1088],
                         '7': [124, 124, 125, 125, 124, 125, 125, 125, 125, 124, 124, 124, 124, 124, 124, 124, 124, 124, 125, 125, 124, 125, 124, 125, 125, 124, 125, 125, 125, 125, 125, 124, 124, 124, 125, 124, 125, 124, 124, 124, 124, 125, 124, 124, 124, 124, 125, 124, 125, 124, 125, 125, 124, 124, 125, 125, 124, 125, 125, 124, 125, 125, 125, 124, 124, 125, 124, 125, 125, 125, 125, 125, 124, 124, 124, 125, 124, 124, 125, 124, 125, 124, 125, 125, 125, 125, 125, 125, 125, 125, 125, 124, 125, 125, 125, 124, 125, 125, 125, 124]})
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
ax1.set_title('Gevoeligheidsanalyse - Uitvoering 4')
ax1.set_xlabel('Drone')
ax1.set_ylabel('Vindtijd [s]')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.spines['left'].set_visible(False)

ax1.tick_params(axis='both', which='both', length=0)

plt.savefig(f'Data/GVAUITV4.pdf')