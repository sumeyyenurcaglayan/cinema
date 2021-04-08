import tkinter as tk
from tkinter import ttk
import addMoviePage as amp
import sqlite3
import random
from cinemaLanguagePack import I18N
import randomMoviePage as ra
import votePage
import Top100Page as t100
from tkinter import messagebox as msg


class homePage:
    def __init__(self,UserName):
        self.win = tk.Tk()
        self.i18n = I18N("en")
        self.Username = UserName
        self.watchedList = []
        self.notWatchedList = []
        self.win.title(self.i18n.title)
        self.win.geometry("800x540+520+220")
        self.win.resizable(False, False)
        self.bg = tk.PhotoImage(file="src_HomePage/Lotrbackground.png")
        self.myLabel = tk.Label(self.win, image=self.bg)
        self.myLabel.place(x=0, y=0, relwidth=1, relheight=1)
        self.win.columnconfigure(0, weight=1)
        self.win.columnconfigure(1, weight=1)
        self.win.columnconfigure(2, weight=1)
        self.getPersonalMovieList()
        self.createWidgets()
        self.list_grades()
        self.win.mainloop()


    def _from_rgb(self,rgb):
        return "#%02x%02x%02x" % rgb

    def addMovie(self):
        self.win.destroy()
        amp.addMoviePage(self.Username)

    def on_double_click(self, e):
        item = self.tv.selection()[0]
        UName = self.Username
        votePage.voteFrame(mid=item, parent=self, username=UName)

    def goRandPage(self):
        self.win.destroy()
        ra.randMovie(self.Username)

    def getPersonalMovieList(self):
        conn = sqlite3.connect("personalDB.db")
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {self.Username}")
        movies = cur.fetchall()

        for i in movies:
            if(i[5] == 0):
                self.notWatchedList.append(i)
            else:
                self.watchedList.append(i)

    def voteFunction1(self):
        UName = self.Username
        voteVal = self.vote1Value.get()
        voteTarget = self.moviesToReccomand[0][0]
        conn = sqlite3.connect("personalDB.db")
        cur = conn.cursor()
        cur.execute(f"UPDATE {UName} SET rating={voteVal} WHERE mid={voteTarget}")
        conn.commit()
        conn.close()
        self.list_grades()

    def voteFunction2(self):
        UName = self.Username
        voteVal = self.vote2Value.get()
        voteTarget = self.moviesToReccomand[1][0]
        conn = sqlite3.connect("personalDB.db")
        cur = conn.cursor()
        cur.execute(f"UPDATE {UName} SET rating={voteVal} WHERE mid={voteTarget}")
        conn.commit()
        conn.close()
        self.list_grades()

    def voteFunction3(self):
        UName = self.Username
        voteVal = self.vote3Value.get()
        voteTarget = self.moviesToReccomand[2][0]
        conn = sqlite3.connect("personalDB.db")
        cur = conn.cursor()
        cur.execute(f"UPDATE {UName} SET rating={voteVal} WHERE mid={voteTarget}")
        conn.commit()
        conn.close()
        self.list_grades()

    def list_grades(self):
        conn = sqlite3.connect("personalDB.db")
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {self.Username} WHERE rating !=0")

        for i in self.tv.get_children():
            self.tv.delete(i)

        grades = cur.fetchall()
        for g in grades:
            self.tv.insert(parent="", index="end", iid=g[0], values=(g[0], g[1], g[2], g[4]))
        conn.close()

    def go_top100(self):
        self.win.destroy()
        t100.top100page(self.Username)

    def searchMovieButton(self):
        UName = self.Username
        targetMovieName = self.searchMovie.get()
        conn = sqlite3.connect("personalDB.db")
        cur = conn.cursor()
        cur.execute(f"SELECT mid, mName, director, year, rating, watched FROM {UName}")
        rec = cur.fetchall()
        wantedmid = 0
        found = 0
        for i in rec:
            if(i[1] == targetMovieName):
                found = 1
                wantedmid = i[0]

        if(found == 1):
            item = wantedmid
            UName = self.Username
            votePage.voteFrame(mid=item, parent=self, username=UName)
        else:
            msg.showerror("Error!","Searched movie not found!")



    def createWidgets(self):
        self.titleLabel = tk.Label(self.win, text=self.i18n.homepage, font=("Comic Sans MS", 16),
                                         foreground="white", bg=self._from_rgb((21, 21, 21)))
        self.titleLabel.grid(column=0, row=0, pady=(12, 0), columnspan=3)


        self.top100_Button = tk.Button(self.win, text="top 100",command=self.go_top100,
                                       activebackground=self._from_rgb((21, 21, 21)),
                                       borderwidth=0, width=250, bg=self._from_rgb((21, 21, 21)))
        self.top100_img = tk.PhotoImage(file="src_HomePage/top100.png")
        self.top100_Button.config(image=self.top100_img)
        self.top100_Button.grid(column=1, row=1, pady=(30, 0))
        self.addMovie_Button = tk.Button(self.win, text="add movie", command=self.addMovie,
                                         activebackground=self._from_rgb((21, 21, 21)),
                                         borderwidth=0, width=250, bg=self._from_rgb((21, 21, 21)))
        self.addMovie_img = tk.PhotoImage(file=self.i18n.img_addMovie)
        self.addMovie_Button.config(image=self.addMovie_img)
        self.addMovie_Button.grid(column=2, row=1, pady=(30, 0))




        self.randomMovie_Button = tk.Button(self.win, text="Random Movie",command=self.goRandPage,
                                            activebackground=self._from_rgb((21, 21, 21)),
                                            borderwidth=0, width=250, bg=self._from_rgb((21, 21, 21)))
        self.img_randomMovie = tk.PhotoImage(file=self.i18n.img_randomMovie)
        self.randomMovie_Button.config(image=self.img_randomMovie)
        self.randomMovie_Button.grid(column=0, row=1, pady=(30, 0))

        self.searchMovie = tk.StringVar()
        self.searchMovie_entered = ttk.Entry(self.win, width=40, font=("default", 15), textvariable=self.searchMovie)
        self.searchMovie_entered.grid(column=0, row=2, columnspan=3)

        self.searchMovie_Label = tk.Label(self.win, text=self.i18n.searchMovie, font=("Comic Sans MS", 12),
                                          foreground="white",
                                          bg=self._from_rgb((21, 21, 21)))
        self.searchMovie_Label.grid(column=0, row=2, pady=(5, 0), padx=(10, 0), sticky=tk.NW)

        self.search_button = tk.Button(self.win, text=self.i18n.search,bg=self._from_rgb((210, 168, 60)),borderwidth=0)
        self.search_button.grid(column=2, row=2)

        self.scoreMovie_Label = tk.Label(self.win, text=self.i18n.myMovieScores, font=("Comic Sans MS", 12),
                                         foreground="white", bg=self._from_rgb((21, 21, 21)))
        self.scoreMovie_Label.grid(column=0, row=3, pady=(15, 0), padx=(10, 0), sticky=tk.NW, columnspan=1)

        self.didYouWatchTheseMovies_Label = tk.Label(self.win, text=self.i18n.didYouWatchTheseMovies, font=("Comic Sans MS", 12),
                                         foreground="white", bg=self._from_rgb((21, 21, 21)))
        self.didYouWatchTheseMovies_Label.grid(column=2, row=3, pady=(15, 0), padx=(10, 0), sticky=tk.NW, columnspan=1)

        self.moviesToReccomand = []
        for i in range(3):
            self.moviesToReccomand.append(self.notWatchedList[random.randint(1,len(self.notWatchedList))])



        self.recomand1 = tk.Label(self.win,text=self.moviesToReccomand[0][1],font=("Times", 12)
                                  ,bg=self._from_rgb((21, 21, 21)),foreground="white")
        self.recomand1.grid(column=2, row=4, pady=(22, 0))

        self.recVove1 = tk.Button(self.win, text=self.i18n.vote, width=8, command=self.voteFunction1,
                                  bg=self._from_rgb((210, 168, 60)),borderwidth=0)
        self.recVove1.grid(column=2, row=5, pady=(6, 0))

        self.vote1Value = tk.IntVar()
        self.vote1Entry = ttk.Entry(self.win, width=3, font=("default", 12), textvariable=self.vote1Value)
        self.vote1Entry.grid(column=2, row=5, pady=(6, 0), padx=(0, 100))

        self.recomand2 = tk.Label(self.win, text=self.moviesToReccomand[1][1], font=("Times", 12)
                                  ,bg=self._from_rgb((21, 21, 21)), foreground="white")
        self.recomand2.grid(column=2, row=6, pady=(22, 0))

        self.recVove2 = tk.Button(self.win, text=self.i18n.vote, width=8, command=self.voteFunction2,
                                  bg=self._from_rgb((210, 168, 60)),borderwidth=0,)
        self.recVove2.grid(column=2, row=7, pady=(6, 0))

        self.vote2Value = tk.IntVar()
        self.vote2Entry = ttk.Entry(self.win, width=3, font=("default", 12), textvariable=self.vote2Value)
        self.vote2Entry.grid(column=2, row=7, pady=(6, 0), padx=(0, 100))


        self.recomand3 = tk.Label(self.win, text=self.moviesToReccomand[2][1], font=("Times", 12)
                                  ,bg=self._from_rgb((21, 21, 21)), foreground="white")
        self.recomand3.grid(column=2, row=8, pady=(22, 0))

        self.recVove3 = tk.Button(self.win, text=self.i18n.vote, width=8, command=self.voteFunction3,
                                  bg=self._from_rgb((210, 168, 60)),borderwidth=0)
        self.recVove3.grid(column=2, row=9, pady=(6, 0))

        self.vote3Value = tk.IntVar()
        self.vote3Entry = ttk.Entry(self.win, width=3, font=("default", 12), textvariable=self.vote3Value)
        self.vote3Entry.grid(column=2, row=9, pady=(6, 0), padx=(0, 100))

        self.tv_frame = tk.Frame(self.win)
        self.tv_frame.grid(column=0, row=4, columnspan=2, rowspan=6, pady=(0,0))

        self.scr_bar = ttk.Scrollbar(self.tv_frame)
        self.scr_bar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tv = ttk.Treeview(self.tv_frame, yscrollcommand=self.scr_bar.set)
        self.tv.pack()

        self.scr_bar.configure(command=self.tv.yview)

        self.tv["columns"] = ("mid","mName", "director", "rating")

        self.tv.column("#0", width=0, stretch=tk.NO)
        self.tv.column("mid", anchor=tk.CENTER, width=50)
        self.tv.column("mName", anchor=tk.W, width=180)
        self.tv.column("director", anchor=tk.W, width=140)
        self.tv.column("rating", anchor=tk.CENTER, width=70)

        self.tv.heading("#0", text="")
        self.tv.heading("mid", text="ID", anchor=tk.CENTER)
        self.tv.heading("mName", text=self.i18n.movie, anchor=tk.W)
        self.tv.heading("director", text=self.i18n.director, anchor=tk.W)
        self.tv.heading("rating", text=self.i18n.myRating, anchor=tk.CENTER)

        self.tv.bind("<Double-1>", self.on_double_click)

        self.win.bind("<Escape>", lambda e: self.win.destroy())
        self.win.bind("<F1>", lambda e: self.reload_gui_text("en"))
        self.win.bind("<F2>", lambda e: self.reload_gui_text("tr"))

    def reload_gui_text(self, language):
        self.i18n = I18N(language)
        self.win.title(self.i18n.title)
        self.titleLabel.configure(text=self.i18n.homepage)
        self.recVove1.configure(text=self.i18n.vote)
        self.recVove2.configure(text=self.i18n.vote)
        self.recVove3.configure(text=self.i18n.vote)
        self.search_button.configure(text=self.i18n.search)
        self.searchMovie_Label.configure(text=self.i18n.searchMovie)
        self.didYouWatchTheseMovies_Label.configure(text=self.i18n.didYouWatchTheseMovies)
        self.scoreMovie_Label.configure(text=self.i18n.myMovieScores)
        self.addMovie_img.configure(file=self.i18n.img_addMovie)
        self.img_randomMovie.configure(file=self.i18n.img_randomMovie)
        self.tv.heading('mName', text=self.i18n.movie)
        self.tv.heading('director', text=self.i18n.director)
        self.tv.heading('rating', text=self.i18n.myRating)





