import os
import shutil

os.chdir("C:/Users/ZainbaMuhdYunus/Desktop/Python")
# # path = os.getcwd()
 
def get_disk_drives():
    # this works for windows only getting disk drive 
    connected_drives = []
    for drive in range(ord('A'), ord('Z')+1):
        if(os.path.exists(chr(drive) + ':')):
            connected_drives.append(chr(drive) + ':')
    return connected_drives

def main():
    available_drives = get_disk_drives()
    Options = input("how do you want to perform your operation? \n A--> Drive to pc \n B--> pc to drive \n C--> pc to pc \n Answer: ")
    Options = Options.upper()

    if Options == "A":
        if (available_drives):
            destination = input("The following drives are available:{0}\n Enter the letter of the back-up drive(eg. E: or C:) and press Enter ".format(available_drives)).upper()

            # getting all filenames that ends with a particular format
            file_format = ""
            file_format =  input("please input the  fileformat you wish to copy:{1}\n (eg. .mp4, .png, .wav) and press Enter ".format(file_format)).upper()

            for filename in available_drives:
                if filename.endswith(file_format):
                    dst_dir = "C:/Users/ZainbaMuhdYunus/Desktop/Python/new_folder"
                    shutil.copy(filename,dst_dir)
        else:
            raise Exception("No Valid Drive was detected")
        

    elif Options =="B":
        if (available_drives):
            destination = input("The following drives are available:{0}\n Enter the letter of the back-up drive(eg. E: or C:) and press Enter ".format(available_drives)).upper()
        # source directory
            src_dir = "C:/Users/ZainbaMuhdYunus/Desktop/Python"

            file_format = ""
            file_format =  input("please input the  fileformat you wish to copy:{0}\n (eg. .mp4, .png, .wav) and press Enter ".format(file_format)).upper()

            for filename in src_dir:
                if filename.endswith(file_format):
                    shutil.copy(filename,destination)
            
        
    elif Options == "C":
        # source directory
        src_dir = "C:/Users/ZainbaMuhdYunus/Desktop/Python"
        dst_dir = "C:/Users/ZainbaMuhdYunus/Desktop/Python/new_folder"

        file_format = ""
        file_format =  input("please input the  fileformat you wish to copy:{0}\n (eg. .mp4, .png, .wav) and press Enter ".format(file_format)).upper()

        for filename in src_dir:
            if filename.endswith(file_format):
                shutil.copy(filename,dst_dir)
        
    else:
        raise Exception("Not a Valid option to choose ")

if __name__ == '__main__':
    main()














# for filename in os.listdir('C:/Users/ZainbaMuhdYunus/Desktop/Python'):
#             if filename.endswith(file_format):
#                 dst_dir = "C:/Users/ZainbaMuhdYunus/Desktop/Python/new_folder"
#                 shutil.copy(filename,dst_dir)
