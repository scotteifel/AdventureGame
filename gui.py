import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from db import (create_db_table, add_char, print_char, edit_char_attr,
get_current_room)

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
        self.master.geometry("%dx%d+%d+%d" % (470,300,x,y))

        self.lab = ttk.Label(self.master, text=prompt1,
                          font=("Arial Bold", 10),justify=tk.CENTER)

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
like to leave, head back west and out the door.".format(char=name))

        #Draw house navigation
        self.north = ttk.Button(self.master,text='North',command=self.go_north)
        self.south = ttk.Button(self.master,text='South',command=self.go_north)
        self.east = ttk.Button(self.master,text='East',command=self.go_north)
        self.west = ttk.Button(self.master,text='West',
                    command=self.master.destroy)

        self.north.grid(column=1,row=1)
        self.east.grid(column=2, row=2,sticky=tk.W)
        self.west.grid(column=0,row=2,sticky=tk.E)
        self.south.grid(column=1, row=3)
        self.quit.grid(column=1,row=4)


    def go_north(self):

        room = get_current_room()
        edit_char_attr({"tired":True, "room":1})

        if room == 1:
            self.north['state'] = 'disabled'
            self.west['state'] = 'disabled'

            self.lab.configure(text="You washed up in the restroom.  Wow what a\n\
            nice smelling soap they have.  Now you can go \nto the living room \
            to the east or head back to the \nmain room.")


    def go_east(self):

        room = get_current_room()

        if room == 1:
            edit_char_attr(room = 2)

            self.west['state'] = 'normal'
            self.east['state'] = 'disabled'

            self.lab.configure(text="Welcome to the workout room. \n\
Would you like to lift some weights?")


    def go_south(self):

        room = get_current_room()

        if room == 2:
            edit_char_attr(tired = True, room = 3)
            self.north['state'] = 'normal'

            self.lab.configure(text="Whoa you've entered the kitchen, and \
wow they have chosen a nice backsplash.  Do you want some water?  You're a \
kind of thirsty.")


    def go_west(self):

        room = get_current_room()

        if room == 2:
            edit_char_attr(tired = True, room = 1)
            self.west['state'] = 'disabled'

            self.lab.configure(text="You're back in the bathroom, you're tired\
.  Do you want to take a refreshing drink?  There's a cup right on the counter")

def main():

    create_db_table()
    root = ThemedTk(theme='arc')
    root.title('AdventureGame')
    app = Application(master=root)
    app.mainloop()



if __name__ == '__main__':
    main()
