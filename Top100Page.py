import tkinter as tk
from tkinter import ttk
import sqlite3
import homePage as hp
import votePage
from cinemaLanguagePack import I18N


class top100page:
    def __init__(self, Username):
        self.win = tk.Tk()

        self.UserName = Username
        self.i18n = I18N("en")
        self.win.title(self.i18n.title)
        self.win.geometry("800x540+520+220")
        self.win.resizable(False, False)
        self.win.iconbitmap("src_main\cam.ico")

        self.createWidgets()
        self.list_grades()
        self.win.mainloop()

    def _from_rgb(self, rgb):
        return "#%02x%02x%02x" % rgb

    def list_grades(self):
        conn = sqlite3.connect("personalDB.db")
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {self.UserName}")

        for i in self.tv.get_children():
            self.tv.delete(i)

        grades = cur.fetchall()
        for g in grades:
            self.tv.insert(parent="", index="end", iid=g[0], values=(g[0], g[1], g[2], g[4]))
        conn.close()


    def go_Back(self):
        self.win.destroy()
        hp.homePage(self.UserName)

    def on_double_click(self, e):
        item = self.tv.selection()[0]
        UName = self.UserName
        votePage.voteFrame(mid=item, parent=self, username=UName)


    def createWidgets(self):
        self.back_Button = tk.Button(self.win,
                                     borderwidth=0, width=40,
                                     command=self.go_Back)
        self.backImg = tk.PhotoImage(file="src_general/BackIcon (2).png")
        self.back_Button.config(image=self.backImg)
        self.back_Button.pack(side=tk.TOP, anchor=tk.NW)

        self.container = tk.Frame(self.win)
        self.container.pack(fill=tk.BOTH, expand=True)

        self.tv_frame = tk.Frame(self.container)
        self.tv_frame.pack()

        self.scr_bar = ttk.Scrollbar(self.tv_frame)
        self.scr_bar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.tv = ttk.Treeview(self.tv_frame, height=22,
                               yscrollcommand=self.scr_bar.set)

        self.tv.bind("<Double-1>", self.on_double_click)
        self.tv.pack()

        self.scr_bar.configure(command=self.tv.yview)

        self.tv["columns"] = ("mid","mName", "director", "rating")

        self.tv.column("#0", width=0, stretch=tk.NO)
        self.tv.column("mid", anchor=tk.CENTER, width=90)
        self.tv.column("mName", anchor=tk.W, width=360)
        self.tv.column("director", anchor=tk.W, width=220)
        self.tv.column("rating", anchor=tk.CENTER, width=100)

        self.tv.heading("#0", text="")
        self.tv.heading("mid", text="ID", anchor=tk.CENTER)
        self.tv.heading("mName", text=self.i18n.movie, anchor=tk.W)
        self.tv.heading("director", text=self.i18n.director, anchor=tk.W)
        self.tv.heading("rating", text=self.i18n.myRating, anchor=tk.CENTER)

        self.titleDouble_Label = tk.Label(self.win, text=self.i18n.titleDouble, font=("Comic Sans MS", 14),
                                   )
        self.titleDouble_Label.pack()

        self.win.bind("<Escape>", lambda e: self.win.destroy())
        self.win.bind("<F1>", lambda e: self.reload_gui_text("en"))
        self.win.bind("<F2>", lambda e: self.reload_gui_text("tr"))

    def reload_gui_text(self, language):
        self.i18n = I18N(language)
        self.win.title(self.i18n.title)
        self.titleDouble_Label.configure(text=self.i18n.titleDouble)
        self.tv.heading('mName', text=self.i18n.movie)
        self.tv.heading('director', text=self.i18n.director)
        self.tv.heading('rating', text=self.i18n.myRating)


