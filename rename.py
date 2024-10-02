import os
import pickle

def s(name, lst):
    for x in lst:
        if name in x:
            print(x)

new_walk = os.walk('/media/db/Elements8/Movies_TV/Movies')
new = [{root: files} for (root, dirs, files) in new_walk]
new_list = {}
for directory in new:
    d = list(directory.keys())[0]
    for file in directory[d]:
        if ('.mp4' in file) or ('.mkv' in file) or ('.avi' in file):
            new_list[file] = list(directory.keys())[0]
            # print(file)

rename = {}
with open('rename.csv') as f:
    for line in f.readlines():
        [old_name, new_name] = line.removesuffix('\n').split(',')
        if old_name[-4:] != new_name[-4:]:
            print(line)
            continue
        try:
            print(f'{new_list[old_name]}/{old_name} --> {new_list[old_name]}/{new_name}')
            os.rename(f'{new_list[old_name]}/{old_name}', f'{new_list[old_name]}/{new_name}')
        except KeyError:
            # print(f'{old_name} KEY ERROR')
            continue

