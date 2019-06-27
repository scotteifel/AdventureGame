from player import Player
from room import Room
import sys

proceed = ["Yes", "yes", "Y", "y"]
leave_list = ["Goodbye", 'goodbye', 'Bye', 'bye']
inMain = False

print("\nWelcome to the Adventure")
answer = input("You are invited into the house, would you like to enter?  Yes to proceed, No to exit.")



while not answer in proceed:
    if answer in ("No", "no", "N", "n"):
        sys.exit("\nHave a nice day.")
    answer = input("Type yes to enter or no to exit.")

name = input("What's your name kind traveler? \n")
print("Excellent, explore the house %s and see what it's like if you will\n" % (name,))

print("\nYou're now in the main room.  It has a high ceiling and some plants.\n")
print("The bathroom is on your left, the kitchen is straight ahead, and theres a workout room to the right.\n")
print("To explore this house, you can use a keyboard and press the number of a room your near to enter it.")
direction = input("Bathroom(2), kitchen(4), or the workout room(6).  You can also leave by typing 'Goodbye'\n  So where to??\n: ")
err = "You can't access that room from here"

player = Player(name)
room = Room()

while True:
    if direction == "1":
        room.room1()



    # destination = "room"+str(direction)
    # room(destination())


#
#
# def game():
#
#         if direction == "2":
#             print("\nYou washed up in the restroom!  What a nice smelling soap this house has!")
#             inMain = True
#             print(direction[:1])
#             direction = input("Now you can go to the living room by typing 3 or back to the mainroom by typing 1.  Where to next?\n")
#
#         if direction == "3":
#             print("\nYour in the livingroom.  It's really nice with great furniture and tall drapes.  The sun is really coming in through that window as well!\n")
#             inMain = False
#             direction = input("Head to the kitchen by pressing 4, or back to the restroom with 2.")
#
#         if direction == "1":
#             print("\nYou're back in the mainroom, wow this is a nice room.\n")
#             inMain = False
#             direction = input("To leave, type 'Goodbye', go to the livingroom(3), or stop in the bathroom(2)")
#
#         if direction == "4":
#             print("Ohh now this is a nice kitchen. The counter is a blue marble, and the cabinets a deep brown.  Yum, a pineapple!  You love it and eat a slice")
#             inMain = False
#             direction = input("After that delicious morsel, do you want to go to the livingroom(3), the dining room(5), or back to the mainroom(1)?")
#
#         if direction == "5":
#             print("Hum, looks like pork and pineapple are on the menu.  Ohh theres some seltzer water, you have a glug and are refreshed.")
#             inMain = False
#             direction = input("Into the kitchen(4)?  Or there is a workout room(6) to your right you can go to.")
#
#         if direction == "6":
#             print("Wow, this room looks great!  There's a bench with some weights on it, about 120 pounds.  There's also an elliptical.  You get some exercise, and are thirsy.  Maybe a trip to the kitchen is in order for a refreshment!\n")
#             inMain = False
#             direction = input("The mainroom(6) is to your left, and the diningroom(5) is straight ahead.  Where do you want to go now?")
#
#
#         if direction[:1].lower() == "g" and inMain == True:
#             sys.exit("Have a nice day.")
#             print("Heyyoo")
#
#         if direction not in ('1','2','3','4','5','6'):
#             print("Whoops try that again please.")
#             direction = input("Where to?")
#
# while True:
#     game()
