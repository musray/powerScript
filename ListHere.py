import os
import datetime
import time

def should_ignore(file):
    status = False 
    ignore_list = ['.git', 'file_list', 'listhere']
    for ig in ignore_list:
        if ig in file:
            status = True
    return status

target = r'H:\EAST_Project\TestProject\TestProject'
walker = os.walk(target)

items = list(walker)

all_files = []
for item in items:
    this_root = item[0]
    for file in item[2]:
        file_full_name = os.path.join(this_root, file)
        all_files.append(file_full_name)


dest_dir = os.getcwd()
name_leading = time.strftime("%Y_%m_%d_%H_%M_%S")

with open(os.path.join(dest_dir, 'file_list', name_leading + '_file_list.txt'), 'w') as f:
    for file in all_files:
        if not should_ignore(file):
            f.write(file)
            f.write('\n')






