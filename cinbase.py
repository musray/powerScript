import os
import shutil
dirs = [
    '0. CIN Cover and Sheet',
    '1. DEN',
    '2. IO List',
    '3. WD and IF',
    '4. SW (Parameter)',
    '5. 互查单'
]

for item in dirs:
    os.mkdir(item)
