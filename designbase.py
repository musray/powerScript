#!/usr/bin/env python3
import os
import shutil
dirs = [
    '1 input',
    '2 reference',
    '3 previous',
    '4 editable',
    '5 import',
    '6 export',
    '7 CheckEvidence',
    '8 互查单',
]

config_skeletron = '''
document title:
19_index:
int_index:
pages:
ied:
    cur_ver: X(channel number)
    revised_ver: X

S/W:
    cur_ver:
    revised_ver:
POL:
    cur_ver:
    revised_ver:
'''

for item in dirs:
    os.mkdir(item)

with open('config.txt', 'w') as f:
    f.write(config_skeletron)

with open('cc文件上传记录.txt', 'w') as cc:
    cc.write('cc文件上传情况记录：')
    cc.write('\n')
