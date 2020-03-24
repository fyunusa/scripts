import fnmatch
import os
import shutil
from threading import Thread

# # drives = ['C:\\','D:\\','E:\\']
# drives = ['E://']
# pattern = "*.wav"
# dst_dir = "C:/Users/fyunu/Downloads/new_folder"

# for rootPath in drives:
#     print ("Now searching in: "),rootPath
#     for root, dirs, files in os.walk(rootPath) :
#         for filename in fnmatch.filter(files, pattern) :
#             shutil.copy(os.path.join(src,dst_dir)
#                 # print (os.path.join(root, filename))
#                 # return filename


drives = ['D:\\']
pattern = "*.mp4"
dst_dir = "C:/Users/fyunu/Downloads/new_folder"


for rootPath in drives:
    print ("Now searching in: "),rootPath
    for root, dirs, files in os.walk(rootPath) :
        for filename in fnmatch.filter(files, pattern) :
            src = filename
            Thread(target=shutil.copy, args=[src, dst_dir]).start()
            # print(filename)
            # shutil.copyfile(filename,target)
            print (os.path.join(root, filename))
           