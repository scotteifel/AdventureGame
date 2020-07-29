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
        cur.execute('''INSERT INTO character (name,thirsty,hungry,tired,
                    room_tracker) VALUES (?,?,?,?,?)''', (name,1,1,0,0))
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
        cur.execute('''UPDATE character SET room_tracker = {x} WHERE
                        name = (?)'''.format(x=kwargs['room']), (CRNT_PLYR,))
        conn.commit()

        # if kwargs['tired'] == True:
        #     cur.execute('''UPDATE character SET tired = 1 WHERE name =
        #                     (?)''',(CRNT_PLYR,))

        conn.commit()
        cur.close()

def get_current_room():
    
        conn = sqlite3.connect("main.db")
        cur = conn.cursor()
        cur.execute('''SELECT room_tracker FROM character WHERE name =
                        (?)''',(CRNT_PLYR,))
        room = cur.fetchone()[0]
        cur.close()
        conn.close()
        return room
