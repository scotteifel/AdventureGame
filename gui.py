import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from db import (create_db_table, add_char, print_char, edit_char_attr,
get_current_room, get_char_attr)


# This is how the rooms are numbered in the game layout
# 0 is the entrance room
# 1 is the bathroom
# 2 is the workout room
# 3 is the kitchen
# 4 is the dining room
# 5 is the living room
#        -------
# ____  | 1 | 2 |
# Entr. | 0 | 3 |
# ____  | 5 | 4 |
#        -------

prompt1 = "Welcome to the Adventure.  What's your name kind traveler?"

class Application(ttk.Frame):

    def __init__(self, master=None):

        super().__init__(master)
        self.master = master

        #Place the window in the center of the screen
        mon_w = self.master.winfo_screenwidth()
        mon_h = self.master.winfo_screenheight()
        x = (mon_w / 2) - (150)
        y = (mon_h / 2) - (150)
        self.master.geometry("%dx%d+%d+%d" % (540,300,x,y))

        self.lab = ttk.Label(self.master, text=prompt1,
             font=("Arial Bold", 10),justify=tk.CENTER,width=55)

        self.ask_name = ttk.Entry(self.master)

        self.enter = ttk.Button(self.master, text="Enter",
                            command=self.set_name)
        self.quit = ttk.Button(self.master, text="Quit",
                            command=self.master.destroy)

        self.lab.grid(columnspan=3,column=0, row=0,padx=40,pady=40)
        self.ask_name.grid(column=1,row=1)
        self.enter.grid(column=1, row=2)
        self.quit.grid(column=1, row=3,pady=15)

    #Store the players name
    def set_name(self):
        name = self.ask_name.get()
        if len(name) == 0:
            return
        self.master.geometry("510x400")
        self.lab.grid(padx=50,pady=50)
        add_char(name)
        self.enter.destroy()
        self.ask_name.destroy()
        self.lab.configure(text="Welcome to the main room {char}. \n\
It has a high ceiling and some plants.  The bathroom is North and \nthe \
kitchen is to the East.  There's a workout room to the South, and \nif \
you'd like to leave, head back West and out the door.  \nWhy not explore?"
.format(char=name),width=65)

        #Draw house navigation
        self.north = ttk.Button(self.master,text='North',
                                    command=self.go_north)
        self.south = ttk.Button(self.master,text='South',
                                    command=self.go_south)
        self.east = ttk.Button(self.master,text='East',command=self.go_east)
        self.west = ttk.Button(self.master,text='West',
                    command=self.go_west)

        self.north.grid(column=1,row=1)
        self.east.grid(column=2, row=2,sticky=tk.W)
        self.west.grid(column=0,row=2,sticky=tk.E)
        self.south.grid(column=1, row=3)
        self.quit.grid(column=1,row=4)


    def go_north(self):

        room = get_current_room()

        if room == 0:
            self.room_prompt(1)

            kw = {"tired":True, "room":"1"}
            edit_char_attr(**kw)

            self.north['state'] = 'disabled'
            self.west['state'] = 'disabled'

        elif room == 3:
            self.room_prompt(2)

            char_inf = {'room':'2'}
            edit_char_attr(**char_inf)

            self.north['state'] = 'disabled'
            self.east['state'] = 'disabled'

        elif room == 5:
            self.room_prompt(0)

            char_inf = {'room':0}
            edit_char_attr(**char_inf)

            self.west['state'] = 'normal'

        elif room == 4:
            self.room_prompt(3)

            char_inf = {'room':3}
            edit_char_attr(**char_inf)

        self.south['state'] = 'normal'


    def go_east(self):
        room = get_current_room()

        if room == 1:
            self.room_prompt(2)

            char_inf = {'room':2}
            edit_char_attr(**char_inf)

        elif room == 0:
            print("Room is 0")
            self.room_prompt(3)

            char_inf = {'room':3}
            edit_char_attr(**char_inf)

        elif room == 5:
            self.room_prompt(4)

            char_inf = {'room':4}
            edit_char_attr(**char_inf)

        self.east['state'] = 'disabled'
        self.west['state'] = 'normal'


    def go_south(self):
        room = get_current_room()

        if room == 1:
            self.room_prompt(0)

            char_inf = {'room':0}
            edit_char_attr(**char_inf)


        elif room == 2:
            self.room_prompt(3)

            char_inf = {'room':3}
            edit_char_attr(**char_inf)


        elif room == 0:
            self.room_prompt(5)

            char_inf = {'room':5}
            edit_char_attr(**char_inf)

            self.south['state'] = 'disabled'

        elif room == 3:
            self.room_prompt(4)

            char_inf = {'room':4}
            edit_char_attr(**char_inf)

            self.south['state'] = 'disabled'
        self.north['state'] = 'normal'



    def go_west(self):
        room = get_current_room()

        if room == 0:
            self.master.destroy()

        elif room == 2:
            self.room_prompt(1)

            char_inf = {'room':1}
            edit_char_attr(**char_inf)
            self.west['state'] = 'disabled'

        elif room == 3:
            self.room_prompt(0)

            char_inf = {'room':0}
            edit_char_attr(**char_inf)

        elif room == 4:
            self.room_prompt(5)

            char_inf = {'room':5}
            edit_char_attr(**char_inf)
            self.west['state'] = 'disabled'

        self.east['state'] = 'normal'


    def room_prompt(self,_room):
        stats = get_char_attr()
        #Values of stats response by index order are:
        # 0 = name
        # 1 = thirsty (1 is yes, 0 is no)
        # 2 = hungry (1 is yes, 0 is no)
        # 3 = tired (1 is yes, 0 is no)
        # 4 = strength level
        # 5 = current room

