import sqlite3, os


def create_db_table():
        #Create the database and map it to the project folder
        path = os.path.abspath("AdventureGame")
        path = path[:-13]
        conn = sqlite3.connect("main.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS character (name TEXT,
                        thirsty INTEGER, hungry INTEGER, tired INTEGER,
                        room_tracker INTEGER)''')
        conn.commit()
        cur.close()
        conn.close()


def add_char(name):

        conn = sqlite3.connect("main.db")
        cur = conn.cursor()
        cur.execute('''INSERT INTO character VALUES (?,?,?,?,?)''', (name,
            1,1,0,0))
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


def edit_char_attr(**kwargs):
        _ = []
        for item in kwargs:
            print(item)
            _.append(item)
        print(_)

        conn = sqlite3.connect("main.db")
        cur = conn.cursor()
        cur.execute('''UPDATE character SET room_tracker = {x}'''
                        .format(x=room))
        conn.commit()

        if tired == True:
            cur.execute('''UPDATE character SET tired = 1''')

        conn.commit()
        cur.close()

def get_current_room():

        conn = sqlite3.connect("main.db")
        cur = conn.cursor()
        cur.execute('''SELECT room_tracker FROM character''')
        room = cur.fetchone()[0]
        print(room)
        cur.close()
        conn.close()
        return room
