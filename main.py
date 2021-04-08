import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import createUserPage as cu
import homePage as hp
from tkinter import messagebox as msg
import sqlite3
from cinemaLanguagePack import I18N


class mainPage:
    def __init__(self):
        self.win = tk.Tk()

        self.i18n = I18N("en")

        self.win.title(self.i18n.title)
        self.win.geometry("800x540+520+220")
        self.win.resizable(False, False)
        self.win.iconbitmap("src_main\cam.ico")
        self.win.columnconfigure(0, weight=2)
        self.win.columnconfigure(1, weight=4)
        self.win.columnconfigure(2, weight=2)

        self.mailValue = tk.StringVar()
        self.passValue = tk.StringVar()
        self.emailText = tk.StringVar()
        self.passwordText = tk.StringVar()
        self.login = tk.StringVar()

        self.bg = tk.PhotoImage(file="src_main/main_bg.png")

        self.myLabel = tk.Label(self.win, image=self.bg)
        self.myLabel.place(x=0, y=0, relwidth=1, relheight=1)

        self.createWidgets()
        self.win.mainloop()


    def _from_rgb(self, rgb):
        return "#%02x%02x%02x" % rgb

    def login_Account(self):
        self.login_User()

    def create_Account(self):
        self.win.destroy()
        cu.createAccountPage()

    def login_User(self):
        conn = sqlite3.connect("coreDB.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM UsersDB")
        users = cur.fetchall()
        conn.close()

        mail = self.mailValue.get()
        password = self.passValue.get()

        for i in users:
            if(i[2] == mail):
                if(i[3] == password):
                    self.win.destroy()
                    hp.homePage(i[1])
                else:
                    msg.showerror(self.i18n.mainInfo1, self.i18n.mainInfo2)
            else:
                msg.showerror(self.i18n.mainInfo3,self.i18n.mainInfo4)


    def login_Account(self):
        self.login_User()


    def createWidgets(self):
        self.logo = Image.open(self.i18n.imgMyMovieLogo)
        self.resized = self.logo.resize((132, 124), Image.ANTIALIAS)
        self.resized_Logo = ImageTk.PhotoImage(self.resized)
        self.img_Label = tk.Label(self.win, image=self.resized_Logo, bg=self._from_rgb((170, 211, 255)))
        self.img_Label.grid(column=1, row=0, pady=(18, 0))

        self.emailText_Label = tk.Label(self.win, text=self.i18n.emailText, font=("Comic Sans MS", 12),
                    bg=self._from_rgb((170, 211, 255)))
        self.emailText_Label.grid(column=1, row=1, pady=(18, 0))

        self.temp_Entry = ttk.Entry(self.win, width=32, textvariable=self.mailValue, font=("Comic Sans MS", 10))
        self.temp_Entry.grid(column=1, row=2, pady=(6, 0))

        self.passwordText_Label = tk.Label(self.win, text=self.i18n.passwordText, font=("Comic Sans MS", 12), bg=self._from_rgb((170, 211, 255)))
        self.passwordText_Label.grid(column=1, row=3, pady=(18, 0))

        self.temp_Entry = ttk.Entry(self.win, width=32, textvariable=self.passValue, font=("Comic Sans MS", 10), show="*")
        self.temp_Entry.grid(column=1, row=4, pady=(6, 0))


        self.login_Button = tk.Button(self.win, text="Login", command=self.login_Account,
                         activebackground=self._from_rgb((170, 211, 255)),
                         borderwidth=0, width=120, bg=self._from_rgb((170, 211, 255)))
        self.img = tk.PhotoImage(file=self.i18n.imgLogin)
        self.login_Button.config(image=self.img)
        self.login_Button.grid(column=1, row=5, pady=(30, 0))

        self.loginInfoText_Label = tk.Button(self.win, text=self.i18n.loginInfoText, command=self.create_Account,
                           activebackground=self._from_rgb((170, 211, 255)),
                           borderwidth=0, font=("Times", 10), bg=self._from_rgb((170, 211, 255)))
        self.loginInfoText_Label.grid(column=1, row=6, pady=(6, 0))

        self.win.bind("<Escape>", lambda e: self.win.destroy())
        self.win.bind("<F1>", lambda e: self.reload_gui_text("en"))
        self.win.bind("<F2>", lambda e: self.reload_gui_text("tr"))

    def reload_gui_text(self, language):

        self.i18n = I18N(language)
        self.win.title(self.i18n.title)
        self.emailText_Label.configure(text=self.i18n.emailText)
        self.passwordText_Label.configure(text=self.i18n.passwordText)
        self.loginInfoText_Label.configure(text=self.i18n.loginInfoText)

        self.img.configure(file= self.i18n.imgLogin)