########################     ENTRANCE     ##################################
        if _room == 0:
            print("ENTRANCE ROOM")
            self.lab.configure(text="You're back in the entrance hall.  Go \
west to head out the door.")

########################     RESTROOM     ##################################
        elif _room == 1:

            #Check the player's thirst
            if stats[1] == 0:

                self.lab.configure(text="You washed up in the restroom. \
You took a sip from a dixie cup and are refreshed.", justify=tk.CENTER)

            else:
                self.lab.configure(text="You washed up in the restroom.  Wow \
what a nice \nsmelling soap they have.  Now you can go \nto the living room \
to the east or head back to the \nmain room.",justify=tk.CENTER)

########################     WORKOUT ROOM     #############################
        elif _room == 2:
            print("ROOM 2 WORKOUT ROOM")

            #Check if the player is tired
            if stats[3] == 0:
                print("The player's tired")

                self.lab.configure(text="You're too tired to lift and run, \
after you rest you should be \ngood to go though.  If you can find a nice \
chair to sink\n into.  That should do the trick.")

            #Check the player's hunger
            elif stats[2] == 0:
                self.lab.configure(text="Mm, you need a snack for some \
strength before you hit the\n iron.  Try looking around for something to \
munch on.")


            #Check if the player's thirsty
            elif stats[1] == 0:
                 self.lab.configure(text="Here's the workout room, but ahh, \
you're parched and there's no \nwatertank in here.  You need a refreshment \
before you get going with any workouts.  Search some other rooms for \
something to help with that")

            else:
                self.lab.configure(text="You're in the exercise room now and \
wow, look at you go.  \nWhoa, did you stretch?  Alright, alright!  You are\n \
really doing a great job.  That definately tired you \nout.  You could use \
something to drink, and maybe a snack, \ntoo.  if you want to workout some \
more.  The kitchen might be a \ngood place make your way to.")

            kw = {'thirsty': 0,'hungry':0,'tired':0,'strength':1}
            edit_char_attr(**kw)

########################    KITCHEN     #####################################
        elif _room == 3:
            print("IN ROOM 3, KITCHEN")

            #Check thirst
            if stats[1] == 0:
                print("Yes I am thirsty.")

                self.lab.configure(text="You're in the kitchen.  This is a \
nice area with marble countertops\n and recently updated cabinets.  You \
drink a glass of nice cold water\n and are refreshed.")

                kw = {'thirsty': 1}
                edit_char_attr(**kw)

            else:
                print("No I'm not thirsty.")

                self.lab.configure(text="You're in the kitchen.  This is a \
nice area with marble countertops\n and recently updated cabinets.  You're \
satisfied so \nthere's no need for a drink of water for ya now.")

########################    DININGROOM     ################################
        elif _room == 4:
            print("DINING ROOM")
            #Check hunger
            if stats[2] == 0:
                print("Yes I'm hungry")

                self.lab.configure(text="You're in the diningroom.  MMM \
there's freshly cooked ham\n on a platter for you to enjoy.  You grab a \
slice,\n and a piece of the pineapple that's on it too.  Mmm mm,\n was that \
satisfying.")

                kw = {'hungry': 1}
                edit_char_attr(**kw)

            else:
                print("Not hungry")

                self.lab.configure(text="You're in the diningroom now and \
there's a delicious ham set out.\n  You're not hungry, but maybe in a bit \
you can have a piece.")

#####################      LIVINGROOM      ##################################
        elif _room == 5:
            print("LIVING ROOM")

            #Check the if the player's tired
            if stats[3] == 0:

                self.lab.configure(text="Your in the livingroom.  It's \
really nice with great\n furniture and tall drapes and the sunshine is really \
streaming in\n through that window.  Ohh what a nice recliner there\n is in \
the corner!  You sit down, play a little Sudoku,\n and rest for a bit.  \
Whoa, where did the time\n go??  You dozed off for a minute!  \nA bite \
to eat seems to be in order now.\n  Where's that diningroom?")
                kw = {'hungry': 0, 'tired':1}
                edit_char_attr(**kw)
            else:

                self.lab.configure(text="Your in the livingroom.  It's \
really nice with great furniture and tall\n drapes.  The sunshine is really \
streaming in through that window.")


def main():

    create_db_table()
    root = ThemedTk(theme='arc')
    root.title('AdventureGame')
    app = Application(master=root)
    app.mainloop()


if __name__ == '__main__':
    main()
