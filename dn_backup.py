import subprocess
import os.path
paths = ['/home/dawahnig/public_html/dnlectures', 
        '/home/dawahnig/public_html/dnlectures2', 
        '/home/dawahnig/public_html/dnlectures2/dnquran']
        
destination = '/home/light_wave_radio/Desktop/'
def get_connected_drives():
    #this is going to work for windows os only, Linux an family not supported for now
    connected_drives = []
    for drive in range(ord('A'), ord('Z')+1):
        if(os.path.exists(chr(drive) + ':')):
            connected_drives.append(chr(drive) + ':')
    return connected_drives

def main():
    available_drives = get_connected_drives()
    if (available_drives):
        destination = input("The following drives are available:{0}\n Enter the letter of the back-up drive(eg. E: or C:) and press Enter ".format(available_drives)).upper()
        for path in paths:
            return_value = subprocess.check_call(
                'rsync -chavzP --stats dawahnig@185.164.35.20:{0} {1}'.format(path, destination),
                shell=True
                )
            if(return_value != 0 ):
                raise subprocess.CalledProcessError(return_value)
    else:
        raise Exception("No Valid Drive was detected")
if __name__ == '__main__':
    main()