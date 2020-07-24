import sys
import os
import shutil
from os import rename, listdir

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)
        
# setting
base_path = 'C:/Users/jsj/Desktop/project/look_like_dog/dataset/' + 'labels'
folder_list = os.listdir(base_path)

train_path = 'C:/Users/jsj/Desktop/project/look_like_dog/dataset/' + 'train_set'
createFolder(train_path)


# copy and rename
for folder in folder_list:
    folder_path = base_path + '/' + folder
    if not os.path.isdir(folder_path):
        continue
    
    dst_path = train_path + '/' + folder
    createFolder(dst_path)
    
    file_list = os.listdir(folder_path)
    n = 1
    for file in file_list:
        src = folder_path + '/' + file
        dst = dst_path + '/' + str(n) + '.jpg'
        shutil.copy(src, dst)    
        n += 1

print('rename and copy complete!!')