import os

logfile =  '/media/db/Elements8/Movies_TV/MP4s/log.log'
root_dir = '/media/db/Elements8/Movies_TV/Movies'
archive_dir = '/media/db/Elements8/Movies_TV/MP4s'

new_walk = os.walk(root_dir)
new = [{root: files} for (root, dirs, files) in new_walk]
for x in new:
    dir = list(x.keys())[0]
    files = x[dir]
    for file in files:
        if file[-4:] == '.srt':
            if f'{file[0:-4]}.mkv' in files:
                with open(logfile, 'a') as f:
                    f.write(f'EXISTS {file[0:-4]}.mkv  Moving SRT & MP4 files\n')
                os.rename(f'{dir}/{file}', f'{archive_dir}/{file}')
                if f'{file[0:-4]}.mp4' in files:
                    os.rename(f'{dir}/{file[0:-4]}.mp4', f'{archive_dir}/{file[0:-4]}.mp4')
                continue
            if f'{file[0:-4]}.mp4' in files:
                command = f'ffmpeg -i "{dir}/{file}" -i "{dir}/{file[0:-4]}.mp4" -c:v copy -c:a copy -c:s subrip "{dir}/{file[0:-4]}.mkv"'
                with open(logfile, 'a') as f:
                    f.write(f'CONVERTING: {command}\n')
                os.system(command)
                os.rename(f'{dir}/{file}', f'{archive_dir}/{file}')
                os.rename(f'{dir}/{file[0:-4]}.mp4', f'{archive_dir}/{file[0:-4]}.mp4')
                continue
            else:
                with open(logfile, 'a') as f:
                    f.write(f'ORPHAN: {dir}/{file}  Moved\n')
                os.rename(f'{dir}/{file}', f'{archive_dir}/{file}')

