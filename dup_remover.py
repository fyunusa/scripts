#loop through the file system
import os, subprocess
paths = ['/home/dawahnig/public_html/dnlectures', '/home/dawahnig/public_html/dnlectures2', '/home/dawahnig/public_html/dnlectures2/dnquran']
extensions = ['.mp3', '.amr', '.wav']

def check_number_of_dupes(files,file_name):
    counter = 0
    dupes = []
    for file in files:
        if(file_name in file):
            dupes.append(file)
            counter += 1
    return [counter,dupes]

def remove_files(file):
        try:
            os.remove(file)
        except Exception as e:
            print("Error:{0}".format(e))

def delete_duplicate_files():
    missing_mp3_files = 0
    missing_amr_files = 0
    # for path in paths:
    temp = []
    cmd = ""
    for current, sub, files in os.walk(os.getcwd()):
        for file in files:
            c = 0
            amr = 0
            mp3 = 0
            dupes =[]
            extension = os.path.splitext(file)[1]
            if(extension in extensions):
                fname = os.path.splitext(file)[0]
                c, dupes = check_number_of_dupes(files, fname)
                if(c > 2):
                    dupes.reverse()
                    for dupe in dupes:
                        if('amr' in dupe.lower()):
                            amr+=1
                            if(amr > 1):
                                remove_files(os.path.join(current, dupe))
                                amr -=1
                        elif("mp3" in dupe.lower()):
                            mp3 += 1
                            if(mp3 > 1):
                                remove_files(os.path.join(current, dupe))
                                mp3 -=1
                        else:
                            pass
                    print("Number of MP3= {0}, AMR = {1}".format(mp3,amr))
                    print("Problem Dey Here ooooo {0}".format(dupes))
                else:
                    print("No Problem {0}".format(c))
        #     temp.append(file.lower())
        # for t in temp:
        #     extension = os.path.splitext(t)[1]
        #     if(extension in extensions):
        #         if(temp.count(t) > 1):
        #             subprocess.call("rm -f {0}".format(os.path.join(current, t)), shell=True)
        #             temp.remove(t)
        #             os.remove(t)
        #             print("file is {0}".format(os.path.join(current, file)))
        #         else:
        #             pass
        # temp = []
                # print("Nothing deetct")
                # print("More than one file file {0} = {1}".format(type(file),file.lower() ))
delete_duplicate_files()


                # extension = os.path.splitext(file)[1]
                # f = file.strip('.mp3') +('.amr') if (file.endswith('.mp3')) else file.strip('.amr') + ('.mp3')
                # if(extension in extensions and f not in files):
                #     if(file.endswith('.mp3')):
                #         try:
                #             dnconverter.processmp3(full_path = os.path.join(current, file))
                #             missing_amr_files += 1
                #         except Exception as e:
                #             print(e)
                #     else:
                #         try:
                #             dnconverter.processamr(full_path = os.path.join(current, file))
                #             missing_mp3_files += 1
                #         except Exception as e:
                #             print(e)
#find files with same extension
#check if we have more two same files with the same extensions remove the one that was created, remove wav files also 
