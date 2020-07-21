import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from db import create_table, add_char, print_char, edit_char_attr

prompt1 = "Welcome to the Adventure.  What's your name kind traveler?"

class Application(ttk.Frame):

    def __init__(self, master=None):

        super().__init__(master)
        self.master = master

        #Place the window in the center of the screen
        mon_w = self.master.winfo_screenwidth()
        mon_h = self.master.winfo_screenheight()

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
        add_char(name)
        self.enter.destroy()
        self.ask_name.destroy()
        self.lab.configure(text="Welcome to the main room {char}. \n\
It has a high ceiling and some plants.  The bathroom is on \
your left, \nthe kitchen is straight ahead, and theres a workout \
room to the right.".format(char=name))

        #Draw house navigation
        self.north = ttk.Button(self.master, text='North', command=self.entered)
        self.south = ttk.Button(self.master, text='South', command=self.entered)
        self.east = ttk.Button(self.master, text='East', command=self.entered)
        self.west = ttk.Button(self.master, text='West', command=self.entered)

        self.north.grid(column=1,row=1)
        self.east.grid(column=2, row=2,sticky=tk.W)
        self.west.grid(column=0,row=2,sticky=tk.E)
        self.south.grid(column=1, row=3)
        self.quit.grid(column=1,row=4)


    def entered(self):
        name = self.ask_name.get()
        print(name, "  IS NAME")
        add_char(name)
        print_char()


 #
 #        self.lab.configure(text="You're now in the main room.  It\
 # has a high ceiling and some plants.\nThe bathroom is on your left, the kitchen\
 # is straight ahead, and theres a workout room to the right.\n")
 #
 #        # print("You're now in the main room.  It has a high ceiling\
 #        #        and some plants.\n")
 #        # print("The bathroom is on your left, the kitchen is straight\
 #        #        ahead, and theres a workout room to the right.\n")
 #        # print("To explore this house, use your keyboard to press the\
 #        #        number of a room your near to enter it.")
 #        # print("Bathroom(2), kitchen(4), or the workout room(6).  ")
 #        print("ok")
 #        # tested()


def main():

    create_table()
    root = ThemedTk(theme='arc')
    root.title('AdventureGame')
    # root.geometry('500')
    app = Application(master=root)
    app.mainloop()



if __name__ == '__main__':
    main()
