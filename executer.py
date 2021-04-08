import sqlite3
import main as ma
import movieList as ml
from cinemaLanguagePack import I18N


iMovieList = ml.iMovieList

def create_user_table():
    try:
        conn = sqlite3.connect("coreDB.db")
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE UsersDB (
            uid INTEGER PRIMARY KEY AUTOINCREMENT,
            uName TEXT,
            mail TEXT,
            password TEXT,
            saveQ TEXT,
            saveA TEXT,
            gender TEXT
            );
            """)
        conn.commit()
        conn.close()
        print("User table is successfully created")
    except:
        print("User table is already exist")

def fill_movie_table():
    try:
        conn = sqlite3.connect("coreDB.db")
        cur = conn.cursor()
        for x in iMovieList:
            cur.execute(
                "INSERT INTO baseMovieDB(mName, director, year, rating, watched) VALUES (?, ?, ?, ?, ?)",
                [x[0], x[1], x[2], x[3], x[4]])

            conn.commit()
            conn.close()
            print("Movie table is successfully filled")
    except:
        print("Error occured at fill_movie_table() function")

def create_movie_table():
    try:
        conn = sqlite3.connect("coreDB.db")
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE baseMovieDB (
            mid INTEGER PRIMARY KEY AUTOINCREMENT,
            mName TEXT,
            director TEXT,
            year INTEGER,
            rating INTEGER,
            watched INTEGER
            );
            """)
        print("-------------------")
        for x in iMovieList:
            cur.execute("INSERT INTO baseMovieDB(mName, director, year, rating, watched) VALUES (?, ?, ?, ?, ?)",
                        [x[0], x[1], x[2], x[3], x[4]])

        conn.commit()
        conn.close()
        print("Movie table is successfully created")
    except:
        print("Movie table is already exist")

create_user_table()
create_movie_table()

ma.mainPage()