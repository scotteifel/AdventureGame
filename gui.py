import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from db import (create_db_table, add_char, print_char, edit_char_attr,
get_current_room)


# This is how the rooms are numbered in the game layout
<<<<<<< HEAD
# 0 is the entrance room
# 1 is the bathroom
# 2 is the workout room
# 3 is the kitchen
# 4 is the living room
# 5 is the dining room
=======
>>>>>>> 00de1221adac94b978e294ef7c8db8bc11bc3a12
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
        self.master.geometry("490x330")
        self.lab.grid(padx=50,pady=50)
        add_char(name)
        self.enter.destroy()
        self.ask_name.destroy()
        self.lab.configure(text="Welcome to the main room {char}. \n\
It has a high ceiling and some plants.  The bathroom is north, \nthe \
kitchen is east.  There's a workout room to the south, and \nif you'd \
like to leave, head back west and out the door.".format(char=name),width=65)

        #Draw house navigation
<<<<<<< HEAD
        self.north = ttk.Button(self.master,text='North',
                                    command=self.go_north)
        self.south = ttk.Button(self.master,text='South',
                                    command=self.go_south)
=======
        self.north = ttk.Button(self.master,text='North',command=self.go_north)
        self.south = ttk.Button(self.master,text='South',command=self.go_south)
>>>>>>> 00de1221adac94b978e294ef7c8db8bc11bc3a12
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
<<<<<<< HEAD

        if room == 0:
            self.room_prompt(1)

            kw = {"tired":True, "room":"1"}
            edit_char_attr(**kw)

=======
        kw = {'tired':"True", "room":"1"}
        edit_char_attr(**kw)
        print(type(room),room,"   That is room")
        if room == 0:
            print("ROOM IS 0")
            char_inf = {'room':1}
            edit_char_attr(**char_inf)
>>>>>>> 00de1221adac94b978e294ef7c8db8bc11bc3a12
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

        elif room == 3:
            char_inf = {'room':'2'}
            edit_char_attr(**char_inf)

            self.north['state'] = 'disabled'
            self.east['state'] = 'disabled'

        elif room == 5:
            char_inf = {'room':0}
            edit_char_attr(**char_inf)

            self.west['state'] = 'normal'
            self.south['state'] = 'normal'

        elif room == 4:
            char_inf = {'room':3}
            edit_char_attr(**char_inf)

            self.south['state'] = 'normal'


    def go_east(self):
        room = get_current_room()

        if room == 1:
<<<<<<< HEAD
            self.room_prompt(2)

=======
>>>>>>> 00de1221adac94b978e294ef7c8db8bc11bc3a12
            char_inf = {'room':2}
            edit_char_attr(**char_inf)

        elif room == 0:
<<<<<<< HEAD
            self.room_prompt(3)

=======
>>>>>>> 00de1221adac94b978e294ef7c8db8bc11bc3a12
            char_inf = {'room':3}
            edit_char_attr(**char_inf)

        elif room == 5:
<<<<<<< HEAD
            self.room_prompt(4)

=======
>>>>>>> 00de1221adac94b978e294ef7c8db8bc11bc3a12
            char_inf = {'room':4}
            edit_char_attr(**char_inf)

        self.east['state'] = 'disabled'
<<<<<<< HEAD
        self.west['state'] = 'normal'
=======
>>>>>>> 00de1221adac94b978e294ef7c8db8bc11bc3a12


    def go_south(self):
        room = get_current_room()

        if room == 1:
<<<<<<< HEAD
            self.room_prompt(0)

            char_inf = {'room':0}
            edit_char_attr(**char_inf)


        elif room == 2:
            self.room_prompt(3)

            char_inf = {'room':3}
            edit_char_attr(**char_inf)


        elif room == 0:
            self.room_prompt(5)

=======
            char_inf = {'room':0}
            edit_char_attr(**char_inf)

        elif room == 2:
            char_inf = {'room':3}
            edit_char_attr(**char_inf)

        elif room == 0:
>>>>>>> 00de1221adac94b978e294ef7c8db8bc11bc3a12
            char_inf = {'room':5}
            edit_char_attr(**char_inf)

            self.south['state'] = 'disabled'

        elif room == 3:
<<<<<<< HEAD
            self.room_prompt(4)

=======
>>>>>>> 00de1221adac94b978e294ef7c8db8bc11bc3a12
            char_inf = {'room':4}
            edit_char_attr(**char_inf)

            self.south['state'] = 'disabled'
<<<<<<< HEAD
        self.north['state'] = 'normal'
=======
>>>>>>> 00de1221adac94b978e294ef7c8db8bc11bc3a12



    def go_west(self):
        room = get_current_room()

        if room == 0:
            self.master.destroy()

        elif room == 2:
<<<<<<< HEAD
            self.room_prompt(1)

            char_inf = {'room':1}
            edit_char_attr(**char_inf)
            self.west['state'] = 'disabled'

        elif room == 3:
            self.room_prompt(0)


=======
            char_inf = {'room':1}
            edit_char_attr(**char_inf)

        elif room == 3:
>>>>>>> 00de1221adac94b978e294ef7c8db8bc11bc3a12
            char_inf = {'room':0}
            edit_char_attr(**char_inf)

        elif room == 4:
<<<<<<< HEAD
            self.room_prompt(5)

            char_inf = {'room':5}
            edit_char_attr(**char_inf)
            self.west['state'] = 'disabled'

        self.east['state'] = 'normal'


    def room_prompt(self,_room):

        if _room == 0:
            self.lab.configure(text="You're in the entrance hall")

        elif _room == 1:
            self.lab.configure(text="You washed up in the restroom.  Wow \
what a\n nice smelling soap they have.  Now you can go \nto the living room \
to the east or head back to the \nmain room.",justify=tk.CENTER)

        elif _room == 2:
            self.lab.configure(text="You're in the workout room")
=======
            char_inf = {'room':5}
            edit_char_attr(**char_inf)

        self.east['state'] = 'disabled'
>>>>>>> 00de1221adac94b978e294ef7c8db8bc11bc3a12

        elif _room == 3:
            self.lab.configure(text="You're in the kitchen.  Wow a chicken!")

        elif _room == 4:
            self.lab.configure(text="You're in the diningroom")

        elif _room == 5:
            self.lab.configure(text="You're in the livingroom")


def main():

    create_db_table()
    root = ThemedTk(theme='arc')
    root.title('AdventureGame')
    app = Application(master=root)
    app.mainloop()



if __name__ == '__main__':
    main()
