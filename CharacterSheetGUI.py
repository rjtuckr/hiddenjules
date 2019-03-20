from tkinter import *
import tkinter

import pymysql
from ReadConfig import read_db_config
db = None

class CharacterSheet():
    def __init__(self):

        characters = []

    def GUI(self):

        window = Tk()
        window.title("Character Sheet")

        name_frame = Frame(window)
        name_frame.grid()

        first_name = Label(name_frame, text="First Name")
        first_name.grid()

        self.fnameVar = StringVar()

        self.first_name_e = Entry(name_frame, textvariable=self.fnameVar)
        self.first_name_e.grid(row=0,column=1,columnspan=2,sticky='w')

        last_name = Label(name_frame, text="Last Name")
        last_name.grid(row=0, column=2)

        self.lnameVar = StringVar()

        self.last_name_e = Entry(name_frame, textvariable=self.lnameVar)
        self.last_name_e.grid(row=0,column=3,columnspan=3)

        race = Label(name_frame, text="Race")
        race.grid(row=1)

        self.raceVar = StringVar()

        self.race_e = Entry(name_frame, textvariable = self.raceVar)
        self.race_e.grid(row=1,column=1,sticky='w')

        gender = Label(name_frame, text="Gender")
        gender.grid(row=1,column=2)

        self.genderVar = StringVar()

        self.gender_e = Entry(name_frame, textvariable=self.genderVar,width=7)
        self.gender_e.grid(row=1,column=3,sticky='w')

        age = Label(name_frame, text="Age")
        age.grid(row=1,column=4,sticky='w')

        self.ageVar = StringVar()

        self.age_e = Entry(name_frame, textvariable=self.ageVar,width=7)
        self.age_e.grid(row=1,column=5)

        title_frame = Frame(window)
        title_frame.grid()

        title = Label(name_frame, text="Title(s)")
        title.grid(row=2)

        self.titleVar = StringVar()

        self.title_e = Entry(name_frame, textvariable = self.titleVar,width=51)
        self.title_e.grid(row=2,column=1,columnspan=5,sticky='w')

        description = Label(name_frame, text="Description:")
        description.grid(row=3)

        descrip = Frame(window)
        descrip.grid(row=4)

        self.T = Text(descrip, height=10, width=53,font='arial', wrap=WORD)
        self.T.grid(row=4)
        self.T.config(font=('arial',10))

        history = Label(descrip, text="History:")
        history.grid(row=5,sticky='w')

        self.H = Text(descrip, height=10, width=53, wrap=WORD)
        self.H.grid(row=6)
        self.H.config(font=('arial',10))

        buttons_frame = Frame(window)
        buttons_frame.grid()

        addB = Button(buttons_frame, text="Save", command=self.write2db)
        addB.grid(row=7)

        clearB = Button(buttons_frame, text="Clear",command=self.clearentries)
        clearB.grid(row=7,column=1)

        window.mainloop()

    def retrieve_Tinput(self):
        return (self.T.get("1.0",'end-1c'))

    def retrieve_Hinput(self):
        return (self.H.get("1.0",'end-1c'))

    def clearentries(self):
        self.first_name_e.delete(0, 'end')
        self.last_name_e.delete(0,'end')
        self.race_e.delete(0, 'end')
        self.gender_e.delete(0, 'end')
        self.age_e.delete(0, 'end')
        self.title_e.delete(0, 'end')
        self.T.delete(0,'end')
        self.H.delete(0,'end')
        self.first_name_e.focus()  # Sets focus back to name

    def write2db(self):
        sql = "INSERT INTO Information (First_Name, Last_Name, Race, Gender, Age, Titles, Description, History)" \
                    "VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (self.fnameVar.get(), self.lnameVar.get(), self.raceVar.get(),
                                       self.genderVar.get(), self.ageVar.get(), self.titleVar.get(), self.retrieve_Tinput(), self.retrieve_Hinput())

        dbParam = read_db_config()
        db = pymysql.connect(**dbParam)  # ** is reference to dictionary
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()

        if db != None:
            db.close()
        print ("Entry added!")

rng = CharacterSheet()
rng.GUI()

