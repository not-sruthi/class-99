import os
import shutil

folder = input("Enter a folder name to organise: ")
filelist = os.listdir(folder)
folder = folder + '/'

for i in filelist:
    exist = os.path.exists(i)
    name, ext = os.path.splitext(i)

    #ext = ext[1:]

    if ext == '':
        continue

    if os.path.exists(folder + ext):
        shutil.move(folder + i, folder + ext + '/' + i)    
    else:
        os.mkdir(folder + ext)
        shutil.move(folder + i, folder + ext + '/' + i)