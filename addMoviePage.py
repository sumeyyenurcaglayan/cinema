import tkinter as tk
from tkinter import ttk
import homePage as hp
import sqlite3
from tkinter import messagebox as msg
from cinemaLanguagePack import I18N

class addMoviePage:
    def __init__(self, Username):
        self.win = tk.Tk()
        self.win.geometry("800x540+520+220")
        self.win.resizable(False, False)
        self.i18n = I18N("en")
        self.UserName = Username
        self.win.title(self.i18n.title)
        self.win.columnconfigure(0, weight=8)
        self.win.columnconfigure(1, weight=2)
        self.win.columnconfigure(2, weight=8)
        self.win.columnconfigure(3, weight=2)

        self.bg = tk.PhotoImage(file="src_addMovie/BG_space.png")
        self.myLabel = tk.Label(self.win, image=self.bg)
        self.myLabel.place(x=0, y=0, relwidth=1, relheight=1)

        self.createWidget()
        self.win.mainloop()

    def _from_rgb(self, rgb):
        return "#%02x%02x%02x" % rgb

    def go_Back(self):
        self.win.destroy()
        hp.homePage(self.UserName)

    def addNewMovie(self):
        name = self.UserName
        movieName = self.movieName.get()
        director = self.Director.get()
        releaseYear = self.year.get()
        score = self.myRating.get()
        watched = 1

        if (movieName == "" or director == "" or releaseYear == "" or score == ""):
            msg.showerror("Empty Form!", "All form elements should be filled.")
        else:
            conn = sqlite3.connect("personalDB.db")
            cur = conn.cursor()
            cur.execute(f"INSERT INTO {name} (mName, director, year, rating, watched) VALUES (?, ?, ?, ?, ?)",
                        [movieName, director, releaseYear, score, watched])
            conn.commit()
            conn.close()
            msg.showinfo("NEW MOVIE", "New Movie Added!")

    def createWidget(self):
        self.back_Button = tk.Button(self.win, activebackground=self._from_rgb((0, 0, 0)),
                                     borderwidth=0, width=80, bg=self._from_rgb((0, 0, 0)),
                                     command=self.go_Back)
        self.backImg = tk.PhotoImage(file="src_general/backArrowWhite.png")
        self.back_Button.config(image=self.backImg)
        self.back_Button.grid(column=0, row=0, sticky=tk.W)

        self.addNewMovie_Label = tk.Label(self.win, text=self.i18n.addNewMovie, font=("Comic Sans MS", 25),foreground="White",
                                       bg=self._from_rgb((0, 0, 0)))
        self.addNewMovie_Label.grid(column=0, row=0, pady=(12, 0), columnspan=4)


        self.movieName_Label = tk.Label(self.win, text=self.i18n.movieName, font=("Comic Sans MS", 12),foreground="White",
                                          bg=self._from_rgb((0, 0, 0)))
        self.movieName_Label.grid(column=0, row=1)

        self.movieName = tk.StringVar()
        self.movieName_entered = ttk.Entry(self.win, width=20, font=("default", 15), textvariable=self.movieName)
        self.movieName_entered.grid(column=0, row=1,pady=(100,0))

        self.Director_Label = tk.Label(self.win, text=self.i18n.director, font=("Comic Sans MS", 12),foreground="White",
                                    bg=self._from_rgb((0, 0, 0)))
        self.Director_Label.grid(column=2, row=1)
        self.Director = tk.StringVar()
        self.Director_entered = ttk.Entry(self.win, width=20, font=("default", 15), textvariable=self.Director)
        self.Director_entered.grid(column=2, row=1, pady=(100,0))

        self.year_Label = tk.Label(self.win, text=self.i18n.year, font=("Comic Sans MS", 12),foreground="White",
                                       bg=self._from_rgb((0, 0, 0)))
        self.year_Label.grid(column=0, row=2)
        self.year = tk.StringVar()
        self.year_entered = ttk.Entry(self.win, width=20, font=("default", 15),
                                          textvariable=self.year)
        self.year_entered.grid(column=0, row=2,pady=(100,0))


        self.myRating_Label = tk.Label(self.win, text=self.i18n.myRating, font=("Comic Sans MS", 12),foreground="White",
                                              bg=self._from_rgb((0, 0, 0)))
        self.myRating_Label.grid(column=2, row=2)
        self.myRating = tk.IntVar()
        self.myRating_entered = ttk.Entry(self.win, width=20, font=("default", 15),
                                                 textvariable=self.myRating)
        self.myRating_entered.grid(column=2, row=2,pady=(100,0))



        self.pic_Label = tk.Label(self.win,
                                            activebackground=self._from_rgb((0, 0, 0)),
                                            borderwidth=0, bg=self._from_rgb((0, 0, 0)))
        self.pic_Label_img = tk.PhotoImage(file="src_addMovie/Po3.png")
        self.pic_Label.config(image=self.pic_Label_img)
        self.pic_Label.grid(column=1, row=1)

        self.pic1_Label = tk.Label(self.win,
                                  activebackground=self._from_rgb((0, 0, 0)),
                                  borderwidth=0, bg=self._from_rgb((0, 0, 0)))
        self.pic1_Label_img = tk.PhotoImage(file="src_addMovie/Clone.png")
        self.pic1_Label.config(image=self.pic1_Label_img)
        self.pic1_Label.grid(column=3, row=1)

        self.pic2_Label = tk.Label(self.win,
                                   activebackground=self._from_rgb((0, 0, 0)),
                                   borderwidth=0, bg=self._from_rgb((0, 0, 0)))
        self.pic2_Label_img = tk.PhotoImage(file="src_addMovie/Darth.png")
        self.pic2_Label.config(image=self.pic2_Label_img)
        self.pic2_Label.grid(column=1, row=2)

        self.pic3_Label = tk.Label(self.win,
                                   activebackground=self._from_rgb((0, 0, 0)),
                                   borderwidth=0, bg=self._from_rgb((0, 0, 0)))
        self.pic3_Label_img = tk.PhotoImage(file="src_addMovie/Kenobi.png")
        self.pic3_Label.config(image=self.pic3_Label_img)
        self.pic3_Label.grid(column=3, row=2)

        login_Button = tk.Button(self.win,  command=self.addNewMovie,
                                 activebackground=self._from_rgb((0, 0, 0)),
                                 borderwidth=0, width=160, bg=self._from_rgb((0, 0, 0)))
        self.img = tk.PhotoImage(file=self.i18n.img_addMov)
        login_Button.config(image=self.img)
        login_Button.grid(column=0, row=3, columnspan=4, pady=(50,0))

        self.win.bind("<Escape>", lambda e: self.win.destroy())
        self.win.bind("<F1>", lambda e: self.reload_gui_text("en"))
        self.win.bind("<F2>", lambda e: self.reload_gui_text("tr"))

    def reload_gui_text(self, language):
        self.i18n = I18N(language)
        self.win.title(self.i18n.title)
        self.addNewMovie_Label.configure(text=self.i18n.addNewMovie)
        self.movieName_Label.configure(text=self.i18n.movieName)
        self.Director_Label.configure(text=self.i18n.director)
        self.year_Label.configure(text=self.i18n.year)
        self.myRating_Label.configure(text=self.i18n.myRating)
        self.img.configure(file=self.i18n.img_addMov)




