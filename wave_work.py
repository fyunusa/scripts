import os
import shutil


# source = os.listdir('C:/Users/fyunu/Downloads')
destination = ('C:/Users/fyunu/OneDrive/Desktop/Python/new_folder')

# getting all filenames that ends with a particular format
# file_format =  input("please input the  fileformat you wish to copy: (eg. .mp4, .png, .wav) and press Enter ")

# for filename in source:
#     if filename.endswith(file_format):
#         dst_dir =  destination 
#         shutil.copy(filename,dst_dir)
def get_connected_drives():
   
    connected_drives = []
    for drive in range(ord('A'), ord('Z')+1):
        if(os.path.exists(chr(drive) + ':')):
            connected_drives.append(chr(drive) + ':')
    return connected_drives
            # print(connected_drives)
def main():
    available_drives = get_connected_drives()
    if (available_drives):
        print (available_drives)
        # destination = input("The following drives are available:{0}\n Enter the letter of the back-up drive(eg. E: or C:) and press Enter ".format(available_drives)).upper()
        for name in available_drives:
            if name==('F:'):
                for folderName, subfolders, items in os.walk(name):
                    print(items)
                    for files in items:
                        if files.endswith(".mp4"):
                            dst_dir = "C:/Users/fyunu/OneDrive/Desktop/Python/new_folder"
                            print(files)
                           
                            # 
                            # print(files)
                        # for folders in folderName:
                        #     print(folders)
                        #     # if folders.endswith(file_format):
                        #     #     shutil.copy(folders,dst_dir)
                        #     for sub in subfolders:
                        #         print(sub)
                                # if sub.endswith(file_format):
                                #     shutil.copy(sub,dst_dir)
                        
                # for filename in os.listdir(name):
                #     print(filename)
                #     for files in filename:
                        # print(files)
                        # file_format = "mp4"
                        # if files.endswith(file_format):
                        #     dst_dir = "C:/Users/fyunu/OneDrive/Desktop/Python/new_folder"
                        #     shutil.copy(files,dst_dir)
if __name__ == '__main__':
    main()




# file_format = ".mp4"
# for filename in os.listdir('C:/Users/fyunu/OneDrive/Desktop/Python'):
#     if filename.endswith(file_format):
#         dst_dir = "C:/Users/fyunu/OneDrive/Desktop/Python/new_folder"
#         shutil.copy(filename,dst_dir)