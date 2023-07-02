#connecting python with mysql
import mysql.connector as sql
mycon=sql.connect(host="localhost",user="root",passwd="sanju1304",database="student_details")


#creating cursor object
cursor=mycon.cursor()

#using GUI programming
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk,ImageSequence


#to open ppts
import os
from openingppt import *

#to display chapter lists
from subjectList import *

import csv
import random

import keyboard

#from assist1 import *
#import assist1

#login window
window=Tk()
window.geometry("500x500")

window.config(bg="black")
window.title("Sign-in | SignUp")

label_head1=Label(window,text="!DEA",fg='turquoise',bg='black',font=("arial",40,"bold")).place(x=170,y=20)

label_head2=Label(window,text="Intelligent Digital Educational Assist",fg='turquoise',bg='black',font=("arial",25,"bold")).place(x=35,y=65)



usid_label=Label(window,text="USER ID : ",bg="black",fg='white',font=("arial",15,"bold"))
usid_label.place(x=110,y=220)

usid_entry=Entry(window,width=20,font=(12))
usid_entry.place(x=230,y=220)

pwd_label=Label(window,text="PASSWORD : ",bg="black",fg='white',font=("arial",15,"bold"))
pwd_label.place(x=110,y=280)

pwd_entry=Entry(window,width=20, font=(12),show="*")
pwd_entry.place(x=230,y=280) 

small_label=Label(window,text="Dont have an account? ",fg='blue',bg="grey",relief=RIDGE,font=("arial",7,"bold"))
small_label.place(x=270,y=380)

# inserting the data in the table from the reg page
def store_details():
    name=entry_1.get()
    email=entry_2.get()
    mno=entry_3.get()
    pwd=entry_4.get()
    add=entry_5.get()
    std=entry_6.get()

    uid = name[0:3]+mno[0:2]+"@ia.com"

    query="insert into basicInfo(userid,name,mail,mno,pwd,addr,class) values(%s,%s,%s,%s,%s,%s,%s)"
    val = (uid,name,email,mno,pwd,add,std)
    cursor.execute(query,val)
    mycon.commit()

    msg = "Registration Successful!\n Use "+uid+" for signing in"
    messagebox.showinfo(title="Success", message=msg)


# registration page (opened when register button is clicked)
def Reg_form():
    window=Tk()
    window.geometry("700x700")
    window.title("Registration form")
    window.config(bg="black")

    global entry_1
    global entry_2
    global entry_3
    global entry_4
    global entry_5
    global entry_6

    label_0=Label(window,text="REGISTRATION PAGE",fg="turquoise",bg="black",relief="solid",font=("Copperplate Gothic",25,"bold"))
    label_0.place(x=220,y=20)

    label_1=Label(window,text="Full Name:",fg="white",bg="black",font=("Comic Sans MS",20))
    label_1.place(x=120,y=120)
    fname=StringVar()
    entry_1=Entry(window, font=("Comic Sans MS",17),textvar=fname,width=20)
    entry_1.place(x=300,y=120)

    label_2=Label(window, text="Email:",fg="white",bg="black",font=("Comic Sans MS",20))
    label_2.place(x=120,y=200)
    email=StringVar()
    entry_2=Entry(window, font=("Comic Sans MS",17),textvar=email,width=20)
    entry_2.place(x=300,y=200)

    label_3=Label(window, text="Mobile no.:",fg="white",bg="black",font=("Comic Sans MS",20))
    label_3.place(x=120,y=280)
    mn=StringVar()
    entry_3=Entry(window, font=("Constantia",17),textvar=mn,width=20)
    entry_3.place(x=300,y=280)

    label_4=Label(window,text="Set Password:",fg="white",bg="black",font=("Comic Sans MS",20))
    label_4.place(x=120,y=360)
    sp=StringVar()
    entry_4=Entry(window, font=("Comic Sans MS",17),textvar=sp,width=20)
    entry_4.place(x=300,y=360)

    label_5=Label(window,text="Address:",fg="white",bg="black",font=("Comic Sans MS",20))
    label_5.place(x=120,y=440)
    sp=StringVar()
    entry_5=Entry(window, font=("Comic Sans MS",17),textvar=sp,width=20)
    entry_5.place(x=300,y=440)

    label_6=Label(window, text="Class:",fg="white",bg="black",font=("Comic Sans MS",20))
    label_6.place(x=120,y=520)
    std=StringVar()
    entry_6=Entry(window, font=("Constantia",17),textvar=std,width=20)
    entry_6.place(x=300,y=520)


    sub_button=Button(window,text="Submit",font=("Comic Sans MS",16),relief=RIDGE,width=12,fg="black",command =store_details)
    sub_button.place(x=250,y=630)

    window.mainloop()

