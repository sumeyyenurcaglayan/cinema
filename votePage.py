import tkinter as tk
from tkinter import ttk
import sqlite3
from cinemaLanguagePack import I18N


class voteFrame:
    def __init__(self, mid, parent, username):
        self.win = tk.Toplevel()
        self.win.grab_set()
        self.UserName = username
        self.win.title("Update Vote")
        self.win.iconbitmap("src_main\cam.ico")
        self.win.geometry("330x100+670+240")
        self.win.resizable(False, False)
        self.movieName = tk.IntVar()
        self.rating = tk.IntVar()
        self.mid = mid
        self.parent = parent
        self.create_widgets()
        self.get_record()


    def update_record(self):
        conn = sqlite3.connect("personalDB.db")
        UName = self.UserName
        myrating = self.rating.get()
        myMid = self.mid
        cur = conn.cursor()

        cur.execute(f"UPDATE {UName} SET rating={myrating} WHERE mid={myMid}")
        conn.commit()
        conn.close()
        self.parent.list_grades()
        self.win.destroy()

    def get_record(self):
        conn = sqlite3.connect("personalDB.db")
        cur = conn.cursor()
        Uname = self.UserName
        cur.execute(f"SELECT mName, director, year, rating, watched FROM {Uname} WHERE mid={self.mid}")
        rec = cur.fetchone()
        conn.close()
        self.fill_text_boxes(rec)

    def fill_text_boxes(self, rec):
        self.rating.set(rec[3])
        self.movieName.set(rec[0])

    def create_widgets(self):
        self.container = tk.LabelFrame(self.win)
        self.container.pack(padx=10, pady=10)

        self.lbl_grade = ttk.Label(self.container, text="Rating")
        self.lbl_grade.grid(column=0, row=2, padx=5, pady=5)

        self.txt_grade = ttk.Entry(self.container, textvariable=self.rating, width=35)
        self.txt_grade.grid(column=1, row=2, padx=5, pady=5)

        self.btn_save = ttk.Button(self.container, text="Update", command=self.update_record)
        self.btn_save.grid(column=0, row=3, columnspan=2, padx=5, pady=(5, 10))

        self.txt_grade.bind("<Return>", lambda e: self.update_record())
        self.win.bind("<Escape>", lambda e: self.win.destroy())

        self.win.bind("<Escape>", lambda e: self.win.destroy())
        self.win.bind("<F1>", lambda e: self.reload_gui_text("en"))
        self.win.bind("<F2>", lambda e: self.reload_gui_text("tr"))

    def reload_gui_text(self, language):
        self.i18n = I18N(language)
        self.win.title(self.i18n.title)