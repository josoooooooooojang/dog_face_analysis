import sys
from os import rename, listdir
import os

rootPath = 'C:\\Users\\조수장\\Desktop\\project\\crawling_example\\dataset\\data'
label_list = ['angry', 'sadness', 'happiness', 'surprised', 'afraid', 'neutral', 'tired', 'wonder', 'etc']

for label in label_list:
    filePath = rootPath + '\\' + label + '\\'
    files = listdir(filePath)

    n = 1
    cnt = 0
    for f in files:
        src = os.path.join(filePath, f)
        dst = label + '_' + str(n) + '.jpg'
        dst = os.path.join(filePath, dst)
        while(os.path.isfile(dst)):
            n += 1
            dst = label + '_' + str(n) + '.jpg'
            dst = os.path.join(filePath, dst)
        os.rename(src, dst)
        n += 1
        cnt += 1

    print('['+ label + ']' + ' data is ' + str(cnt))
    





