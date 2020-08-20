import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import tkinter.font as tkfont
from PIL import Image, ImageTk
import math

from db import (create_db_table, add_char, print_char, edit_char_attr,
get_current_room, get_char_attr, check_char)


# This is how the rooms are numbered in the game layout
# 0 : entrance room
# 1 : bathroom
# 2 : workout room
# 3 : kitchen
# 4 : dining room
# 5 : living room
#        -------
# _______    | 1 | 2 |
# Out front. | 0 | 3 |
# _______   | 5 | 4 |
#        -------


prompt1 = "Welcome to the Adventure!  What's your name kind traveler?"

class Application(ttk.Frame):

    def __init__(self, master=None):

        super().__init__(master)
        self.master = master

        img = Image.open('hammock.png')
        self.img = ImageTk.PhotoImage(img)
        imgx,imgy=self.img.width()+40,self.img.height()+40
        ###     Place the window in the center of the screen     ###
        mon_w = self.master.winfo_screenwidth()
        mon_h = self.master.winfo_screenheight()
        x = (mon_w / 2) - (150)
        y = (mon_h / 2) - (150)
        self.master.geometry("%dx%d+%d+%d" % (465,330,x,y))

        ##Placing final stage window with already retrieved variables
        ## x and y, then hiding until final strength level is achieved.
        self.win1 = tk.Toplevel(self.master)
        self.win1.geometry("%dx%d+%d+%d" % (imgx,imgy,x-190,y-400))
        self.win1.withdraw()

        self.master.configure(bg="#51e880")
        #tk and not ttk is used for the availability of extra attributes
        self.lab = tk.Label(self.master, text=prompt1,
font=("Bodoni MT", 16),justify=tk.CENTER,width=25,
wraplength=300,bg="#51b8e8",fg='darkblue',padx=35,pady=20,relief='raised')

        self.ask_name = ttk.Entry(self.master)
        self.ask_name.focus()

        self.enter = ttk.Button(self.master, text="Enter",
                            command=self.set_name)
        self.enter.bind(sequence="<ButtonRelease>", func=self.set_name)
        self.master.bind("<Return>", self.set_name)

        self.quit = ttk.Button(self.master, text="Quit",
                            command=self.master.destroy)

        self.lab.grid(columnspan=3,column=0, row=0,padx=45,pady=40)
        self.ask_name.grid(column=1,row=1)
        self.enter.grid(column=1, row=2,pady=15)
        self.quit.grid(column=1, row=3)
        print_char()



    #Store the players name
    def set_name(self,event):
        name = self.ask_name.get().lower()

        #Check if the player is already in the database
        if len(name) == 0:
            return
        #Welcome back prompt
        elif check_char(name):
            self.lab.configure(text="Hello again {char}, it's nice to \
have you back.  You're now in the entrance hall, the ceiling is \
high and there are various plants throughout room.  \nThe bathroom is \
North and the kitchen is to the East.  Head South to find the living room.  \
When you'd like to leave, head back West and out the door."
.format(char=name.title()),width=35,wraplength=400,height=9,padx=35,pady=20)
            pass
        #First welcome prompt
        else:
            add_char(name)
            self.lab.configure(text="Welcome to the main room {char}, \
it has a high ceiling and some plants.  The bathroom is North and the \
kitchen is to the East.  There's a workout room somewhere in here, and if \
you'd like to leave, head back West and out the door."
.format(char=name.title()),width=35,wraplength=400,
height=9,padx=20,pady=20)

        self.master.geometry("605x540")
        self.lab.grid(padx=67,pady=40)
        self.enter.destroy()
        self.ask_name.destroy()
        self.quit.destroy()

        #Draw house navigation
        self.north = ttk.Button(self.master,text='North',
                                    command=self.go_north)
        self.south = ttk.Button(self.master,text='South',
                                    command=self.go_south)
        self.east = ttk.Button(self.master,text='East',command=self.go_east)
        self.west = ttk.Button(self.master,text='EXIT',
                    command=self.go_west)

        self.north.grid(column=1,row=1)
        self.east.grid(column=2, row=2,sticky=tk.W)
        self.west.grid(column=0,row=2,sticky=tk.E)
        self.south.grid(column=1, row=3)


################Processing room navigation##################
    def go_north(self):
        room = get_current_room()

        if room == 0:
            self.north['state'] = 'disabled'
            self.west['state'] = 'disabled'

            self.room_prompt(1)

            kw = {"tired":True, "room":"1"}
            edit_char_attr(**kw)

        elif room == 3:
            self.north['state'] = 'disabled'
            self.east['state'] = 'disabled'

            self.room_prompt(2)

            char_inf = {'room':'2'}
            edit_char_attr(**char_inf)

        elif room == 5:
            self.west['state'] = 'normal'

            self.room_prompt(0)

            char_inf = {'room':0}
            edit_char_attr(**char_inf)

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
            self.west['state'] = 'normal'


        elif room == 2:
            self.room_prompt(3)

            char_inf = {'room':3}
            edit_char_attr(**char_inf)


        elif room == 0:
            self.room_prompt(5)

            char_inf = {'room':5}
            edit_char_attr(**char_inf)
            self.south['state'] = 'disabled'
            self.west['state'] = 'disabled'

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
########End of processing room navigation


    def room_prompt(self,_room):
        stats = get_char_attr()
        print_char()
        #Values of stats response by index order are:
        # 0 = name
        # 1 = thirsty (1 is yes, 0 is no)
        # 2 = hungry (1 is yes, 0 is no)
        # 3 = tired (1 is yes, 0 is no)
        # 4 = strength level
        # 5 = current room


