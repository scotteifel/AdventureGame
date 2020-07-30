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
                        strength INTEGER, room_tracker INTEGER)''')
        conn.commit()
        cur.close()
        conn.close()

#See if character has already played
def check_char(submission):
        global CRNT_PLYR

        conn = sqlite3.connect("main.db")
        cur = conn.cursor()
        cur.execute('''SELECT name FROM character WHERE name = (?)''',
                        (submission,))
        if cur.fetchone():
                CRNT_PLYR = submission

                cur.execute('''UPDATE character SET room_tracker = 0 WHERE
                        name = (?)''',(submission,))
                conn.commit()
                cur.close()
                conn.close()
                return True
        else:
            return

def add_char(name):
        global CRNT_PLYR
        CRNT_PLYR = name

        conn = sqlite3.connect("main.db")
        cur = conn.cursor()
        cur.execute('''INSERT INTO character (name,thirsty,hungry,tired,
            strength,room_tracker) VALUES (?,?,?,?,?,?)''', (name,1,1,0,0,0))
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

        if 'room' in kwargs:

            cur.execute('''UPDATE character SET room_tracker = {x} WHERE
                    name = (?)'''.format(x=kwargs['room']), (CRNT_PLYR,))
            conn.commit()

        if 'thirsty' in kwargs:

            if kwargs['thirsty'] == 1:
                cur.execute('''UPDATE character SET thirsty = 1 WHERE name =
                (?)''',(CRNT_PLYR,))
            else:
                 cur.execute('''UPDATE character SET thirsty = 0 WHERE name =
                 (?)''',(CRNT_PLYR,))

            conn.commit()

        if 'hungry' in kwargs:

            if kwargs['hungry'] == 1:
                cur.execute('''UPDATE character SET hungry = 1 WHERE name =
                (?)''',(CRNT_PLYR,))
            else:
                 cur.execute('''UPDATE character SET hungry = 0 WHERE name =
                 (?)''',(CRNT_PLYR,))
            conn.commit()

        if 'tired' in kwargs:

            if kwargs['tired'] == 1:
                cur.execute('''UPDATE character SET tired = 1 WHERE name =
                (?)''',(CRNT_PLYR,))
            else:
                 cur.execute('''UPDATE character SET tired = 0 WHERE name =
                 (?)''',(CRNT_PLYR,))
            conn.commit()

        if 'strength' in kwargs:
            #Set thirst, hunger, and tired to 0
            cur.execute('''UPDATE character SET thirsty = 0, hungry = 0,
                tired = 0 WHERE name = (?)''', (CRNT_PLYR,))
            conn.commit()

            #Add one strength
            cur.execute('''SELECT strength from character WHERE name =
            (?)''',(CRNT_PLYR,))
            new_strength = cur.fetchone()[0]
            new_strength+=1
            print("New strength is ", new_strength)
            cur.execute('''UPDATE character SET strength = (?) WHERE
                name = (?)''',(new_strength, CRNT_PLYR))


            conn.commit()
        cur.close()
        conn.close()

def get_char_attr():

        conn = sqlite3.connect("main.db")
        cur = conn.cursor()
        cur.execute('''SELECT * FROM character WHERE name = (?)''',
                        (CRNT_PLYR,))

        stats = cur.fetchone()
        cur.close()
        conn.close()
        return stats

def get_current_room():

        conn = sqlite3.connect("main.db")
        cur = conn.cursor()
        cur.execute('''SELECT room_tracker FROM character WHERE name =
                        (?)''',(CRNT_PLYR,))
        room = cur.fetchone()[0]
        cur.close()
        conn.close()
        return room
