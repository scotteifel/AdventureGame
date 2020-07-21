import sqlite3, os


def create_table():
        #Create the database and map it to the project folder
        path = os.path.abspath("AdventureGame")
        path = path[:-13]
        conn = sqlite3.connect("main.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS character (name TEXT,
                        thirsty INTEGER, hungry INTEGER, tired INTEGER)''')
        conn.commit()
        cur.close()
        conn.close()


def add_char(name):

        conn = sqlite3.connect("main.db")
        cur = conn.cursor()
        cur.execute('''INSERT INTO character VALUES (?,?,?,?)''', (name,
            1,1,0))
        conn.commit()
        cur.close()
        conn.close()


def print_char():

        conn = sqlite3.connect("main.db")
        cur = conn.cursor()
        cur.execute('''SELECT * FROM character''')
        print(cur.fetchall())
        cur.close()
        conn.close()


def edit_char_attr(attr):
        print(type(attr))

        conn = sqlite3.connect("main.db")
        cur = conn.cursor()

        if attr == "tired":
            cur.execute('''UPDATE character SET tired = 1''')

        conn.commit()
        cur.close()
