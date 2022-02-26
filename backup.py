import os
import shutil

source = input("Enter the source folder: ")
filelist = os.listdir(source)
source = source + '/'

destination = input("Enter the destination folder: ")
destination = destination + '/'

for i in filelist:
    shutil.copy(source + i, destination)
