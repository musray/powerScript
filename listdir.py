import os
lst = os.listdir('./')
with open('./lst.txt', 'w') as f:
    for item in lst:
        f.write(item)
        f.write('\n')

os.system('notepad.exe lst.txt')
