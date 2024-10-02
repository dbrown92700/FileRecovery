import os
import pickle

new_walk = os.walk('/media/db/Elements8/Books/ComicsLibrary')
new = [files for (root, dirs, files) in new_walk]
new_list = []
for y in new:
    for x in y:
        if ('.cbr' in x) or ('.cbz' in x):
            new_list.append(x)

old = pickle.load(open('ComicBooksLibrary.pickle', 'rb'))
old_list = []
for y in old:
    for x in old[y]:
        if ('.cbr' in x) or ('.cbz' in x):
            old_list.append(x.removesuffix('.L0CK3D'))

for x in old_list:
    if x not in new_list:
        print(x)
