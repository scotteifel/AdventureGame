import sqlite3, os
global CRNT_PLYR

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
        global CRNT_PLYR
        CRNT_PLYR = name

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

        conn = sqlite3.connect("main.db")
        cur = conn.cursor()
        cur.execute('''UPDATE character SET room_tracker = {x}'''
                        .format(x=kwargs["room"]))
        conn.commit()
        print("room is ",kwargs["room"])

        if kwargs['tired'] == True:
            cur.execute('''UPDATE character SET tired = 1''')

        conn.commit()
        cur.close()
        print_char()

def get_current_room():
        print_char()
        print("Just printed")
        conn = sqlite3.connect("main.db")
        cur = conn.cursor()
        cur.execute('''SELECT room_tracker WHERE name={tab}'''
        .format(tab=CRNT_PLYR))
        room = cur.fetchone()[0]
        print(room, " This is from the db")
        cur.close()
        conn.close()
        return room
