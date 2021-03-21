# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 22:18:22 2021

@author: Relieak
"""

'''
YouTube 影片下載工具
'''

''' Function'''

def choose():
    Result.set("You choose {} Video".format(Quality_choice.get()))  # item_1 item_2 ==> text
    
def DL_Video():   
    
    PathDir = DL_path.get()
    
    if PathDir == "{}".format(os.getcwd()):
        print("\n====== Download Path ======\n\n{}".format(PathDir))
    
    else :
        
        print("\n====== Download Path ======\n\n{}".format(PathDir))
            
        if not os.path.isdir(PathDir) :
            os.mkdir(PathDir)
        
    try :
        print("\n==== Video Downloading ====\n")
        yt = YouTube("{}".format(YT_url.get()))
        print(yt.title)
        
        if Quality_choice.get() == "Highest Quality" :
            yt.streams.get_highest_resolution().download(PathDir)
        
        elif Quality_choice.get() == "Lowest Quality" :
            yt.streams.get_lowest_resolution().download(PathDir)
            
        Result.set("{}\nDownload Completed".format(yt.title))
    
    except :
        print("Web Address Error")
        Result.set("Youtube Web Address Error\nTry Again !")

                   
from pytube import YouTube
import tkinter as tk
import os

'''major window'''
win = tk.Tk()
win.title("Youtube Video Downloader")
win.geometry("512x256")

'''Variable Setting'''
YT_url =  tk.StringVar()   # youtbe web address
DL_path = tk.StringVar()   # Download path
Quality_choice = tk.StringVar()   # Video Quality
Result = tk.StringVar()           # Show Result

'''Frame 1'''
frame_1 = tk.Frame(win)
frame_1.pack()

Address_txt = tk.Label(frame_1, text ="YouTube Address :")
Address_txt.grid(row = 0, column = 0, padx=5, pady=5)

Input_txt_1 = tk.Entry(frame_1, textvariable = YT_url, width=40) 
Input_txt_1.grid(row = 0, column = 1, padx=5, pady=5)

'''Frame 2'''
frame_2 = tk.Frame(win)
frame_2.pack()

Path_txt = tk.Label(frame_2, text ="Download Path :")
Path_txt.grid(row = 0, column = 0, padx=5, pady=5)

DL_path.set("{}".format(os.getcwd()))        # Default download path
Input_txt_2 = tk.Entry(frame_2, textvariable = DL_path, width=40) 
Input_txt_2.grid(row = 0, column = 1, padx=5, pady=5)

''' Frame 3'''
frame_3 = tk.Frame(win)
frame_3.pack()

item_1 = tk.Radiobutton(frame_3, text="Highest Quality mp4", value="Highest Quality", variable=Quality_choice, command=choose  )
item_1.grid(row = 0, column = 0, padx=5, pady=5)

'''Frame 4'''
frame_4 = tk.Frame(win)
frame_4.pack()

item_2 = tk.Radiobutton(frame_4, text="Lowest Quality mp4", value="Lowest Quality", variable=Quality_choice, command=choose  )
item_2.grid(row = 0, column = 0, padx=5, pady=5)

'''Frame 5'''
frame_5 = tk.Frame(win)
frame_5.pack()

Button_txt = tk.Button(frame_5, text ="Start Download", command=DL_Video)
Button_txt.grid(row = 0, column = 0, padx=5, pady=5)

'''Frame 6'''
'''show result'''
frame_6 = tk.Frame(win)
frame_6.pack()

Result_txt = tk.Label(frame_6, textvariable = Result, fg="blue")  
Result_txt.grid(row = 0, column = 0, padx=5, pady=5)

'''Select item_1 for default value'''
item_1.select()
choose()

win.mainloop()
