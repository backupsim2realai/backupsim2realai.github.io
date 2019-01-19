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
'Clara': 100000,
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

dataset_dict={
        'table': 8443,
        'car': 7497,
        'chair': 6778,
        'airplane':4045,
        'sofa': 3173,
        'rifle': 2373,
        'lamp': 2318,
        'watercraft': 1939,
        'bench': 1816,
        'loudspeaker': 1618,
        'cabinet': 1572,
        'display': 1095,
        'telephone': 1052,
        'bus': 939,
        'bathtub': 857,
        'guitar': 797,
        'faucet': 744,
        'clock': 655,
        'flowerpot': 602,
        'jar': 597,
        'bottle': 498,
        'bookshelf': 466,
        'laptop': 460,
        'knife': 424,
        'train': 389,
        'trash bin': 343,
        'motorbike': 337,
        'pistol': 307,
        'file cabinet': 298,
        'bed': 254,
        'piano': 239,
        'stove': 218,
        'mug': 214,
        'bowl': 186,
        'washer': 169,
        'printer': 166,
        'helmet': 162,
        'microwave': 152,
        'stakeboard': 152,
        'tower': 133,
        'camera': 113,
        'basket': 113,
        'can': 108,
        'pillow': 96,
        'mailbox': 94,
        'dishwasher': 93,
        'rocket': 85,
        'bag': 83,
        'birdhouse': 73,
        'earphone': 73,
        'microphone': 67,
        'remote': 67,
        'keyboard': 65,
        'bicycle': 59,
        'cap': 56
        }


dataset_dict = OrderedDict(sorted(dataset_dict.items(), key=lambda x: x[1]))

dataset_name, datasets_size = list(dataset_dict.keys()), list(dataset_dict.values())
fig, ax = plt.subplots()

ind = np.arange(len(dataset_name))

_fontsize =10

#ax.bar(ind, np.array(datasets_size)/1000.0, width=0.35,
#       color='aquamarine', #label='datasets'
#       )

ax.bar(ind, np.array(datasets_size), width=0.35,
       color='aquamarine', #label='datasets'
       )
#ax.set_ylabel('Dataset size x 1e3', fontsize=_fontsize)
ax.set_ylabel('Number of Instances', fontsize=_fontsize)
ax.set_title('Number of Objects', fontsize=_fontsize)
ax.set_xticks(ind)
ax.set_xticklabels(dataset_name)
ax.legend()

#ax.axhline(y=1000,linestyle='dotted')
#plt.text(4, 1200, '1 million models', fontsize=_fontsize, va='center', ha='center', color='blue')

plt.xticks(fontsize=_fontsize, rotation=75)

plt.tight_layout()
plt.show()
