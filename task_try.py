import time 
import random
import pyautogui
import tkinter as tk
from tkinter import filedialog

root= tk.Tk()
def takeScreenshot ():
    count=0
    name=random.randrange(1,1000)
    full_name=str(name) + ".jpg"
    for i in full_name:
        count=count+1
    myScreenshot = pyautogui.screenshot()
    myScreenshot.interval = 100
# generate a random time between 120 and 300 sec
    random_time = random.randrange(20,30)
# wait between 120 and 300 seconds (or between 2 and 5 minutes)
    time.sleep(random_time)
    myScreenshot.save((r'C:\Users\ZainbaMuhdYunus\Desktop\shots2\shot') + full_name)

    # keeps doing count
counter=0
while 1:
    counter = counter+1
    takeScreenshot()
