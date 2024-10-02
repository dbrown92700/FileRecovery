import os
import pickle

new_walk = os.walk('/media/db/Elements8/Books/MainBooksLibrary')
new = [files for (root, dirs, files) in new_walk]
new_list = []
for y in new:
    for x in y:
        if ('.epub' in x):
            new_list.append(x)

old = pickle.load(open('MainBooksLibrary.pickle', 'rb'))
old_list = []
for y in old:
    for x in old[y]:
        if ('.epub' in x):
            old_list.append(x.removesuffix('.L0CK3D'))

for x in old_list:
    if x not in new_list:
        print(x)

