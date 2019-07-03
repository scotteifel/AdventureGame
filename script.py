from player import Player
import sys

proceed = ["Yes", "yes", "Y", "y"]
leave_list = ["Goodbye", 'goodbye', 'Bye', 'bye']
no_list = ["No", "no", "N", "n"]
inMain = False

print("\nWelcome to the Adventure")
answer = input("You are invited into the house, would you like to enter?  Yes to proceed, No to exit.")



while not answer in proceed:
    if answer in no_list:
        sys.exit("\nHave a nice day.")
    answer = input("Type yes to enter or no to exit.")

name = input("What's your name kind traveler? \n")
print("\nExcellent, explore the house %s and see what it's like.\n" % (name,))
err = "You can't access that room from here"
direction = ""
player = Player(name)

while direction not in leave_list:

    last_location = ""


    # print("Bathroom(2), kitchen(4), or the workout room(6).  ")
    # direction = input("You can also leave by typing 'Goodbye'\n  So where to??\n: ")

    # Primary prompt when entering house.
    if player.direction == "JUST ENTERED...":
        print("You're now in the main room.  It has a high ceiling and some plants.\n")
        print("The bathroom is on your left, the kitchen is straight ahead, and theres a workout room to the right.\n")
        print("To explore this house, use your keyboard to press the number of a room your near to enter it.")
        print("Bathroom(2), kitchen(4), or the workout room(6).  ")
        player.direction = input("You can also leave by typing 'Goodbye'\n  So where to??\n: ")

    if player.direction == "1":
        last_location = direction
        player.enter_room_1()

    if player.direction == "2":
        last_location = direction
        this = player.enter_room_2()

    if player.direction == "3":
        last_location = direction
        player.enter_room_3()

    if player.direction == "4":
        last_location = direction
        player.enter_room_4()

    if player.direction == "5":
        last_location = direction
        player.enter_room_5()

    if player.direction == "6":
        last_location = direction
        player.enter_room_6()

    if player.direction in leave_list:
        sys.exit("\nHave a nice day %s!" %(player.name))

    else:
        player.direction = input("where to?")
   # Sets the new direction before running the loop again.
    direction = player.direction
