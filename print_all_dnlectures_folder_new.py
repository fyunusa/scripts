import os



# paths = ['/home/dawahnig/public_html/dnlectures', 
#         '/home/dawahnig/public_html/dnlectures2', ]


def print_folders(path):
    if (path == '/home/dawahnig/public_html/dnlectures' ):
        for current, sub, files in os.walk(path):
            print('\n'.join(sub))
            break

        with open('dnlectures.txt', 'a+') as files_obj:
            files_obj.write("========== All files in {0} ==========\n".format(path))
            files_obj.write('\n'.join(files))
            files_obj.write("\n\n========All folders in {0}===========\n".format(path))
            files_obj.write('\n'.join(sub))
    elif (path == '/home/dawahnig/public_html/dnlectures2'):
        for current, sub, files in os.walk(path):
            print('\n'.join(sub))
            break

        with open('dnlectures2.txt', 'a+') as files_obj:
            files_obj.write("========== All files in {0} ==========\n".format(path))
            files_obj.write('\n'.join(files))
            files_obj.write("\n\n========All folders in {0}===========\n".format(path))
            files_obj.write('\n'.join(sub))
    else:
        for current, sub, files in os.walk(path):
            print('\n'.join(sub))
            break

        with open('all_folders_and_files.txt', 'a+') as files_obj:
            files_obj.write("========== All files in {0} ==========\n".format(path))
            files_obj.write('\n'.join(files))
            files_obj.write("\n\n========All folders in {0}===========\n".format(path))
            files_obj.write('\n'.join(sub))
       
if __name__ == "__main__":
    path = input("Enter a Folder name to print its files and subfolders:")
    print_folders(path)