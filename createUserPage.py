import tkinter as tk
from tkinter import ttk
import main as ma
import sqlite3
from tkinter import messagebox as msg
import movieList as mi
from cinemaLanguagePack import I18N


iMovieList = mi.iMovieList

class createAccountPage:
    def __init__(self):
        self.win = tk.Tk()
        self.i18n = I18N("en")
        self.win.geometry("800x540+520+220")
        self.win.resizable(False, False)
        self.win.columnconfigure(0, weight=8)
        self.win.columnconfigure(1, weight=8)
        self.win.title(self.i18n.title)
        self.bg = tk.PhotoImage(file="src_createAccount/ToyStory.png")
        self.myLabel = tk.Label(self.win, image=self.bg)
        self.myLabel.place(x=0, y=0, relwidth=1, relheight=1)


        self.comboquestion1 = tk.StringVar()
        self.createWidget()
        self.win.mainloop()

    def radio_handler(self):
        pass

    def go_Back(self):
        self.win.destroy()
        ma.mainPage()

    def createPersonalTable(self, name):
        conn = sqlite3.connect("personalDB.db")
        cur = conn.cursor()
        sqlLine = f"CREATE TABLE {name} (mid INTEGER PRIMARY KEY AUTOINCREMENT, mName TEXT, director TEXT, year INTEGER, rating INTEGER,watched INTEGER);"
        cur.execute(sqlLine)
        conn.commit()
        for x in iMovieList:
            cur.execute(f"INSERT INTO {name} (mName, director, year, rating, watched) VALUES (?, ?, ?, ?, ?)",
                        [x[0], x[1], x[2], x[3], x[4]])

        conn.commit()

        # conn = sqlite3.connect("personalDB.db")
        # cur = conn.cursor()
        # cur.execute(f"SELECT * FROM {name}")
        # movies = cur.fetchall()
        # print(movies)
        conn.close()

    def createNewUser(self, name, Email, pas, saQ, saA, gend):
        conn = sqlite3.connect("coreDB.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO UsersDB(uName, mail, password, saveQ, saveA, gender) VALUES (?, ?, ?, ?, ?, ?)",
                    [name, Email, pas, saQ, saA, gend])
        conn.commit()
        print(f"User {name} created")
        conn.close()
        self.createPersonalTable(name)


    def _from_rgb(self ,rgb):
        return "#%02x%02x%02x" % rgb

    def create_user(self):
        username = self.nameSurname.get()
        mail = self.eMail.get()
        pas = self.password.get()
        pasControl = self.passwordControl.get()
        recoveryQ = self.recoveryQuestion.get()
        recoveryQAnswer = self.recoveryQuestionAnswer.get()
        gender = self.rd_var.get()

        if(username == "" or mail == "" or pas == "" or pasControl == "" or recoveryQ == "" or recoveryQAnswer == "" or gender == ""):
            self.error_Label.configure(text=self.i18n.createUserInfo1)
            return

        for i in username:
            if(i in username == " "):
                self.error_Label.configure(text=self.i18n.createUserInfo2)
                return


        if (pas != pasControl):
            self.error_Label.configure(text=self.i18n.createUserInfo3)
            return

        self.createNewUser(username,mail,pas,recoveryQ,recoveryQAnswer,gender) 
        msg.showinfo("Account Created","You successfully created an account. Now you can login!")



    def createWidget(self):
        self.back_Button = tk.Button(self.win, activebackground=self._from_rgb((82, 166, 203)),
                                       borderwidth=0, width=80, bg=self._from_rgb((82, 166, 203)),
                                       command=self.go_Back)
        self.backImg = tk.PhotoImage(file="src_general/BackIcon (2).png")
        self.back_Button.config(image=self.backImg)
        self.back_Button.grid(column=0, row=0, sticky=tk.W)

        self.createNewAccount_Label = tk.Label(self.win, text=self.i18n.createNewAccount, font=("Comic Sans MS", 20),
                                       bg=self._from_rgb((82, 166, 203)))
        self.createNewAccount_Label.grid(column=0, row=0, pady=(12, 0), columnspan=2)

        self.nameSurname_Label = tk.Label(self.win, text=self.i18n.userName, font=("Comic Sans MS", 12),
                                          bg=self._from_rgb((82, 166, 203)))
        self.nameSurname_Label.grid(column=0, row=1, pady=(20, 0))
        self.nameSurname = tk.StringVar()
        self.nameSurname_entered = ttk.Entry(self.win, width=30, font=("default", 15), textvariable=self.nameSurname)
        self.nameSurname_entered.grid(column=0, row=2, pady=(5, 0))
        self.nameSurname_InfoLabel = tk.Label(self.win, foreground=self._from_rgb((40, 40, 40)),
                                              text=self.i18n.createUserInfo4,
                                              activebackground=self._from_rgb((82, 166, 203)),
                                              borderwidth=0, font=("Times", 10), bg=self._from_rgb((82, 166, 203)))
        self.nameSurname_InfoLabel.grid(column=0, row=3, pady=(0, 50))

        self.eMail_Label = tk.Label(self.win, text=self.i18n.email, font=("Comic Sans MS", 12), bg=self._from_rgb((82, 166, 203)))
        self.eMail_Label.grid(column=1, row=1, pady=(20, 0))
        self.eMail = tk.StringVar()
        self.eMail_entered = ttk.Entry(self.win, width=30, font=("default", 15), textvariable=self.eMail)
        self.eMail_entered.grid(column=1, row=2, pady=(5, 0))
        self.password_Label = tk.Label(self.win, text=self.i18n.password, font=("Comic Sans MS", 12), bg=self._from_rgb((82, 166, 203)))
        self.password_Label.grid(column=0, row=3, pady=(60, 0))
        self.password = tk.StringVar()
        self.password_entered = ttk.Entry(self.win, width=30, font=("default", 15), show="*", textvariable=self.password)
        self.password_entered.grid(column=0, row=4, pady=(5, 0))
        self.password_InfoLabel = tk.Label(self.win, text=self.i18n.createUserInfo5,
                                           foreground=self._from_rgb((40, 40, 40)),
                                           activebackground=self._from_rgb((82, 166, 203)),
                                           borderwidth=0, font=("Times", 10), bg=self._from_rgb((82, 166, 203)))
        self.password_InfoLabel.grid(column=0, row=5, pady=(0, 0))

        self.passwordControl_Label = tk.Label(self.win, text=self.i18n.passwordControl, font=("Comic Sans MS", 12),
                                              bg=self._from_rgb((82, 166, 203)))
        self.passwordControl_Label.grid(column=1, row=3, pady=(60, 0))
        self.passwordControl = tk.StringVar()
        self.passwordControl_entered = ttk.Entry(self.win, width=30, font=("default", 15), show="*",
                                                 textvariable=self.passwordControl)
        self.passwordControl_entered.grid(column=1, row=4, pady=(5, 0))

        self.recoveryQuestion_Label = tk.Label(self.win, text=self.i18n.recoveryQuestion, font=("Comic Sans MS", 12),
                                               bg=self._from_rgb((82, 166, 203)))
        self.recoveryQuestion_Label.grid(column=1, row=5, pady=(20, 0))
        self.recoveryQuestion = tk.StringVar()
        self.recovery_chosen = ttk.Combobox(self.win, width=53, textvariable=self.recoveryQuestion, state="readonly")
        self.recovery_chosen['values'] = (self.i18n.comboquestion1,
                                          self.i18n.comboquestion2,
                                          self.i18n.comboquestion3,
                                          self.i18n.comboquestion4,
                                          self.i18n.comboquestion5,
                                          self.i18n.comboquestion6)
        self.recovery_chosen.grid(column=1, row=6)
        #self.recovery_chosen.current(0)

        self.recoveryQuestionAnswer_Label = tk.Label(self.win, text=self.i18n.recoveryQuestionAnswer, font=("Comic Sans MS", 12),
                                                     bg=self._from_rgb((82, 166, 203)))
        self.recoveryQuestionAnswer_Label.grid(column=1, row=7, pady=(20, 0))
        self.recoveryQuestionAnswer = tk.StringVar()
        self.recoveryQuestionAnswer_entered = ttk.Entry(self.win, width=30, font=("default", 15),
                                                        textvariable=self.recoveryQuestionAnswer)
        self.recoveryQuestionAnswer_entered.grid(column=1, row=8, pady=(0, 90))

        self.rd_var = tk.StringVar()

        self.woman = self.i18n.female
        self.man = self.i18n.male

        self.gender_Label = tk.Label(self.win, text=self.i18n.gender, font=("Comic Sans MS", 12),
                                                     bg=self._from_rgb((82, 166, 203)))
        self.gender_Label.grid(column=0, row=6, pady=(0, 0))

        self.signUp_Button = tk.Button(self.win, command = self.create_user,
                                       activebackground=self._from_rgb((82, 166, 203)),
                                       borderwidth=0, width=250, bg=self._from_rgb((82, 166, 203)))
        self.img1 = tk.PhotoImage(file=self.i18n.img_alien)
        self.signUp_Button.config(image=self.img1)
        self.signUp_Button.grid(column=0, row=8, pady=(30, 0), columnspan=2)

        self.myColor = '#52A6CB'
        self.win.configure(bg=self.myColor)

        self.s = ttk.Style()
        self.s.configure('Wild.TRadiobutton',
                         background=self.myColor,
                         foreground='black')

        self.rb1 = ttk.Radiobutton(self.win, text=self.i18n.male, style='Wild.TRadiobutton', variable=self.rd_var, value=1,
                                   command=self.radio_handler)  # Linking style with the button

        self.rb1.grid(column=0, row=8, sticky=tk.N, pady=(0, 0))

        self.rb2 = ttk.Radiobutton(self.win, text=self.i18n.female, style='Wild.TRadiobutton', variable=self.rd_var, value=2,
                                   command=self.radio_handler)  # Linking style with the button

        self.rb2.grid(column=0, row=7, sticky=tk.N, pady=(10, 0))
        

        self.error_Label = tk.Label(self.win, foreground="red", text="",
                                    font=("Comic Sans MS", 11), bg=self._from_rgb((82, 166, 203)))
        self.error_Label.grid(column=0, row=9, pady=(0, 0), columnspan=2)

        self.win.bind("<Escape>", lambda e: self.win.destroy())
        self.win.bind("<F1>", lambda e: self.reload_gui_text("en"))
        self.win.bind("<F2>", lambda e: self.reload_gui_text("tr"))


    def reload_gui_text(self, language):
        self.i18n = I18N(language)
        self.win.title(self.i18n.title)
        self.createNewAccount_Label.configure(text=self.i18n.createNewAccount)
        self.nameSurname_Label.configure(text=self.i18n.userName)
        self.eMail_Label.configure(text=self.i18n.email)
        self.password_Label.configure(text=self.i18n.password)
        self.passwordControl_Label.configure(text=self.i18n.passwordControl)
        self.recoveryQuestion_Label.configure(text=self.i18n.recoveryQuestion)
        self.recoveryQuestionAnswer_Label.configure(text=self.i18n.recoveryQuestionAnswer)
        self.rb1.configure(text=self.i18n.female)
        self.rb2.configure(text=self.i18n.male)
        self.gender_Label.configure(text=self.i18n.gender)
        self.nameSurname_InfoLabel.configure(text=self.i18n.createUserInfo4)
        self.password_InfoLabel.configure(text=self.i18n.createUserInfo5)
        self.img1.configure(file=self.i18n.img_alien)

        self.recovery_chosen['values'] = (self.i18n.comboquestion1,
                                          self.i18n.comboquestion2,
                                          self.i18n.comboquestion3,
                                          self.i18n.comboquestion4,
                                          self.i18n.comboquestion5,
                                          self.i18n.comboquestion6)










