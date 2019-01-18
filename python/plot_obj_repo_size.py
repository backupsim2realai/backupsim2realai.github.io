import numpy as np
import matplotlib.pyplot as plt
import operator
from collections import OrderedDict

dataset_dict={'3D Warehouse':4000000,
'3dMdb': 3040000,
'GrabCAD':  2840000,
'STLFinder': 2000000,
'Sketchfab':    1500000,
'Yeggi':        1498000,
'Thingiverse': 1068080,
'Yobi3D': 1000000,
'IFind3D':  911047,
'CGTrader': 650000,
'PrintMeASheep': 100000,
'Free3D': 48000}
''',
'My Mini Factory': 45000,
'Cults': 33000,
'Pinshape': 30000,
'TurboSquid':  26800,	
'CGStudio':	26172,
'FlatPyramid':	15500,
'Hum3D':	15354,	
'YouMagine': 14000,
'PARTcloud.net':8500,	
'XYZprinting': 8270,
'3Dupndown':	7800,
'3D Orchard':	6500}
'''

dataset_dict = OrderedDict(sorted(dataset_dict.items(), key=lambda x: x[1]))

dataset_name, datasets_size = list(dataset_dict.keys()), list(dataset_dict.values())
fig, ax = plt.subplots()

ind = np.arange(len(dataset_name))

_fontsize =10

ax.bar(ind, np.array(datasets_size)/1000.0, width=0.35,
       color='aquamarine', #label='datasets'
       )

ax.set_ylabel('Dataset size x 1e3', fontsize=_fontsize)
ax.set_title('Size of object repositories', fontsize=_fontsize)
ax.set_xticks(ind)
ax.set_xticklabels(dataset_name)
ax.legend()

plt.xticks(fontsize=_fontsize, rotation=75)

plt.tight_layout()
plt.show()