########################     ENTRANCE     ##################################
        if _room == 0:
            self.lab.configure(text="You're back in the entrance hall.  \
Head west to go out the door.")

########################     RESTROOM     ##################################
        elif _room == 1:

            #Check the player's thirst
            if stats[1] == 0:

                self.lab.configure(text="You washed up in the restroom. \
You took a sip from a dixie cup and are refreshed.", justify=tk.CENTER)

            else:
                self.lab.configure(text="You washed up in the restroom.  \
Wow what a nice smelling soap they have.  Now you can go to the living \
room to the east or head back to the main room.",justify=tk.CENTER)

########################     WORKOUT ROOM     #############################
        elif _room == 2:
            print(stats[3])

            #Check if the player is tired
            if stats[3] == 0:

                self.lab.configure(text="You're too tired to lift and run, \
after you rest you should be good to go though.  If you can find a nice \
chair to sink into, that could do the trick.")

            #Check the player's hunger
            elif stats[2] == 0:
                self.lab.configure(text="Mm, you need a snack for some \
strength before you hit the iron.  Try looking around for something to \
munch on.")


            #Check if the player's thirsty
            elif stats[1] == 0:
                 self.lab.configure(text="Here's the workout room, but ahh, \
you're parched and there's no watertank in here.  You need a refreshment \
before you get going with any workouts.  Search some other rooms for \
something to help with that")

            ##Hidden suprise accessed at strength 5  Hammock is accessed
            #Strength 5 is reached
            elif stats[4] >= 4:

                print("done")
                self.lab.configure(text="Strength 5 achieved.  You head \
to the door and tug on it, it opens up.  Wow you're outside and there's a \
hammock swinging there between some strong trees.  You go and lay down and close \
you're eyes.  Congratulations, you've gained great comfort! \n \
Game's Over.")

                self.north.destroy()
                self.west.destroy()
                self.east.destroy()
                self.south['text'] = "Exit"
                self.south.configure(command=self.master.destroy)
                self.south.grid(pady=35)
                self.win1.deiconify()
                self.canv = tk.Label(self.win1, image=self.img,relief="solid")
                self.canv.grid(row=0,column=0,padx=15,pady=15)
                return



            elif stats[4] >= 2:
                self.lab.configure(text="You're back in the exercise \
room and you're at it again!  Whoa, you are really getting stronger, \
if you keep this up you might be able to open that jammed door leading \
to the backyard.  Welp, you'll need more rest and nutrition if you plan \
on opening that door up.")

                kw = {'thirsty': 0,'hungry':0,'tired':0,'strength':1}
                edit_char_attr(**kw)

            else:
                self.lab.configure(text="You're in the exercise room now \
and wow, look at you go.  Whoa, did you stretch?  Alright, alright!  You \
are really doing a great job.  That definately tired you out.  You could \
use something to drink, and maybe a snack, too, if you want to workout \
some more.  The kitchen might be a good place to make your way to.")
                kw = {'thirsty': 0,'hungry':0,'tired':0,'strength':1}
                edit_char_attr(**kw)


########################    KITCHEN     ###################################
        elif _room == 3:

            #Check thirst
            if stats[1] == 0:

                self.lab.configure(text="You're in the kitchen.  This is a \
nice area with marble countertops and recently updated cabinets.  You \
drink a glass of nice cold water and are refreshed.")

                kw = {'thirsty': 1}
                edit_char_attr(**kw)

            else:
                self.lab.configure(text="You're in the kitchen.  This is a \
nice area with marble countertops and recently updated cabinets.  You're \
satisfied so there's no need for a drink of water for ya now.")

########################    DININGROOM     ################################
        elif _room == 4:
            #Check hunger
            if stats[2] == 0:

                self.lab.configure(text="You're in the diningroom.  MMM \
there's freshly cooked ham on a platter for you to enjoy.  You grab a \
slice, and a piece of the pineapple that's on it too.  Mmm mm, was that \
satisfying.")

                kw = {'hungry': 1}
                edit_char_attr(**kw)

            else:
                self.lab.configure(text="You're in the diningroom now and \
there's a delicious ham set out.  You're not hungry, but maybe in a bit \
you can have a piece.")

#####################      LIVINGROOM      ##################################
        elif _room == 5:

            #Check the if the player's tired
            if stats[3] == 0:

                self.lab.configure(text="You're in the livingroom.  It's \
really nice with great furniture and tall drapes.  Wow the sunshine is \
really streaming in through that window, too.  Ohh what a nice recliner \
there is in the corner!  You sit down, play a little Sudoku, and rest for \
a bit.  Whoa, where did the time go??  You dozed off for a minute!  A bite \
to eat seems to be in order now.  Where's that diningroom?")
                kw = {'hungry': 0, 'tired':1}
                edit_char_attr(**kw)
            else:

                self.lab.configure(text="Your in the livingroom.  It's \
really nice with great furniture and tall drapes.  The sunshine is really \
streaming in through that window.")

        if _room == 0:
            self.west['text'] = "EXIT"
        else:
            self.west['text'] = "West"



def main():

    create_db_table()
    root = ThemedTk(theme='arc')
    root.title('AdventureGame')
    root.resizable(False,False)
    app = Application(master=root)
    app.mainloop()


if __name__ == '__main__':
    main()
