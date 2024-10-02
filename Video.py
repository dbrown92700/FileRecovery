import os
import pickle

def s(name, lst):
    for x in lst:
        if name in x:
            print(x)

new_walk = os.walk('/media/db/Elements8/Movies_TV/Movies')
new = [files for (root, dirs, files) in new_walk]
new_list = []
for y in new:
    for x in y:
        if ('.mp4' in x) or ('.mkv' in x) or ('.avi' in x):
            new_list.append(x)

# new_walk = os.walk('/media/db/Elements/Movies_TV/Adult Movies')
# new = [files for (root, dirs, files) in new_walk]
# for y in new:
#     for x in y:
#         if ('.mp4' in x) or ('.mkv' in x):
#             new_list.append(x)

old = pickle.load(open('Movies_TV.pickle', 'rb'))
old_list = []
for y in old:
    if '/media/db/Elements/Movies_TV/Movies/' in y:
        for x in old[y]:
            if ('.mp4' in x) or ('.mkv' in x) or ('.avi' in x):
                old_list.append(x.removesuffix('.L0CK3D'))

missing = []
for x in set(old_list):
    if x not in new_list:
        missing.append(x)

print(f'\n\n\n\nMissing: {len(missing)}')
for x in missing:
    print(x)

extra = []
for x in set(new_list):
    if x not in old_list:
        extra.append(x)

print(f'\n\n\n\nExtra: {len(extra)}')
for x in extra:
    print(x)
