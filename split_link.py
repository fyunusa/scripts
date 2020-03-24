import os
import pandas as pd
import csv
import sys

os.chdir("C:/Users/fyunu/OneDrive/Desktop")

a = pd.read_csv("my_colon.csv")
# a = pd.read_csv("dawahcast_export.csv")

# choose keys
uid = a.uniqueID
# nid = a.Nid
title = a.Title
rp = a.Resource_Person
topics = a.Topics
key = a.Keywords
languaga = a.Language
audio = a.Audio_URL
# main = a.Audio_URL_main
amr = a.aMR_Audio_File
dur = a.Duration
album = a.AlbumID
mp3_size = a.mp3_size_range
dur_range = a.Duration_Range

link = audio
			 		
counta = 0
countb = 0

with open('failed.txt', 'w') as f, open('correct.txt', 'w') as c:
    for i,j,k,l,m,n,o,p,q,r,s,t in zip(uid,title,rp,topics,key,languaga,amr,link,dur,album,mp3_size,dur_range):
        link2 = p.replace("%20", " ")
        splitter = (link2.split('/'))
        # print (splitter[4])
        splitter2 = splitter[4]

        test = (str(i) +'*-*'+ str(j) +'*-*'+ str(k) +'*-*'+ str(l) +'*-*'+ str(m) +'*-*'+
                str(n) +'*-*'+ str(o) +'*-*'+ str(p) +'*-*'+ str(q) +'*-*'+ str(r) +'*-*'+ 
                str(s) +'*-*'+ str(t) +'*-*'+ str(splitter2))

        if k == p:
            counta = counta + 1
            sys.stdout = c
            print (test)
        else:
            countb = countb + 1
            sys.stdout = f
            print (test)

    with open('failed.txt', 'r') as infile, open('failed.csv', 'w') as outfile: 
                    stripped = (line.strip() for line in infile)
                    splitter = (line.split('*-*')for line in stripped if line)
                    writer = csv.writer(outfile)
                    writer.writerows(splitter)

    with open('correct.txt', 'r') as inner, open('correct.csv', 'w') as outer:
                    stripped = (line.strip() for line in inner)
                    splitter = (line.split('*-*')for line in stripped if line)
                    writer2 = csv.writer(outer)
                    writer2.writerows(splitter)

























# link = "http://media.dawahnigeria.com/dnlectures2/Ustaz%20AbdGhaniy%20Jum'ah%20(Lagos)/Tafseer/Ustadh%20Abdul%20Ganiyy%20Jum'ah_Tafseer%20-%20Suratul%20Shuarah%20[Q26%20vs209-215]%20-%20(11-01-20%20(Yoruba)_DN.amr"
# link = link.replace("%20", " ")
# splitter = (link.split('/'))

# print(splitter)
# print (splitter[4])
