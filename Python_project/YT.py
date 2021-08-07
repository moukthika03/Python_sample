from tkinter import *
from tkinter import filedialog
from pytube import YouTube
import time
#import Video_player
import webbrowser
import Gt_vdqt
import datetime
from csv import writer


#import os
#os.system('clear')

root = Tk()
root.title('YouTube Video Downloader')
root.geometry("900x500")
root.configure(background='black')

def downloadFunction():

    link=myTextBox.get()

    video = YouTube(link)
    stream = video.streams.get_highest_resolution()
    #print(video.title,video.views,video.vid_info)
    stream.download(dirname)
    current = datetime.datetime.now()
    title =video.title
    views = video.views
    duration= video.length
    #df = pd.read_csv('YouTubeData.csv')
    newVideo = [str(title).replace("\n", " "),str(link).replace("\n", " "),str(current).replace("\n", " "),str(dirname).replace("\n", " "),str(views).replace("\n", " "),str(duration).replace("\n", " ")]
    with open('YouTubeData.csv', 'a',newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(newVideo)
        f_object.close()
    #newVideo.to_csv('YouTubeData.csv',index=False)
    downloadedLabel = Label(root, text="Downloaded!")
    downloadedLabel.grid(row=5, column=0)

    

def callback(event):
    webbrowser.open_new("http://127.0.0.1:5000/")

def fileBrowser():
    global dirname
    dirname = filedialog.askdirectory(parent=root, initialdir="/", title='Please select a directory')
    if len(dirname) > 0:
        browseBox.delete(0,END)
        browseBox.insert(0,dirname)
    
myLabel = Label(root,text="Video link")
myLabel.grid(row=0, column=0)



myTextBox = Entry(root,width=50,bg="black",fg="white",borderwidth=5)
myTextBox.grid(row=0,column=1)
myTextBox.insert(0,"Add link here")

Label(root, text=" ", fg="black", bg="black").grid(row=1,column=0)

browseBoxLabel = Label(root,text="File Location")
browseBoxLabel.grid(row=2,column=0)

browseBox = Entry(root,width=50,bg="black",fg="white",borderwidth=5)
browseBox.grid(row=2,column=1)
browseBox.insert(0,"Choose file location")

Label(root, text=" ", fg="black",bg="black").grid(row=3,column=0)

myButton = Button(root,text="Download", command=downloadFunction, fg="green" ,bg="grey",width=15)
myButton.grid(row=4,column=1)

browseBoxButton = Button(root,text="Browse", command=fileBrowser, fg="green" ,bg="grey",width=15)
browseBoxButton.grid(row=5,column=1)

lbl = Label(root, text=r"Visit our website!", fg="grey", cursor="hand2")
lbl.grid(row=6,column=1)
lbl.bind("<Button-1>", callback)



browseBoxButton2 = Button(root,text="Play Video", command=Gt_vdqt.playv, fg="green" ,bg="black",width=15)
browseBoxButton2.grid(row=7,column=1)
root.mainloop()