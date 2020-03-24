import os
import pandas as pd
import csv
import sys

os.chdir("C:/Users/ZainbaMuhdYunus/Desktop")

a = pd.read_csv("my_colon.csv")

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
mp3_size = a.mp3_Size_Range
dur_range = a.Duration_Range

link = audio
link = link.replace("%20", " ")
splitter = (link.split('/'))
serverName = splitter[4]
					
counta = 0
countb = 0

with open('failed.txt', 'w') as f, open('correct.txt', 'w') as c:
    for i,j,k,l,m,n,o,p,q,r,s,t in zip(uid,title,rp,topics,key,languaga,amr,serverName,dur,album,mp3_size,dur_range):
        test = (str(i) +'*-*'+ str(j) +'*-*'+ str(k) +'*-*'+ str(l) +'*-*'+ str(m) +'*-*'+
                str(n) +'*-*'+ str(o) +'*-*'+ str(p) +'*-*'+ str(q) +'*-*'+ str(r) +'*-*'+ 
                str(s) +'*-*'+ str(t) 
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
    # print ('total number of same items are : ' + str(counta))
    # print ('total number of items that are not same are : ' + str(countb))