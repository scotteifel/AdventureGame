# from tkinter import *
# from tkinter import ttk
#
# def calculate(*args):
#     try:
#         value = float(feet.get())
#         meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
#     except ValueError:
#         pass
#
# root = Tk()
# root.title("Adventure Game")
#
# mainframe = ttk.Frame(root, padding="3 3 12 12")
# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
#
# feet = StringVar()
# meters = StringVar()
#
# feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
# feet_entry.grid(column=2, row=1, sticky=(W, E))
#
# ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
# ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)
#
# ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
# ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
# ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)
#
# for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
#
# feet_entry.focus()
# root.bind('<Return>', calculate)
#
# root.mainloop()


from tkinter import *
from other import tested

window = Tk()

window.title("Adventure Game")

def entered():
    lab.configure(text="Button Clicked")
    tested()


window.geometry('600x400')

lab = Label(window, text="Welcome to the Adventure.  You are invited into the house, would you like to enter?",
            font=("Arial Bold", 10))

lab.grid(column=1, row=0)

btn1 = Button(window, text="Yes to Enter.", command=entered)

btn2 = Button(window, text="No to leave", command=window.destroy)

btn1.grid(column=1, row=1)
btn2.grid(column=1, row=2)

window.mainloop()
