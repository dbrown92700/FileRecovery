import os
import subprocess
from tkinter.tix import Shell

logfile =  '/media/db/Elements8/Movies_TV/AVIs/log.log'
root_dir = '/media/db/Elements8/Movies_TV/Movies'
archive_dir = '/media/db/Elements8/Movies_TV/AVIs'

new_walk = os.walk(root_dir)
new = [{root: files} for (root, dirs, files) in new_walk]
for x in new:
    dir = list(x.keys())[0]
    files = x[dir]
    for file in files:
        if file[-4:] == '.avi':
            mkv_file = file[0:-4] + '.mkv'
            if mkv_file in files:
                os.rename(f'{dir}/{file}', f'{archive_dir}/{file}')
                with open(logfile, 'a') as f:
                    f.write(f'{dir}/{file} MOVED\n')
                continue
            srt_file = file[0:-4] + '.srt'
            if srt_file in files:
                subrip = f'-i "{dir}/{srt_file}" -c:s subrip '
            else:
                subrip = ''
            command = f'ffmpeg -i "{dir}/{file}" {subrip} "{dir}/{file[0:-4]}.mkv"'
            print(command)
            os.system(command)
            os.rename(f'{dir}/{file}', f'{archive_dir}/{file}')
            with open(logfile, 'a') as f:
                f.write(f'{dir}/{file} CONVERTED\n')
            if srt_file in files:
                os.rename(f'{dir}/{srt_file}', f'{archive_dir}/{srt_file}')