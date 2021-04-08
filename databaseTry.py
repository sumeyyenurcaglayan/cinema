import sqlite3

iMovieList = [('The Shawshank Redemption', 'Frank Darabont', 1994, 0, 0),
              ('The Godfather', 'Francis Ford Coppola', 1972, 0, 0),
              ('The Dark Knight', 'Christopher Nolan', 2008, 0, 0),
              ('The Godfather: Part II', 'Francis Ford Coppola', 1974, 0, 0)
             ]


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

        for x in iMovieList:
            cur.execute("INSERT INTO baseMovieDB(mName, director, year, rating, watched) VALUES (?, ?, ?, ?, ?)", [x[0], x[1], x[2], x[3], x[4]])

        conn.commit()
        conn.close()
        print("Movie table is successfully created")
    except:
        print("Movie table is already exist")


def fill_movie_table():
    try:
        conn = sqlite3.connect("coreDB.db")
        cur = conn.cursor()
        for x in iMovieList:
            cur.execute("INSERT INTO baseMovieDB(mName, director, year, rating, watched) VALUES (?, ?, ?, ?, ?)", [x[0], x[1], x[2], x[3], x[4]])

        conn.commit()
        conn.close()
        print("Movie table is successfully filled")
    except:
        print("Error occured at fill_movie_table() function")



def createPersonalTable(name):
    conn = sqlite3.connect("personalDB.db")
    cur = conn.cursor()
    sqlLine = f"CREATE TABLE {name} (mid INTEGER PRIMARY KEY AUTOINCREMENT, mName TEXT, director TEXT, year INTEGER, rating INTEGER,watched INTEGER);"
    cur.execute(sqlLine)
    conn.commit()
    for x in iMovieList:
        cur.execute(f"INSERT INTO {name} (mName, director, year, rating, watched) VALUES (?, ?, ?, ?, ?)",
                    [x[0], x[1], x[2], x[3], x[4]])

    print(f"{name} tablosu oluşturuldu ve dolduruldu")
    conn.commit()
    conn.close()

def createNewUser(name, Email, pas, saQ, saA, gend):
    conn = sqlite3.connect("coreDB.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO UsersDB(uName, mail, password, saveQ, saveA, gender) VALUES (?, ?, ?, ?, ?, ?)", [name, Email, pas, saQ, saA, gend])
    conn.commit()
    print(f"User {name} created")
    conn.close()
    createPersonalTable(name)


def getListofUsers():
    conn = sqlite3.connect("coreDB.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM UsersDB")
    users = cur.fetchall()
    conn.close()
    return users

def getListofMovies():
    conn = sqlite3.connect("coreDB.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM baseMovieDB")
    movies = cur.fetchall()
    conn.close()
    return movies

def getListofPersonalMovies(name):
    conn = sqlite3.connect("personalDB.db")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {name}")
    movies = cur.fetchall()
    conn.close()
    return movies

#create_user_table()
#create_movie_table()

#createNewUser("MustafaFuttu", "mfuttum@gmail.com", "mypass123", "En sevdiğim yemek", "mantar çorbası", "male")
#createNewUser("Sümeyye Nur Çağlayan", "sumo@gmail.com", "herpassword789", "En sevdiğim kitap", "İki şehrin hikayesi", "female")
#createNewUser("AliSu", "asu@gmail.com", "alipass", "ilk evcil hayavanının adı", "haydut", "male")
#createNewUser("KemalSu", "kemal@gmail.com", "alipass", "ilk evcil hayavanının adı", "haydut", "male")
#createNewUser("Melikeee", "mel@gmail.com", "melo123", "En sevdiğim renk", "mor", "female")


#print(getListofUsers())

#print(getListofMovies())

#print(getListofPersonalMovies("MustafaFuttu"))