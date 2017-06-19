import os
import fnmatch

def all_files(root, patterns='*', single_level=False, yield_folders=False):
    # patterns: 字符串，多个pattern的话用分号隔开，例如：'*.py;*.js;*.csv'
    # single_level: False，处理root下的所有子文件夹；True，只处理root内一层，不处理其子文件夹
    # yield_folders: False, 是在处理结果中排除文件夹；True, 是在处理结果中包含文件夹

    # 将模式从字符串中取出放入列表
    patterns = patterns.split(';')
    for path, subdirs, files in os.walk(root):
        if yield_folders:
            files.extend(subdirs)
        files.sort()
        for name in files:
            for pattern in patterns:
                if fnmatch.fnmatch(name, pattern):
                    yield os.path.join(path, name)
                    break
        if single_level:
            break

if __name__ == '__main__':

    test_folder = '/Users/churui/Projects/offset/'

    py_files = list(all_files(test_folder, '*.py', False, True))
    csv_files = list(all_files(test_folder, '*.csv'))

    print(len(csv_files))

