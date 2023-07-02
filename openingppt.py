from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk,ImageSequence


import os, sys, subprocess

import csv

def openPpt(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])



#SEARCH BUTTON
#Search and Open a ppt
def searchppt(x):
    x=x.lower()
    if x=="paris":
        filename = r"/Users/sanjanasen/Documents/Python_Workspce/RasberryPi_Project/LectureVideos/Paris.ppsx"
        openPpt(filename)

    elif x=="london":
        filename = r"/Users/sanjanasen/Documents/Python_Workspce/RasberryPi_Project/LectureVideos/London.ppsx"
        openPpt(filename)

    elif x=="japan":
        filename = r"/Users/sanjanasen/Documents/Python_Workspce/RasberryPi_Project/LectureVideos/Japan.ppsx"
        openPpt(filename)

    elif x=="marvel studios":
        filename = r"/Users/sanjanasen/Documents/Python_Workspce/RasberryPi_Project/LectureVideos/Marvel.ppsx"
        openPpt(filename)

    elif x=="earth":
        filename = r"/Users/sanjanasen/Documents/Python_Workspce/RasberryPi_Project/LectureVideos/earth.ppsx"
        openPpt(filename)

    elif x=="parts of body":
        bodypartsP()

    elif x=="":
        messagebox.showerror("Error","Find any lectures by topic name")

    else:
        messagebox.showerror("Error","Content not in your syllabus")

#Adding the vdo to csv
def addtocsvHome(x,usid):
    
    row = [usid,x]

    csvFilename = "sampledata.csv"
    with open(csvFilename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(row)


#HOME PAGE OPENING PPT LECTURES
#FRAME 1
def solarsysP(usid):
    filename = r"/Users/sanjanasen/Documents/Python_Workspce/RasberryPi_Project/LectureVideos/solarsystem.ppsx"
    vdoname = "CH:09 - Solar System"
    addtocsvHome(vdoname,usid)
    openPpt(filename)

def bodypartsP(usid):
    filename = r"/Users/sanjanasen/Documents/Python_Workspce/RasberryPi_Project/LectureVideos/bodyPartsbio.ppsx"
    vdoname = "CH:03 - Parts of Body"
    addtocsvHome(vdoname,usid)
    openPpt(filename)

def historyP(usid):
    filename = r"/Users/sanjanasen/Documents/Python_Workspce/RasberryPi_Project/LectureVideos/ScrollingSlideZoomsatreon.ppsx"
    vdoname = "CH:11 - ScrollingSlideZoom"
    addtocsvHome(vdoname,usid)
    openPpt(filename)

def scienceP(usid):
    filename = r"/Users/sanjanasen/Documents/Python_Workspce/RasberryPi_Project/LectureVideos/Marvel.ppsx"
    vdoname = "CH:09 - Marvel"
    addtocsvHome(vdoname,usid)
    openPpt(filename)

def earthPpt():
    filename = r"/Users/sanjanasen/Documents/Python_Workspce/RasberryPi_Project/LectureVideos/earth.ppsx"
    openPpt(filename)

#FRAME 2