#checking for login credentials and opening home page   
def welcome():
    usid=usid_entry.get()
    pwd=pwd_entry.get()

    query = """select userid,pwd from basicInfo where userid=%s"""
    cursor.execute(query,(usid,)) 
    res=cursor.fetchall()

    query2 = """select utype from basicInfo where userid=%s"""
    cursor.execute(query2,(usid,)) 
    res2=cursor.fetchall()

    if usid!="":
        if res==[(usid,pwd)]:
            #if user exists,their HOME PAGE will be opened         
            #global window1
            window1=Tk()  #window1 is home page
            window1.geometry("2500x1000")
            window1.title("Intelligent Digital Educational Assist")
            window1.config(bg="black")


            def explorePage():
                window2=Tk()  #window2 is explore page
                window2.geometry("2500x1000")
                window2.title("Intelligent Educational Assist || Explore Page")
                window2.config(bg="black")

                def homePageE():
                    window2.destroy()
                    welcome()

                homeBtn=Button(window2,text="Home",bg='blue',fg='black',font=("arial",17,"bold"),width=8,command=homePageE)
                homeBtn.place(x=400,y=20)

                #no command as this explore button is in explore page itself
                expBtn=Button(window2,text="Explore",bg='black',fg='black',font=("arial",17,"bold"),width=8)
                expBtn.place(x=550,y=20)

                def libraryPageE():
                    window2.destroy()
                    libraryPage()

                libBtn=Button(window2,text="Library",bg='black',fg='black',font=("arial",15,"bold"),width=8,command=libraryPageE)
                libBtn.place(x=700,y=20)
                
                #srch image here
                srchPhoto=PhotoImage(master=window2,file="img/searchButton-2-2.png")
                srchLabel=Label(window2,image=srchPhoto)
                srchLabel.place(x=860,y=20)

                searchEntry=Entry(window2, font=("Comic Sans MS",13),width=27)
                searchEntry.place(x=900,y=20)

                def searchpass():
                    val = searchEntry.get()
                    searchppt(val)

                srchBtn=Button(window2,text="Search",bg='black',fg='black',font=("arial",12,"bold"),width=6,command=searchpass)
                srchBtn.place(x=1160,y=20)

                #adding a profile pic image as a button
                prflePhoto=PhotoImage(master=window2,file="img/profilePic.png")
                prflLabel=Label(window2,image=prflePhoto)


                pfleBtn = Button(window2,image=prflePhoto,command=my_profile)
                pfleBtn.place(x=1300,y=20)


                #BROWSE MORE VIDEOS (CLASS AND SUBJECT WISE)
                more_label=Label(window2,text="My Courses",fg="white",bg="black",font=("Apple Braille",35,"bold"))
                more_label.place(x=100,y=130)

                query = """select class from basicInfo where userid=%s"""
                cursor.execute(query,(usid,)) 
                res=cursor.fetchall()
                class_n = res[0][0]

                if class_n==10:
                    #10th class math ppt button image
                    mathPhoto1=PhotoImage(master=window2,file="img/math_10th.png")
                    mathLabel1=Label(window2,image=mathPhoto1)

                    def math_10():
                        mathList = ["CH:01 - Number System","CH:02 - Algebra","CH:03 - Coordinate Geometry","CH:04 - Geometry","CH:05 - Trigonometry","CH:06 - Mensuration","CH:07 - Statistics","CH:08 - Probablity","CH:01 - Number System","CH:02 - Algebra","CH:03 - Coordinate Geometry","CH:04 - Geometry","CH:05 - Trigognometry","CH:06 - Mensuration","CH:07 - Statistics","CH:08 - Probablity"]
                        ClassSubjList(mathList,"Class 10 Math Modules",usid)

                    math10Btn = Button(window2,image=mathPhoto1,command=math_10)
                    math10Btn.place(x=100,y=190)


                    #10th class science ppt button image
                    sciPhoto1=PhotoImage(master=window2,file="img/sci2.png")
                    sciLabel1=Label(window2,image=sciPhoto1)

                    def sci_10():
                        sciList = ["CH:01 - Semen Anatomy","CH:02 - Transels","CH:03 - Parts of Body","CH:04 - Reproductive System","CH:05 - Cell biology","CH:06 - Inheritance","CH:07 - Evolution","CH:08 - Biotechnology","CH:01 - Semen Anatomy","CH:02 - Transels","CH:03 - Parts of Body","CH:04 - Reproductive System","CH:05 - Cell biology","CH:06 - Inheritance","CH:07 - Evolution","CH:08 - Biotechnology"]
                        ClassSubjList(sciList,"Class 10 Science Modules",usid)

                    sci10Btn = Button(window2,image=sciPhoto1,command=sci_10)
                    sci10Btn.place(x=330,y=190)

                    #10th class social ppt button image
                    socPhoto1=PhotoImage(master=window2,file="img/social_10th.png")
                    socLabel1=Label(window2,image=socPhoto1)

                    def soc_10():
                        sciList = ["CH:01 - Semen Anatomy","CH:02 - Transels","CH:03 - Parts of Body","CH:04 - Reproductive System","CH:05 - Cell biology","CH:06 - Inheritance","CH:07 - Evolution","CH:08 - Biotechnology","CH:01 - Semen Anatomy","CH:02 - Transels","CH:03 - Parts of Body","CH:04 - Reproductive System","CH:05 - Cell biology","CH:06 - Inheritance","CH:07 - Evolution","CH:08 - Biotechnology"]
                        ClassSubjList(sciList,"Class 10 Social Modules",usid)

                    soc10Btn = Button(window2,image=socPhoto1,command=soc_10)
                    soc10Btn.place(x=560,y=190)


                    #10th class english ppt button image
                    engPhoto1=PhotoImage(master=window2,file="img/eng_10th.png")
                    engLabel1=Label(window2,image=engPhoto1)

                    def eng_10():
                        sciList = ["CH:01 - Semen Anatomy","CH:02 - Transels","CH:03 - Parts of Body","CH:04 - Reproductive System","CH:05 - Cell biology","CH:06 - Inheritance","CH:07 - Evolution","CH:08 - Biotechnology","CH:01 - Semen Anatomy","CH:02 - Transels","CH:03 - Parts of Body","CH:04 - Reproductive System","CH:05 - Cell biology","CH:06 - Inheritance","CH:07 - Evolution","CH:08 - Biotechnology"]
                        ClassSubjList(sciList,"Class 10 English Modules",usid)

                    eng10Btn = Button(window2,image=engPhoto1,command=eng_10)
                    eng10Btn.place(x=790,y=190)

                    #10th class tamil ppt button image
                    tamPhoto1=PhotoImage(master=window2,file="img/tamil_10th.png")
                    tamLabel1=Label(window2,image=tamPhoto1)

                    def tamil_10():
                        sciList = ["CH:01 - Semen Anatomy","CH:02 - Transels","CH:03 - Parts of Body","CH:04 - Reproductive System","CH:05 - Cell biology","CH:06 - Inheritance","CH:07 - Evolution","CH:08 - Biotechnology","CH:01 - Semen Anatomy","CH:02 - Transels","CH:03 - Parts of Body","CH:04 - Reproductive System","CH:05 - Cell biology","CH:06 - Inheritance","CH:07 - Evolution","CH:08 - Biotechnology"]
                        ClassSubjList(sciList,"Class 10 Tamil Modules",usid)

                    tam10Btn = Button(window2,image=tamPhoto1,command=tamil_10)
                    tam10Btn.place(x=1020,y=190)

                if class_n==11:
                    #11th class math ppt button image
                    mathPhoto1=PhotoImage(master=window2,file="img/math_10th.png")
                    mathLabel1=Label(window2,image=mathPhoto1)

                    def math_11():
                        sciList = ["CH:01 - Semen Anatomy","CH:02 - Transels","CH:03 - Parts of Body","CH:04 - Reproductive System","CH:05 - Cell biology","CH:06 - Inheritance","CH:07 - Evolution","CH:08 - Biotechnology","CH:01 - Semen Anatomy","CH:02 - Transels","CH:03 - Parts of Body","CH:04 - Reproductive System","CH:05 - Cell biology","CH:06 - Inheritance","CH:07 - Evolution","CH:08 - Biotechnology"]
                        ClassSubjList(sciList,"Class 11 Math Modules",usid)

                    math11Btn = Button(window2,image=mathPhoto1,command=math_11)
                    math11Btn.place(x=100,y=190)


                    #11th class physics ppt button image
                    phyPhoto1=PhotoImage(master=window2,file="img/physics.png")
                    phyLabel1=Label(window2,image=phyPhoto1)

                    def phy_11():
                        sciList = ["CH:01 - Semen Anatomy","CH:02 - Transels","CH:03 - Parts of Body","CH:04 - Reproductive System","CH:05 - Cell biology","CH:06 - Inheritance","CH:07 - Evolution","CH:08 - Biotechnology","CH:01 - Semen Anatomy","CH:02 - Transels","CH:03 - Parts of Body","CH:04 - Reproductive System","CH:05 - Cell biology","CH:06 - Inheritance","CH:07 - Evolution","CH:08 - Biotechnology"]
                        ClassSubjList(sciList,"Class 11 Physics Modules",usid)

                    phy11Btn = Button(window2,image=phyPhoto1,command=phy_11)
                    phy11Btn.place(x=330,y=190)

                    #11th class chemistry ppt button image
                    chemPhoto1=PhotoImage(master=window2,file="img/Chemistry.png")
                    chemLabel1=Label(window2,image=chemPhoto1)

                    def chem_11():
                        sciList = ["CH:01 - Semen Anatomy","CH:02 - Transels","CH:03 - Parts of Body","CH:04 - Reproductive System","CH:05 - Cell biology","CH:06 - Inheritance","CH:07 - Evolution","CH:08 - Biotechnology","CH:01 - Semen Anatomy","CH:02 - Transels","CH:03 - Parts of Body","CH:04 - Reproductive System","CH:05 - Cell biology","CH:06 - Inheritance","CH:07 - Evolution","CH:08 - Biotechnology"]
                        ClassSubjList(sciList,"Class 11 Chemistry Modules",usid)

                    chem11Btn = Button(window2,image=chemPhoto1,command=chem_11)
                    chem11Btn.place(x=560,y=190)
                    

                    #11th class english ppt button image
                    engPhoto1=PhotoImage(master=window2,file="img/eng_10th.png")
                    engLabel1=Label(window2,image=engPhoto1)

                    def eng_11():
                        sciList = ["CH:01 - Semen Anatomy","CH:02 - Transels","CH:03 - Parts of Body","CH:04 - Reproductive System","CH:05 - Cell biology","CH:06 - Inheritance","CH:07 - Evolution","CH:08 - Biotechnology","CH:01 - Semen Anatomy","CH:02 - Transels","CH:03 - Parts of Body","CH:04 - Reproductive System","CH:05 - Cell biology","CH:06 - Inheritance","CH:07 - Evolution","CH:08 - Biotechnology"]
                        ClassSubjList(sciList,"Class 11 English Modules",usid)

                    eng11Btn = Button(window2,image=engPhoto1,command=eng_11)
                    eng11Btn.place(x=790,y=190)

                    #11th class csc ppt button image
                    bioPhoto1=PhotoImage(master=window2,file="img/biology.png")
                    bioLabel1=Label(window2,image=bioPhoto1)

                    def bio_11():
                        sciList = ["CH:01 - Semen Anatomy","CH:02 - Transels","CH:03 - Parts of Body","CH:04 - Reproductive System","CH:05 - Cell biology","CH:06 - Inheritance","CH:07 - Evolution","CH:08 - Biotechnology","CH:01 - Semen Anatomy","CH:02 - Transels","CH:03 - Parts of Body","CH:04 - Reproductive System","CH:05 - Cell biology","CH:06 - Inheritance","CH:07 - Evolution","CH:08 - Biotechnology"]
                        ClassSubjList(sciList,"Class 11 Biology Modules",usid)

                    bio11Btn = Button(window2,image=bioPhoto1,command=bio_11)
                    bio11Btn.place(x=1020,y=190)

                if class_n==12:
                    #12th class math ppt button image
                    mathPhoto1=PhotoImage(master=window2,file="img/math_10th.png")
                    mathLabel1=Label(window2,image=mathPhoto1)

                    def math_12():
                        sciList = ["CH:01 - Semen Anatomy","CH:02 - Transels","CH:03 - Parts of Body","CH:04 - Reproductive System","CH:05 - Cell biology","CH:06 - Inheritance","CH:07 - Evolution","CH:08 - Biotechnology","CH:01 - Semen Anatomy","CH:02 - Transels","CH:03 - Parts of Body","CH:04 - Reproductive System","CH:05 - Cell biology","CH:06 - Inheritance","CH:07 - Evolution","CH:08 - Biotechnology"]
                        ClassSubjList(sciList,"Class 12 Math Modules",usid)

                    math12Btn = Button(window2,image=mathPhoto1,command=math_12)
                    math12Btn.place(x=100,y=190)


                    #12th class physics ppt button image
                    phyPhoto1=PhotoImage(master=window2,file="img/physics.png")
                    phyLabel1=Label(window2,image=phyPhoto1)

                    def phy_12():
                        sciList = ["CH:01 - Semen Anatomy","CH:02 - Transels","CH:03 - Parts of Body","CH:04 - Reproductive System","CH:05 - Cell biology","CH:06 - Inheritance","CH:07 - Evolution","CH:08 - Biotechnology","CH:01 - Semen Anatomy","CH:02 - Transels","CH:03 - Parts of Body","CH:04 - Reproductive System","CH:05 - Cell biology","CH:06 - Inheritance","CH:07 - Evolution","CH:08 - Biotechnology"]
                        ClassSubjList(sciList,"Class 12 Math Modules",usid)

                    phy12Btn = Button(window2,image=phyPhoto1,command=phy_12)
                    phy12Btn.place(x=330,y=190)

                    #12th class chemistry ppt button image
                    chemPhoto1=PhotoImage(master=window2,file="img/Chemistry.png")
                    chemLabel1=Label(window2,image=chemPhoto1)

                    def chem_12():
                        sciList = ["CH:01 - Semen Anatomy","CH:02 - Transels","CH:03 - Parts of Body","CH:04 - Reproductive System","CH:05 - Cell biology","CH:06 - Inheritance","CH:07 - Evolution","CH:08 - Biotechnology","CH:01 - Semen Anatomy","CH:02 - Transels","CH:03 - Parts of Body","CH:04 - Reproductive System","CH:05 - Cell biology","CH:06 - Inheritance","CH:07 - Evolution","CH:08 - Biotechnology"]
                        ClassSubjList(sciList,"Class 12 Chemistry Modules",usid)

                    chem12Btn = Button(window2,image=chemPhoto1,command=chem_12)
                    chem12Btn.place(x=560,y=190)
                    

                    #12th class english ppt button image
                    engPhoto1=PhotoImage(master=window2,file="img/eng_10th.png")
                    engLabel1=Label(window2,image=engPhoto1)

                    def eng_12():
                        sciList = ["CH:01 - Semen Anatomy","CH:02 - Transels","CH:03 - Parts of Body","CH:04 - Reproductive System","CH:05 - Cell biology","CH:06 - Inheritance","CH:07 - Evolution","CH:08 - Biotechnology","CH:01 - Semen Anatomy","CH:02 - Transels","CH:03 - Parts of Body","CH:04 - Reproductive System","CH:05 - Cell biology","CH:06 - Inheritance","CH:07 - Evolution","CH:08 - Biotechnology"]
                        ClassSubjList(sciList,"Class 12 English Modules",usid)

                    eng12Btn = Button(window2,image=engPhoto1,command=eng_12)
                    eng12Btn.place(x=790,y=190)

                    #12th class csc ppt button image
                    bioPhoto1=PhotoImage(master=window2,file="img/biology.png")
                    bioLabel1=Label(window2,image=bioPhoto1)

                    def bio_12():
                        sciList = ["CH:01 - Semen Anatomy","CH:02 - Transels","CH:03 - Parts of Body","CH:04 - Reproductive System","CH:05 - Cell biology","CH:06 - Inheritance","CH:07 - Evolution","CH:08 - Biotechnology","CH:01 - Semen Anatomy","CH:02 - Transels","CH:03 - Parts of Body","CH:04 - Reproductive System","CH:05 - Cell biology","CH:06 - Inheritance","CH:07 - Evolution","CH:08 - Biotechnology"]
                        ClassSubjList(sciList,"Class 12 Biology Modules",usid)

                    bio12Btn = Button(window2,image=bioPhoto1,command=bio_12)
                    bio12Btn.place(x=1020,y=190)


                #ALL SUBJECTS
                subj_label=Label(window2,text="Explore all Subjects",fg="white",bg="black",font=("Apple Braille",40,"bold"))
                subj_label.place(x=100,y=330)

                def passMathList():
                    mathList = ["CH:01 - Number System","CH:02 - Algebra","CH:03 - Coordinate Geometry","CH:04 - Geometry","CH:05 - Trigonometry","CH:06 - Mensuration","CH:07 - Statistics","CH:08 - Probablity","CH:01 - Number System","CH:02 - Algebra","CH:03 - Coordinate Geometry","CH:04 - Geometry","CH:05 - Trigognometry","CH:06 - Mensuration","CH:07 - Statistics","CH:08 - Probablity"]
                    showList(mathList,usid)

                SmathBtn=Button(window2,text="Maths",bg='black',fg='black',font=("Apple Braille",20,"bold"),width=12,command=passMathList)
                SmathBtn.place(x=170,y=420)

                def passbioList():
                    bioList = ["CH:01 - Semen Anatomy","CH:02 - Transels","CH:03 - Parts of Body","CH:04 - Reproductive System","CH:05 - Cell biology","CH:06 - Inheritance","CH:07 - Evolution","CH:08 - Biotechnology","CH:01 - Semen Anatomy","CH:02 - Transels","CH:03 - Parts of Body","CH:04 - Reproductive System","CH:05 - Cell biology","CH:06 - Inheritance","CH:07 - Evolution","CH:08 - Biotechnology"]
                    showList(bioList,usid)

                SbioBtn=Button(window2,text="Biology",bg='black',fg='black',font=("Apple Braille",20,"bold"),width=12,command=passbioList)
                SbioBtn.place(x=370,y=420)

                def passchemList():
                    chemList = ["CH:01 - Atoms and Molecules","CH:02 - Organic Chem","CH:03 - Thermodynamics","CH:04 - Electrochem","CH:05 - Surface chem","CH:06 - Alcohols","CH:07 - Polymers","CH:08 - Kinetics","CH:01 - Atoms and Molecules","CH:02 - Organic Chem","CH:03 - Thermodynamics","CH:04 - Electrochem","CH:05 - Surface chem","CH:06 - Alcohols","CH:07 - Polymers","CH:08 - Kinetics"]
                    showList(chemList,usid)

                SchemBtn=Button(window2,text="Chemistry",bg='black',fg='black',font=("Apple Braille",20,"bold"),width=12,command=passchemList)
                SchemBtn.place(x=570,y=420)

                def passphyList():
                    phyList = ["CH:01 - Kinematics","CH:02 - Motion","CH:03 - Velocity","CH:04 - Acceleration","CH:05 - Thermodynamics","CH:06 - Stress and Strain","CH:07 - Young's Module","CH:08 - Gravity","CH:01 - Kinematics","CH:02 - Motion","CH:03 - Velocity","CH:04 - Acceleration","CH:05 - Thermodynamics","CH:06 - Stress and Strain","CH:07 - Young's Module","CH:08 - Gravity"]
                    showList(phyList,usid)

                
                SphyBtn=Button(window2,text="Physics",bg='black',fg='black',font=("Apple Braille",20,"bold"),width=12,command=passphyList)
                SphyBtn.place(x=770,y=420)

                def passengList():
                    engList = ["CH:01 - Noun","CH:02 - Pronouns","CH:03 - Verbs","CH:04 - Adverbs","CH:05 - Adjective","CH:06 - Pronounciation","CH:07 - Lierature","CH:08 - Life Lessons","CH:01 - Noun","CH:02 - Pronouns","CH:03 - Verbs","CH:04 - Adverbs","CH:05 - Adjective","CH:06 - Pronounciation","CH:07 - Lierature","CH:08 - Life Lessons"]
                    showList(engList,usid)
                
                SengBtn=Button(window2,text="English",bg='black',fg='black',font=("Apple Braille",20,"bold"),width=12,command=passengList)
                SengBtn.place(x=970,y=420)

                def passTamList():
                    tamList = ["CH:01 - Kural","CH:02 - Thirukural","CH:03 - Literature","CH:04 - Seyul","CH:05 - Adfgus","CH:06 - Pdufhu","CH:07 - Ldscdjscgh","CH:08 - Lueyw","CH:01 - Kural","CH:02 - Thirukural","CH:03 - Literature","CH:04 - Seyul","CH:05 - Adfgus","CH:06 - Pdufhu","CH:07 - Ldscdjscgh","CH:08 - Lueyw"]
                    showList(tamList,usid)
                
                StamBtn=Button(window2,text="Tamil",bg='black',fg='black',font=("Apple Braille",20,"bold"),width=12,command=passTamList)
                StamBtn.place(x=170,y=480)

                def passgeoList():
                    geoList = ["CH:01 - Japan","CH:02 - Paris","CH:03 - London","CH:04 - France","CH:05 - Earth","CH:06 - India","CH:07 - States of India","CH:08 - Western ghats","CH:01 - Japan","CH:02 - Paris","CH:03 - London","CH:04 - France","CH:05 - Earth","CH:06 - India","CH:07 - States of India","CH:08 - Western ghats"]
                    showList(geoList,usid)
                
                SgeoBtn=Button(window2,text="Geography",bg='black',fg='black',font=("Apple Braille",20,"bold"),width=12,command=passgeoList)
                SgeoBtn.place(x=370,y=480)

                
                ShisBtn=Button(window2,text="History",bg='black',fg='black',font=("Apple Braille",20,"bold"),width=12,command=passgeoList)
                ShisBtn.place(x=570,y=480)

                ScivBtn=Button(window2,text="Civics",bg='black',fg='black',font=("Apple Braille",20,"bold"),width=12,command=passgeoList)
                ScivBtn.place(x=770,y=480)

                ScscBtn=Button(window2,text="Computer science",bg='black',fg='black',font=("Apple Braille",20,"bold"),width=12,command=passgeoList)
                ScscBtn.place(x=970,y=480)

                ShinBtn=Button(window2,text="Hindi",bg='black',fg='black',font=("Apple Braille",20,"bold"),width=12,command=passgeoList)
                ShinBtn.place(x=170,y=540)

                SecoBtn=Button(window2,text="Economics",bg='black',fg='black',font=("Apple Braille",20,"bold"),width=12,command=passgeoList)
                SecoBtn.place(x=370,y=540)

                SentBtn=Button(window2,text="Entertainment",bg='black',fg='black',font=("Apple Braille",20,"bold"),width=12,command=passgeoList)
                SentBtn.place(x=570,y=540)

                SaccBtn=Button(window2,text="Accounts",bg='black',fg='black',font=("Apple Braille",20,"bold"),width=12,command=passgeoList)
                SaccBtn.place(x=770,y=540)

                ScomBtn=Button(window2,text="Commerce",bg='black',fg='black',font=("Apple Braille",20,"bold"),width=12,command=passgeoList)
                ScomBtn.place(x=970,y=540)
                
                

                window2.mainloop()

            def libraryPage():
                window3=Tk()  #window3 is library page
                window3.geometry("2500x1000")
                window3.title("Intelligent Educational Assist || Library Page")
                window3.config(bg="black")

                def homePageL():
                    window3.destroy()
                    welcome()

                homeBtn=Button(window3,text="Home",bg='blue',fg='black',font=("arial",17,"bold"),width=8,command=homePageL)
                homeBtn.place(x=400,y=20)

                def explorePageL():
                    window3.destroy()
                    explorePage()

                expBtn=Button(window3,text="Explore",bg='black',fg='black',font=("arial",17,"bold"),width=8,command=explorePageL)
                expBtn.place(x=550,y=20)


                #no command as this lib button is in lib page itself
                libBtn=Button(window3,text="Library",bg='black',fg='black',font=("arial",15,"bold"),width=8)
                libBtn.place(x=700,y=20)

                #srch image here
                srchPhoto=PhotoImage(master=window3,file="img/searchButton-2-2.png")
                srchLabel=Label(window3,image=srchPhoto)
                srchLabel.place(x=860,y=20)

                searchEntry=Entry(window3, font=("Comic Sans MS",13),width=27)
                searchEntry.place(x=900,y=20)

                def searchpass():
                    val = searchEntry.get()
                    searchppt(val)

                srchBtn=Button(window3,text="Search",bg='black',fg='black',font=("arial",12,"bold"),width=6,command=searchpass)
                srchBtn.place(x=1160,y=20)

                #adding a profile pic image as a button
                prflePhoto=PhotoImage(master=window3,file="img/profilePic.png")
                prflLabel=Label(window3,image=prflePhoto)

                pfleBtn = Button(window3,image=prflePhoto,command=my_profile)
                pfleBtn.place(x=1300,y=20)

                urCollec_label=Label(window3,text="Your Collections ! ",fg="white",bg="black",font=("Apple Braille",40,"bold"))
                urCollec_label.place(x=100,y=130)

                filename = "libraryData.csv"
                rows = []
                with open(filename, 'r') as csvfile:
                    #creating a csv reader object
                    csvreader = csv.reader(csvfile)

                    # extracting each data row one by one
                    for i in csvreader:
                        rows.append(i)
                collec_n=0
                listt = []
                for i in rows:
                    if i!=[]:
                        if i[0]==usid:
                            collec_n+=1
                            listt.append(i[1])

                listt = list(set(listt))
                nsv = len(listt)

                listt.reverse()

                list1 = listt[:5]
                list2 = listt[5:]

                if collec_n==0:
                    noCollec_label=Label(window3,text="Your saved lectures will appear here !",fg="gray",bg="black",font=("Apple Braille",35))
                    noCollec_label.place(x=250,y=280)
                else:
                    #library algorithm
                    mytext = "You have saved "+str(nsv)+" modules in your collections"
                    lib_label2=Label(window3,text=mytext,fg="gray",bg="black",font=("Apple Braille",25))
                    lib_label2.place(x=230,y=190)

                    vdo1x = list1[0]
                    if len(list1)>=2:
                        vdo2x = list1[1]
                    if len(list1)>=3:
                        vdo3x = list1[2]
                    if len(list1)>=4:
                        vdo4x = list1[3]
                    if len(list1)>=5:
                        vdo5x = list1[4]

                    #Image Buttons
                    #1
                    vdo1=PhotoImage(master=window3,file="img/libraryIcon.png")
                    vdo1Lbl=Label(window3,image=vdo1)

                    def vdo1func():
                        playPpt(vdo1x)

                    vdo1Btn = Button(window3,image=vdo1,borderwidth=0,command=vdo1func)
                    vdo1Btn.place(x=100,y=240)

                    #2
                    if len(list1)>=2:
                        vdo2=PhotoImage(master=window3,file="img/libraryIcon.png")
                        vdo2Lbl=Label(window3,image=vdo2)

                        def vdo2func():
                            playPpt(vdo2x)

                        vdo2Btn = Button(window3,image=vdo2,borderwidth=0,command=vdo2func)
                        vdo2Btn.place(x=330,y=240)

                    #3
                    if len(list1)>=3:
                        vdo3=PhotoImage(master=window3,file="img/libraryIcon.png")
                        vdo3Lbl=Label(window3,image=vdo3)

                        def vdo3func():
                            playPpt(vdo3x)

                        vdo3Btn = Button(window3,image=vdo3,borderwidth=0,command=vdo3func)
                        vdo3Btn.place(x=560,y=240)

                    #4
                    if len(list1)>=4:
                        vdo4=PhotoImage(master=window3,file="img/libraryIcon.png")
                        vdo4Lbl=Label(window3,image=vdo4)

                        def vdo4func():
                            playPpt(vdo4x)

                        vdo4Btn = Button(window3,image=vdo4,borderwidth=0,command=vdo4func)
                        vdo4Btn.place(x=790,y=240)

                    #5
                    if len(list1)>=5:
                        vdo5=PhotoImage(master=window3,file="img/libraryIcon.png")
                        vdo5Lbl=Label(window3,image=vdo5)

                        def vdo5func():
                            playPpt(vdo5x)

                        vdo5Btn = Button(window3,image=vdo5,borderwidth=0,command=vdo5func)
                        vdo5Btn.place(x=1020,y=240)

                    #Image labels
                    v1Lbl=Label(window3,text=vdo1x,fg="white",bg="black",font=("Apple Braille",15,"bold"))
                    v1Lbl.place(x=100,y=335)

                    if len(list1)>=2:
                        v2Lbl=Label(window3,text=vdo2x,fg="white",bg="black",font=("Apple Braille",15,"bold"))
                        v2Lbl.place(x=330,y=335)

                    if len(list1)>=3:
                        v3Lbl=Label(window3,text=vdo3x,fg="white",bg="black",font=("Apple Braille",15,"bold"))
                        v3Lbl.place(x=560,y=335)

                    if len(list1)>=4:
                        v4Lbl=Label(window3,text=vdo4x,fg="white",bg="black",font=("Apple Braille",15,"bold"))
                        v4Lbl.place(x=790,y=335)

                    if len(list1)>=5:
                        v5Lbl=Label(window3,text=vdo5x,fg="white",bg="black",font=("Apple Braille",15,"bold"))
                        v5Lbl.place(x=1020,y=335)

                    def more_history():
                        showList(list2,usid)
                    more_button=Button(window3,text="More...",fg='black',relief=RIDGE,font=("Comic Sans MS",12,"bold"),width=8,command=more_history)
                    more_button.place(x=100,y=400)


                pick_label=Label(window3,text="Picked for You ! ",fg="white",bg="black",font=("Apple Braille",40,"bold"))
                pick_label.place(x=100,y=460)

                allModules = ["CH:01 - Number System","CH:02 - Algebra","CH:03 - Coordinate Geometry","CH:04 - Geometry",

                            "CH:05 - Trigonometry","CH:06 - Mensuration","CH:07 - Statistics","CH:08 - Probablity",

                            "CH:01 - Semen Anatomy","CH:02 - Transels","CH:03 - Parts of Body","CH:04 - Reproductive System",

                            "CH:05 - Cell biology","CH:06 - Inheritance","CH:07 - Evolution","CH:08 - Biotechnology",

                            "CH:01 - Atoms and Molecules","CH:02 - Organic Chem","CH:03 - Thermodynamics","CH:04 - Electrochem",

                            "CH:05 - Surface chem","CH:06 - Alcohols","CH:07 - Polymers","CH:08 - Kinetics",

                            "CH:01 - Kinematics","CH:02 - Motion","CH:03 - Velocity","CH:04 - Acceleration",

                            "CH:06 - Stress and Strain","CH:07 - Young's Module","CH:08 - Gravity",

                            "CH:01 - Noun","CH:02 - Pronouns","CH:03 - Verbs","CH:04 - Adverbs","CH:05 - Adjective",

                            "CH:06 - Pronounciation","CH:07 - Lierature","CH:08 - Life Lessons", 

                            "CH:01 - Kural","CH:02 - Thirukural","CH:03 - Literature","CH:04 - Seyul","CH:05 - Adfgus",

                            "CH:06 - Pdufhu","CH:07 - Ldscdjscgh","CH:08 - Lueyw", "CH:01 - Japan","CH:02 - Paris","CH:03 - London",

                            "CH:04 - France","CH:05 - Earth","CH:06 - India","CH:07 - States of India","CH:08 - Western ghats","CH:09 - Solar System"
                            
                            ]

                filename = "sampledata.csv"
                rows = []
                with open(filename, 'r') as csvfile:
                    #creating a csv reader object
                    csvreader = csv.reader(csvfile)

                    # extracting each data row one by one
                    for i in csvreader:
                        rows.append(i)

                watched_chaps=[]
                for i in rows:
                    if i!=[] and i[0]==usid:
                        watched_chaps.append(i[1])

                allModules1 = set(allModules)
                watched_chaps = set(watched_chaps)

                diff_list = list(allModules1.difference(watched_chaps))

                recomendation_list = random.choices(diff_list, k=5)

                image_sci = allModules[8:31]
                image_soc = allModules[47:]
                image_tam = allModules[39:43]
                image_mat = allModules[:8]
                image_csc = allModules[43:47]
                image_eng = allModules[31:39]

                #ADD IMAGE BUTTONS FOR RECOMENDATION
                # co ords : y is 550
                # x: 100,330,560,790,1020

                #Image labels
                r1Lbl=Label(window3,text=recomendation_list[0],fg="white",bg="black",font=("Apple Braille",15,"bold"))
                r1Lbl.place(x=100,y=672)

                r2Lbl=Label(window3,text=recomendation_list[1],fg="white",bg="black",font=("Apple Braille",15,"bold"))
                r2Lbl.place(x=330,y=672)

                r3Lbl=Label(window3,text=recomendation_list[2],fg="white",bg="black",font=("Apple Braille",15,"bold"))
                r3Lbl.place(x=560,y=672)

                r4Lbl=Label(window3,text=recomendation_list[3],fg="white",bg="black",font=("Apple Braille",15,"bold"))
                r4Lbl.place(x=790,y=672)

                r5Lbl=Label(window3,text=recomendation_list[4],fg="white",bg="black",font=("Apple Braille",15,"bold"))
                r5Lbl.place(x=1020,y=672)

                #BUTTON 1
                if recomendation_list[0] in image_mat:
                    rec_vdo1=PhotoImage(master=window3,file="img/matRec.png")
                elif recomendation_list[0] in image_csc:
                    rec_vdo1=PhotoImage(master=window3,file="img/cscRec.png")
                elif recomendation_list[0] in image_sci:
                    rec_vdo1=PhotoImage(master=window3,file="img/sciRec.png")
                elif recomendation_list[0] in image_soc:
                    rec_vdo1=PhotoImage(master=window3,file="img/socRec.png")
                elif recomendation_list[0] in image_tam:
                    rec_vdo1=PhotoImage(master=window3,file="img/tamRec.png")
                elif recomendation_list[0] in image_eng:
                    rec_vdo1=PhotoImage(master=window3,file="img/engRec.png")

                def recvdo1():
                    playPpt(recomendation_list[0])
                
                rec_vdo1Lbl=Label(window3,image=rec_vdo1)
                rec_vdo1Btn = Button(window3,image=rec_vdo1,borderwidth=0,command=recvdo1)
                rec_vdo1Btn.place(x=100,y=550)

                #BUTTON 2
                if recomendation_list[1] in image_mat:
                    rec_vdo2=PhotoImage(master=window3,file="img/matRec.png")
                elif recomendation_list[1] in image_csc:
                    rec_vdo2=PhotoImage(master=window3,file="img/cscRec.png")
                elif recomendation_list[1] in image_sci:
                    rec_vdo2=PhotoImage(master=window3,file="img/sciRec.png")
                elif recomendation_list[1] in image_soc:
                    rec_vdo2=PhotoImage(master=window3,file="img/socRec.png")
                elif recomendation_list[1] in image_tam:
                    rec_vdo2=PhotoImage(master=window3,file="img/tamRec.png")
                elif recomendation_list[1] in image_eng:
                    rec_vdo2=PhotoImage(master=window3,file="img/engRec.png")

                def recvdo2():
                    playPpt(recomendation_list[1])
                
                rec_vdo2Lbl=Label(window3,image=rec_vdo2)
                rec_vdo2Btn = Button(window3,image=rec_vdo2,borderwidth=0,command=recvdo2)
                rec_vdo2Btn.place(x=330,y=550)

                #BUTTON 3
                if recomendation_list[2] in image_mat:
                    rec_vdo3=PhotoImage(master=window3,file="img/matRec.png")
                elif recomendation_list[2] in image_csc:
                    rec_vdo3=PhotoImage(master=window3,file="img/cscRec.png")
                elif recomendation_list[2] in image_sci:
                    rec_vdo3=PhotoImage(master=window3,file="img/sciRec.png")
                elif recomendation_list[2] in image_soc:
                    rec_vdo3=PhotoImage(master=window3,file="img/socRec.png")
                elif recomendation_list[2] in image_tam:
                    rec_vdo3=PhotoImage(master=window3,file="img/tamRec.png")
                elif recomendation_list[2] in image_eng:
                    rec_vdo3=PhotoImage(master=window3,file="img/engRec.png")

                def recvdo3():
                    playPpt(recomendation_list[2])
                
                rec_vdo3Lbl=Label(window3,image=rec_vdo1)
                rec_vdo3Btn = Button(window3,image=rec_vdo3,borderwidth=0,command=recvdo3)
                rec_vdo3Btn.place(x=560,y=550)

                #BUTTON 4
                if recomendation_list[3] in image_mat:
                    rec_vdo4=PhotoImage(master=window3,file="img/matRec.png")
                elif recomendation_list[3] in image_csc:
                    rec_vdo4=PhotoImage(master=window3,file="img/cscRec.png")
                elif recomendation_list[3] in image_sci:
                    rec_vdo4=PhotoImage(master=window3,file="img/sciRec.png")
                elif recomendation_list[3] in image_soc:
                    rec_vdo4=PhotoImage(master=window3,file="img/socRec.png")
                elif recomendation_list[3] in image_tam:
                    rec_vdo4=PhotoImage(master=window3,file="img/tamRec.png")
                elif recomendation_list[3] in image_eng:
                    rec_vdo4=PhotoImage(master=window3,file="img/engRec.png")

                def recvdo4():
                    playPpt(recomendation_list[3])
                
                rec_vdo4Lbl=Label(window3,image=rec_vdo4)
                rec_vdo4Btn = Button(window3,image=rec_vdo4,borderwidth=0,command=recvdo4)
                rec_vdo4Btn.place(x=790,y=550)

                #BUTTON 5
                if recomendation_list[4] in image_mat:
                    rec_vdo5=PhotoImage(master=window3,file="img/matRec.png")
                elif recomendation_list[4] in image_csc:
                    rec_vdo5=PhotoImage(master=window3,file="img/cscRec.png")
                elif recomendation_list[4] in image_sci:
                    rec_vdo5=PhotoImage(master=window3,file="img/sciRec.png")
                elif recomendation_list[4] in image_soc:
                    rec_vdo5=PhotoImage(master=window3,file="img/socRec.png")
                elif recomendation_list[4] in image_tam:
                    rec_vdo5=PhotoImage(master=window3,file="img/tamRec.png")
                elif recomendation_list[4] in image_eng:
                    rec_vdo5=PhotoImage(master=window3,file="img/engRec.png")

                def recvdo5():
                    playPpt(recomendation_list[4])
                
                rec_vdo5Lbl=Label(window3,image=rec_vdo5)
                rec_vdo5Btn = Button(window3,image=rec_vdo5,borderwidth=0,command=recvdo5)
                rec_vdo5Btn.place(x=1020,y=550)



                

                window3.mainloop()



            #Home page

            #no command as this home button is in home page itself
            homeBtn=Button(window1,text="Home",bg='black',fg='black',font=("arial",17,"bold"),width=8)
            homeBtn.place(x=400,y=20)

            def explorePageH():
                window1.destroy()
                explorePage()

            expBtn=Button(window1,text="Explore",bg='black',fg='black',font=("arial",17,"bold"),width=8,command=explorePageH)
            expBtn.place(x=550,y=20)

            def libraryPageH():
                window1.destroy()
                libraryPage()

            libBtn=Button(window1,text="Library",bg='black',fg='black',font=("arial",15,"bold"),width=8,command=libraryPageH)
            libBtn.place(x=700,y=20)
  
            #srch image
            srchPhoto=PhotoImage(master=window1,file="img/searchButton-2-2.png")
            srchLabel=Label(window1,image=srchPhoto)
            srchLabel.place(x=860,y=20)

            searchEntry=Entry(window1, font=("Comic Sans MS",13),width=27)
            searchEntry.place(x=900,y=20)

            def searchpass():
                val = searchEntry.get()
                searchppt(val)

            srchBtn=Button(window1,text="Search",bg='black',fg='black',font=("arial",12,"bold"),width=6,command=searchpass)
            srchBtn.place(x=1160,y=20)

            #adding a profile pic image as a button
            prflePhoto=PhotoImage(master=window1,file="img/profilePic.png")
            prflLabel=Label(window1,image=prflePhoto)

            def my_profile():
                query = """select name,mail,mno,class,addr from basicInfo where userid=%s"""
                cursor.execute(query,(usid,)) 
                res=cursor.fetchall()

                prof_window=Tk()
                prof_window.geometry("400x400")
                prof_window.title("Profile page")
                prof_window.config(bg="turquoise")
                prof_window.resizable(False,False)

                prof_label=Label(prof_window,text="My profile ",fg="black",bg="turquoise",font=("Apple Braille",30,"bold"))
                prof_label.place(x=130,y=20)

                nameLbl = Label(prof_window,text="Name: ",fg="black",bg="turquoise",font=("Apple Braille",20,"bold"))
                nameLbl.place(x=50,y=80)
                name=res[0][0]
                nameval = Label(prof_window,text=name,fg="black",bg="turquoise",font=("Apple Braille",20,"bold"))
                nameval.place(x=180,y=80)

                mnoLbl = Label(prof_window,text="Mobile No.: ",fg="black",bg="turquoise",font=("Apple Braille",20,"bold"))
                mnoLbl.place(x=50,y=120)
                mno=res[0][2]
                mno=str(mno)
                mnoval = Label(prof_window,text=mno,fg="black",bg="turquoise",font=("Apple Braille",20,"bold"))
                mnoval.place(x=180,y=120)

                emailLbl = Label(prof_window,text="E-mail: ",fg="black",bg="turquoise",font=("Apple Braille",20,"bold"))
                emailLbl.place(x=50,y=160)
                mail=res[0][1]
                mailval = Label(prof_window,text=mail,fg="black",bg="turquoise",font=("Apple Braille",20,"bold"))
                mailval.place(x=180,y=160)

                clLbl = Label(prof_window,text="Class: ",fg="black",bg="turquoise",font=("Apple Braille",20,"bold"))
                clLbl.place(x=50,y=200)
                cl=res[0][3]
                cl=str(cl)
                clval = Label(prof_window,text=cl,fg="black",bg="turquoise",font=("Apple Braille",20,"bold"))
                clval.place(x=180,y=200)

                adLbl = Label(prof_window,text="Address: ",fg="black",bg="turquoise",font=("Apple Braille",20,"bold"))
                adLbl.place(x=50,y=240)
                ad=res[0][4]
                adval = Label(prof_window,text=ad,fg="black",bg="turquoise",font=("Apple Braille",20,"bold"))
                adval.place(x=180,y=240)

                def homeLogout():
                    if messagebox.askokcancel("Quit", "Are you sure you want to Logout?"):
                        prof_window.destroy()
                        window1.destroy()
                        messagebox.showinfo("Error","Logged out Successfully")

                logout_button=Button(prof_window,text="Logout",fg='black',bg="red",relief=RIDGE,font=("Comic Sans MS",12,"bold"),width=12,command=homeLogout)
                logout_button.place(x=130,y=290)



            pfleBtn = Button(window1,image=prflePhoto,command=my_profile)
            pfleBtn.place(x=1300,y=20)

            #adding a welcome message on the top.
            welcome_label=Label(window1,text="Welcome ",fg="white",bg="black",font=("Apple Braille",40,"bold"))
            welcome_label.place(x=100,y=130)
            query_name="select name from basicInfo where userid=%s"
            cursor.execute(query_name,(usid,))
            w_name=cursor.fetchall()
            welcomename_label=Label(window1, text=w_name, fg="white",bg="black",font=("Apple Braille",40,"bold"))
            welcomename_label.place(x=280,y=130)

            
            #HISTORY PART
            his_label=Label(window1,text="History ",fg="white",bg="black",font=("Apple Braille",30,"bold"))
            his_label.place(x=100,y=180)

            filename = "sampledata.csv"
            rows = []
            with open(filename, 'r') as csvfile:
                #creating a csv reader object
                csvreader = csv.reader(csvfile)
        
                # extracting each data row one by one
                for i in csvreader:
                    rows.append(i)

            nvv=0
            listt = []
            for i in rows:
                if i!=[]:
                    if i[0]==usid:
                        nvv+=1
                        listt.append(i[1])

            listt.reverse()

            list1 = listt[:5]
            list2 = listt[5:]

            if nvv==0:
                his_label1=Label(window1,text="Your previously watched modules will appear here ",fg="gray",bg="black",font=("Apple Braille",35))
                his_label1.place(x=250,y=330)
            else:
                #history algorithm
                mytext = "You have watched "+str(nvv)+" modules in total"
                his_label2=Label(window1,text=mytext,fg="gray",bg="black",font=("Apple Braille",25))
                his_label2.place(x=230,y=190)

            #finding which video
            if list1!=[]:
                vdo1x = list1[0]
                if len(list1)>=2:
                    vdo2x = list1[1]
                if len(list1)>=3:
                    vdo3x = list1[2]
                if len(list1)>=4:
                    vdo4x = list1[3]
                if len(list1)>=5:
                    vdo5x = list1[4]

                #Image Buttons
                #1
                vdo1=PhotoImage(master=window1,file="img/historyicon.png")
                vdo1Lbl=Label(window1,image=vdo1)

                def vdo1func():
                    playPpt(vdo1x)

                vdo1Btn = Button(window1,image=vdo1,borderwidth=0,command=vdo1func)
                vdo1Btn.place(x=100,y=240)

                #2
                if len(list1)>=2:
                    vdo2=PhotoImage(master=window1,file="img/historyicon.png")
                    vdo2Lbl=Label(window1,image=vdo2)

                    def vdo2func():
                        playPpt(vdo2x)

                    vdo2Btn = Button(window1,image=vdo2,borderwidth=0,command=vdo2func)
                    vdo2Btn.place(x=330,y=240)

                #3
                if len(list1)>=3:
                    vdo3=PhotoImage(master=window1,file="img/historyicon.png")
                    vdo3Lbl=Label(window1,image=vdo3)

                    def vdo3func():
                        playPpt(vdo3x)

                    vdo3Btn = Button(window1,image=vdo3,borderwidth=0,command=vdo3func)
                    vdo3Btn.place(x=560,y=240)

                #4
                if len(list1)>=4:
                    vdo4=PhotoImage(master=window1,file="img/historyicon.png")
                    vdo4Lbl=Label(window1,image=vdo4)

                    def vdo4func():
                        playPpt(vdo4x)

                    vdo4Btn = Button(window1,image=vdo4,borderwidth=0,command=vdo4func)
                    vdo4Btn.place(x=790,y=240)

                #5
                if len(list1)>=5:
                    vdo5=PhotoImage(master=window1,file="img/historyicon.png")
                    vdo5Lbl=Label(window1,image=vdo5)

                    def vdo5func():
                        playPpt(vdo5x)

                    vdo5Btn = Button(window1,image=vdo5,borderwidth=0,command=vdo5func)
                    vdo5Btn.place(x=1020,y=240)

                #Image labels
                v1Lbl=Label(window1,text=vdo1x,fg="white",bg="black",font=("Apple Braille",15,"bold"))
                v1Lbl.place(x=100,y=330)

                if len(list1)>=2:
                    v2Lbl=Label(window1,text=vdo2x,fg="white",bg="black",font=("Apple Braille",15,"bold"))
                    v2Lbl.place(x=330,y=330)

                if len(list1)>=3:
                    v3Lbl=Label(window1,text=vdo3x,fg="white",bg="black",font=("Apple Braille",15,"bold"))
                    v3Lbl.place(x=560,y=330)

                if len(list1)>=4:
                    v4Lbl=Label(window1,text=vdo4x,fg="white",bg="black",font=("Apple Braille",15,"bold"))
                    v4Lbl.place(x=790,y=330)

                if len(list1)>=5:
                    v5Lbl=Label(window1,text=vdo5x,fg="white",bg="black",font=("Apple Braille",15,"bold"))
                    v5Lbl.place(x=1020,y=330)

                def more_history():
                    showList(list2,usid)
                more_button=Button(window1,text="More...",fg='black',relief=RIDGE,font=("Comic Sans MS",12,"bold"),width=8,command=more_history)
                more_button.place(x=100,y=400)


            
            #Finding the standard of the student and displaying its respective tutorials
            query = """select class from basicInfo where userid=%s"""
            cursor.execute(query,(usid,)) 
            res=cursor.fetchall()
            class_n = res[0][0]
            title = "Class "+str(class_n)+" modules"
            his_label=Label(window1,text=title,fg="white",bg="black",font=("Apple Braille",30,"bold"))
            his_label.place(x=100,y=500)

            
            if class_n==10 or class_n==11 or class_n==12:
                #display all class ppts

                frame1 = Frame(window1,height=140,width=1150,bg="black",bd=1,relief=FLAT)
                frame1.place(x=100,y=550)


                #solar system
                solarsys=PhotoImage(master=frame1,file="img/solarsystem.png")
                solarsysLbl=Label(frame1,image=solarsys)

                def homevdo1():
                    solarsysP(usid)

                solarsysBtn = Button(frame1,image=solarsys,borderwidth=0,command=homevdo1)
                solarsysBtn.place(x=10,y=10)


                #parts of body
                bodyparts=PhotoImage(master=frame1,file="img/partsBody.png")
                bodypartsLbl=Label(frame1,image=bodyparts)

                def homevdo2():
                    bodypartsP(usid)

                bodyBtn = Button(frame1,image=bodyparts,borderwidth=0,command=homevdo2)
                bodyBtn.place(x=240,y=10)

                #earth
                earth=PhotoImage(master=frame1,file="img/earth.png")
                earthLbl=Label(frame1,image=earth)

                def homevdo3():
                    earthPpt(usid)

                earthBtn = Button(frame1,image=earth,borderwidth=0,command=homevdo3)
                earthBtn.place(x=470,y=10)

                #Science
                science=PhotoImage(master=frame1,file="img/science.png")
                scienceLbl=Label(frame1,image=science)

                def homevdo4():
                    scienceP(usid)

                scienceBtn = Button(frame1,image=science,borderwidth=0,command=homevdo4)
                scienceBtn.place(x=700,y=10)

                #History
                history=PhotoImage(master=frame1,file="img/historical-evolution-3.png")
                historyLbl=Label(frame1,image=history)

                def homevdo5():
                    historyP(usid)

                historyBtn = Button(frame1,image=history,borderwidth=0,command=homevdo5)
                historyBtn.place(x=930,y=10)

                def openNewFrame():
                    frame2 = Frame(window1,height=140,width=1150,bg="black",bd=1,relief=FLAT)
                    frame2.place(x=100,y=550)

                    pic1=PhotoImage(master=frame2,file="img/frame2_1.png")
                    pic1Lbl=Label(frame2,image=pic1)

                    pic1Btn = Button(frame2,image=pic1,borderwidth=0,command=None)
                    pic1Btn.place(x=10,y=10)

                    pic2=PhotoImage(master=frame2,file="img/frame2_2.png")
                    pic2Lbl=Label(frame2,image=pic2)

                    pic2Btn = Button(frame2,image=pic2,borderwidth=0,command=None)
                    pic2Btn.place(x=240,y=10)

                    pic3=PhotoImage(master=frame2,file="img/frame2_3.png")
                    pic3Lbl=Label(frame2,image=pic3)

                    pic3Btn = Button(frame2,image=pic3,borderwidth=0,command=None)
                    pic3Btn.place(x=470,y=10)

                    pic4=PhotoImage(master=frame2,file="img/frame2_4.png")
                    pic4Lbl=Label(frame2,image=pic4)

                    pic4Btn = Button(frame2,image=pic4,borderwidth=0,command=None)
                    pic4Btn.place(x=700,y=10)

                    pic5=PhotoImage(master=frame2,file="img/frame2_5.png")
                    pic5Lbl=Label(frame2,image=pic5)

                    pic5Btn = Button(frame2,image=pic5,borderwidth=0,command=None)
                    pic5Btn.place(x=930,y=10)

                    mainloop()

                nextBtnimg=PhotoImage(master=window1,file="img/nextButton.png")
                nextBtnLbl=Label(window1,image=nextBtnimg)

                next_button=Button(window1,image=nextBtnimg,borderwidth=0,command=openNewFrame)
                next_button.place(x=1200,y=500)

                def openOldFrame():
                    frame1 = Frame(window1,height=140,width=1150,bg="black",bd=1,relief=FLAT)
                    frame1.place(x=100,y=550)


                    #solar system
                    solarsys=PhotoImage(master=frame1,file="img/solarsystem.png")
                    solarsysLbl=Label(frame1,image=solarsys)

                    def homevdo1():
                        solarsysP(usid)

                    solarsysBtn = Button(frame1,image=solarsys,borderwidth=0,command=homevdo1)
                    solarsysBtn.place(x=10,y=10)


                    #parts of body
                    bodyparts=PhotoImage(master=frame1,file="img/partsBody.png")
                    bodypartsLbl=Label(frame1,image=bodyparts)

                    def homevdo2():
                        bodypartsP(usid)

                    bodyBtn = Button(frame1,image=bodyparts,borderwidth=0,command=homevdo2)
                    bodyBtn.place(x=240,y=10)

                    #earth
                    earth=PhotoImage(master=frame1,file="img/earth.png")
                    earthLbl=Label(frame1,image=earth)

                    def homevdo3():
                        earthPpt(usid)

                    earthBtn = Button(frame1,image=earth,borderwidth=0,command=homevdo3)
                    earthBtn.place(x=470,y=10)

                    #Science
                    science=PhotoImage(master=frame1,file="img/science.png")
                    scienceLbl=Label(frame1,image=science)

                    def homevdo4():
                        scienceP(usid)

                    scienceBtn = Button(frame1,image=science,borderwidth=0,command=homevdo4)
                    scienceBtn.place(x=700,y=10)

                    #History
                    history=PhotoImage(master=frame1,file="img/historical-evolution-3.png")
                    historyLbl=Label(frame1,image=history)

                    def homevdo5():
                        historyP(usid)

                    historyBtn = Button(frame1,image=history,borderwidth=0,command=homevdo5)
                    historyBtn.place(x=930,y=10)

                    mainloop()

                backBtnimg=PhotoImage(master=window1,file="img/backButton.png")
                backBtnLbl=Label(window1,image=backBtnimg)

                back_button=Button(window1,image=backBtnimg,borderwidth=0,command=openOldFrame)
                back_button.place(x=1160,y=500)


            
            # if res2==[('blind',)]:
            #     usname = w_name[0][0]
            #     assist1.wishMe()
            #     assist1.username(usname)
            #     assist1.mainprog()
                
                
            window1.mainloop()

        else:
            #if entered values are incorrect:
            messagebox.showerror("Error","Incorrect userid/password")
    else:
        #if no value is entered
        messagebox.showerror("Error","Please fill your details!")

#button used to login to your acc
login_button=Button(window,text="Login",fg='black',bg="black",relief=RIDGE,font=("arial",12,"bold"),width=12,command=welcome)
login_button.place(x=110,y=400)

#button used to register yourself to the assist.
reg_button=Button(window,text="Register",fg='black',bg="black",relief=RIDGE,font=("arial",12,"bold"),width=12,command=Reg_form)
reg_button.place(x=270,y=400)

window.mainloop()
