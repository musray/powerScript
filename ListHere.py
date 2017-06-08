import os
import sys
import time


def should_ignore(file):
    status = False 
    ignore_list = ['.git', 'file_list', 'listhere', '.idea']
    for ig in ignore_list:
        if ig in file:
            status = True
    return status


def main(path):
    # 获得一个walk的结果的list
    # list里的每一个元素，是一个len=3的tuple
    # (文件夹绝对路径, [该路径内的文件夹名称], [该路径内的文件名称]])
    items = list(os.walk(path))

    # 准备存储所有的文件
    all_files = []
    # 遍历出每一个tuple
    for item in items:
        # item[0]是每个文件夹的绝对路径
        this_root = item[0]
        # item[2]是item[0]里的所有文件(不含子文件夹中的文件)
        for file in item[2]:
            file_full_name = os.path.join(this_root, file)
            all_files.append(file_full_name)

    dest_dir = os.getcwd()
    # 生成时间标签的字符串
    name_leading = time.strftime("%Y_%m_%d_%H_%M_%S")

    # 新建一个txt文件，将文件全名写入该文件
    with open(os.path.join(dest_dir, 'file_list', name_leading + '_file_list.txt'), 'w', encoding='utf-8') as f:
        for file in all_files:
            # 如果文件名中不包含需要忽略的字符:
            if not should_ignore(file):
                f.write(file)
                f.write('\n')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if os.path.isdir(sys.argv[1]):
            PATH = sys.argv[1]
            main(PATH)
    else:
        main(os.getcwd())

    # for DEBUG
    # PATH = r'H:\EAST_Project\TestProject\TestProject'

