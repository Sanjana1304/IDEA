from tkinter import *
from tkinter import messagebox

from openingppt import *

import csv


#To play the ppt from the listbox
def playPpt(x):
    if x=="CH:01 - Number System":
        filename = r"/Users/sanjanasen/Documents/Python_Workspce/RasberryPi_Project/LectureVideos/numbersystemMath.ppsx"
        openPpt(filename)

    elif x=="CH:02 - Algebra":
        filename = r"/Users/sanjanasen/Documents/Python_Workspce/RasberryPi_Project/LectureVideos/coffee.ppsx"
        openPpt(filename)

    elif x=="CH:03 - Coordinate Geometry":
        filename = r"/Users/sanjanasen/Documents/Python_Workspce/RasberryPi_Project/LectureVideos/coffee.ppsx"
        openPpt(filename)

    elif x=="CH:01 - Semen Anatomy":
        filename = r"/Users/sanjanasen/Documents/Python_Workspce/RasberryPi_Project/LectureVideos/coffee.ppsx"
        openPpt(filename)

    elif x=="CH:02 - Transels":
        filename = r"/Users/sanjanasen/Documents/Python_Workspce/RasberryPi_Project/LectureVideos/coffee.ppsx"
        openPpt(filename)

    elif x=="CH:03 - Parts of Body":
        filename = r"/Users/sanjanasen/Documents/Python_Workspce/RasberryPi_Project/LectureVideos/bodypartsBio.ppsx"
        openPpt(filename)

    elif x=="CH:01 - Japan":
        filename = r"/Users/sanjanasen/Documents/Python_Workspce/RasberryPi_Project/LectureVideos/Japan.ppsx"
        openPpt(filename)

    elif x=="CH:02 - Paris":
        filename = r"/Users/sanjanasen/Documents/Python_Workspce/RasberryPi_Project/LectureVideos/Paris.ppsx"
        openPpt(filename)


    elif x=="CH:03 - London":
        filename = r"/Users/sanjanasen/Documents/Python_Workspce/RasberryPi_Project/LectureVideos/London.ppsx"
        openPpt(filename)    

    elif x=="CH:05 - Earth":
        filename = r"/Users/sanjanasen/Documents/Python_Workspce/RasberryPi_Project/LectureVideos/earth.ppsx"
        openPpt(filename)

    elif x=="CH:09 - Solar System":
        filename = r"/Users/sanjanasen/Documents/Python_Workspce/RasberryPi_Project/LectureVideos/solarsystem.ppsx"
        openPpt(filename)

    elif x=="CH:11 - ScrollingSlideZoomsatreon":
        filename = r"/Users/sanjanasen/Documents/Python_Workspce/RasberryPi_Project/LectureVideos/ScrollingSlideZoomsatreon.ppsx"
        openPpt(filename)


    else:
        filename = r"/Users/sanjanasen/Documents/Python_Workspce/RasberryPi_Project/LectureVideos/strangerthings.ppsx"
        openPpt(filename)

#TO DISPLAY PARTICULAR CLASS MODULES OF THE PARTICUALR SUBJECT

def ClassSubjList(subjList,heading,usid):  #explore button la irukka frst row
    root = Tk()
    root.geometry("600x500")
    root.config(bg='black')
    root.title('List of Chapters')
    scrollbar = Scrollbar(root, orient="vertical")
    lb = Listbox(root, width=30, height=20, font=("Verdena",20),yscrollcommand=scrollbar.set)
    scrollbar.config(command=lb.yview)

    lb.configure(background="black", foreground="pink")
    scrollbar.pack(side="right", fill="y")

    head_label=Label(root,text=heading,fg="white",bg="black",font=("Apple Braille",35,"bold"))
    head_label.place(x=100,y=15)


    def addtocsvAndPass1():
        x = lb.get(ACTIVE)
        row = [usid,x]

        csvFilename = "sampledata.csv"
        with open(csvFilename, 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(row)
        playPpt(x)

    playBtn=Button(root,text="PLAY",bg='blue',fg='black',font=("Comic Sans MS",17,"bold"),width=8,command=addtocsvAndPass1)
    playBtn.place(x=100,y=70)

    def addtolibrarydata1():
        x = lb.get(ACTIVE)
        row = [usid,x]

        csvFilename = "libraryData.csv"
        with open(csvFilename, 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(row)

        messagebox.showinfo("Error","Added to Library !")

    addBtn=Button(root,text="ADD",bg='blue',fg='black',font=("Comic Sans MS",17,"bold"),width=8,command=addtolibrarydata1)
    addBtn.place(x=350,y=70)


    for i in subjList:
        lb.insert("end", i,"\n")

    lb.place(x=30,y=150)

    root.mainloop()


# TO DISPLAY ALL THE MODULES OF THE PARTICULAR SUBJECT
def showList(subjList,usid):  #explore button la irukka second row
    root = Tk()
    root.geometry("600x500")
    root.config(bg='black')
    root.title('List of Chapters')
    scrollbar = Scrollbar(root, orient="vertical")
    lb = Listbox(root, width=30, height=20, font=("Verdena",20),yscrollcommand=scrollbar.set)
    scrollbar.config(command=lb.yview)

    lb.configure(background="black", foreground="turquoise")
    scrollbar.pack(side="right", fill="y")

    def addtocsvAndPass2():
        x = lb.get(ACTIVE)
        row = [usid,x]

        csvFilename = "sampledata.csv"
        with open(csvFilename, 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(row)
        playPpt(x)
        

    playBtn=Button(root,text="PLAY",bg='blue',fg='black',font=("Comic Sans MS",17,"bold"),width=8,command=addtocsvAndPass2)
    playBtn.place(x=100,y=10)

    def addtolibrarydata2():
        x = lb.get(ACTIVE)
        row = [usid,x]

        csvFilename = "libraryData.csv"
        with open(csvFilename, 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(row)

        messagebox.showinfo("Error","Added to Library !")

    addBtn=Button(root,text="ADD",bg='blue',fg='black',font=("Comic Sans MS",17,"bold"),width=8,command=addtolibrarydata2)
    addBtn.place(x=350,y=10)


    for i in subjList:
        lb.insert("end", i,"\n")

    lb.place(x=30,y=70)

    root.mainloop()

