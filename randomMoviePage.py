import tkinter as tk
from tkinter import ttk
import homePage as hp
import sqlite3
import random
from cinemaLanguagePack import I18N

class randMovie:
    def __init__(self, username):
        self.win = tk.Tk()

        self.UserName = username
        self.i18n = I18N("en")

        self.win.title(self.i18n.title)
        self.win.geometry("800x540+520+220")
        self.win.resizable(False, False)
        self.win.iconbitmap("src_main\cam.ico")

        self.bg = tk.PhotoImage(file="src_randMovie/Hog_BG.png")
        self.myLabel = tk.Label(self.win, image=self.bg)
        self.myLabel.place(x=0, y=0, relwidth=1, relheight=1)

        self.createWidgets()
        self.getRandomName()
        self.win.mainloop()

    def getRandomName(self):
        UName = self.UserName
        conn = sqlite3.connect("personalDB.db")
        cur = conn.cursor()
        cur.execute(f"SELECT mName FROM {UName}")
        rec = cur.fetchall()
        randNnum = random.randint(0,100)
        self.recName.configure(text=rec[randNnum][0])
        conn.commit()
        conn.close()


    def _from_rgb(self, rgb):
        return "#%02x%02x%02x" % rgb

    def go_Back(self):
        self.win.destroy()
        hp.homePage(self.UserName)

    def createWidgets(self):
        self.back_Button = tk.Button(self.win, bg="black",
                                     borderwidth=0, width=40,
                                     command=self.go_Back)
        self.backImg = tk.PhotoImage(file="src_general/backArrowWhite.png")
        self.back_Button.config(image=self.backImg)
        self.back_Button.pack(side=tk.TOP, anchor=tk.NW)


        self.recTitle = tk.Label(self.win, text=self.i18n.randomRecommendation, font=("Comic Sans MS", 18),
                    bg=self._from_rgb((170, 211, 255)))
        self.recTitle.pack(pady=(100,0))

        self.recName = tk.Label(self.win, text="Random Recommendation", font=("Comic Sans MS", 18),
                                  bg=self._from_rgb((170, 130, 140)))
        self.recName.pack(pady=(60, 0))

        self.win.bind("<Escape>", lambda e: self.win.destroy())
        self.win.bind("<F1>", lambda e: self.reload_gui_text("en"))
        self.win.bind("<F2>", lambda e: self.reload_gui_text("tr"))

    def reload_gui_text(self, language):
        self.i18n = I18N(language)
        self.win.title(self.i18n.title)
        self.recTitle.configure(text=self.i18n.randomRecommendation)


