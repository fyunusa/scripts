import requests
import collections.abc
import json
import csv
import os
#os.chdir('/home/light_wave_radio/Downloads/')
os.chdir('C:/Users/ZainbaMuhdYunus/Desktop/csv')
#get the rp/reciter from nid export
def validate():
    with open('https_audit.csv') as nidexport:
        reader = csv.DictReader(nidexport)
        print(reader.fieldnames)
        this = 186253
        # 173493
  

        # for item in reader:
    #get the rp/reciter from the dawacast server
        response = requests.get('https://dawahnigeria.com/dawahcast/lectureapi3/'   + str(this)).json()
            # response = requests.get('https://dawahnigeria.com/dawahcast/albumapi4/'   + str(item['nid'])).json()
           
            # data_string = json.dumps(response, skipkeys=True, sort_keys=True)
    #compare the result try:
        for r in response:
            print (r)
                # with open('Rps_with_different_reciters.csv', 'a+') as found_files:
                #     r2 = csv.DictReader(found_files)
                #     headers = list(r.keys())
                #     headers.append("Error")
                #     writer = csv.DictWriter(found_files, fieldnames = ['Album','AlbumNid','AlbumRp','AudioNid', "Audio", "AudioRP", "Error"])
                #     with open('Rps_with_different_reciters.csv', 'rb+') as p:
                #         headers = next(p, None)
                #         if headers == None:
                #             writer.writeheader()
                #     #writer.writeheader()
                        
                #     # print("The Audio Rp is {0} and  album ID is {1}".format(r.keys(), item['rp']))
                #         if(item['rp'] != r['rp']):
                #             if(item['rp'] == "" and r['rp'] != ""):
                #                 print("The Album RP=None but the Audio has {0}".format(r['rp']))
                #                 writer.writerow({
                #                 "Album": item['title'],
                #                 "Audio":r['AlbumTitle'],
                #                 "Error": "The audio RP has rp but the album doesn't"})

                #             elif (item['rp'] != "" and r['rp'] == ""):
                #                 writer.writerow(
                #                 {"Album": item['title'],
                #                  "Audio":r['AlbumTitle'],
                #                  "Error": "Album Has RP but the Audio Doesn't"})
                                

                #             elif(item['rp'] == "" and r['rp']==""):
                #                 print("both are empty")

                #                 if(item['reciter'] == "" and r['reciter'] != ""):
                #                     writer.writerow({
                #                     "Album": item['title'],
                #                     "AudioNid": r['Nid'],
                #                     "Audio":r['AlbumTitle'],
                #                     "Error": "The Album has Reciter but the Audio doesn't"},
                                    
                #                     )

                #                 elif(item['reciter'] == "" and r['reciter']==""):
                #                     writer.writerow({
                #                     "AlbumNid": item['nid'],
                #                     "Album": item['title'],
                #                     "AudioNid": r['Nid'],
                #                     "Audio":r['AlbumTitle'],
                #                     "Error": "Both audio and album have no Reciter And no RP"})

                #                 else:
                #                     writer.writerow({
                #                     "AlbumNid": item['nid'],
                #                     "Album": item['title'],
                #                     "AlbumRp": item['rp'],
                #                     "AudioNid": r['Nid'],
                #                     "Audio":r['AlbumTitle'],
                #                     "AudioRP": r['rp'],
                #                     "Error": "Audio Rp is different from Album RP"})
                #             else:
                #                 # print("The Audio RP=>> {0}  || Album RP=>> {1}".format(r['AlbumTitle'], item['rp']))
                #                 print(r['AlbumTitle'])
                #                 writer.writerow(
                #                  {
                #                  "AlbumNid": item['nid'],
                #                  "Album": item['title'],
                #                  "AlbumRp": item['rp'],
                #                  "AudioNid": r['Nid'],
                #                  "Audio":r['AlbumTitle'],
                #                  "AudioRP": r['rp'],
                #                  "Error": "Audio Rp is different from Album RP"}
                #                  )
                        # with open('Rps_with_different_reciters.csv', 'a+') as found_files:
                        #     r2 = csv.DictReader(found_files)
                        #     writer = csv.DictWriter(found_files, fieldnames = r.keys())
                        #     # field_name = r2.fieldnames
                        #     # print("Filed Name is {0}".format(field_name))
                        #     with open('Rps_with_different_reciters.csv', 'rb+') as p:
                        #         headers = next(p, Non[e)
                        #         if headers == None:
                        #             writer.writeheader()
                        #     #writer.writeheader()
                        #     writer.writerow(r)
                        # print("The Audio Rp is {0} and  album ID is {1}".format(r.keys(), item['rp']))
                # else:
                #     print("Good To Go!!")
    #generate a file of type csv to report findings. 
if (__name__ == '__main__'):
    validate()
