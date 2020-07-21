from player import Player

class Room:

    def room1(self):
        if player.room in ("2", "4", "6"):
            print("\nYou washed up in the restroom!  What a nice smelling soap this house has!")
            player.inMain = True
            print("Now you can go to the living room(3) or back to the mainroom(1).")
            direction = input("Where to next?\n: ")
            return direction
        else:
            err()


    def room2(self):
        if player.room in ("1", "3"):
            print("\nYou washed up in the restroom.  What a nice smelling soap they have!")
            player.inMain = False
            print("Now you can go to the living room(3) or back to the mainroom(1).\n")
            direction = input("Where to next?\n: ")
            return direction
        else:
            err()


    def room3(self):
        if player.room in ("2", "4"):
            print("\nYour in the livingroom.  It's really nice with great furniture and tall drapes.\n")
            print("The sunshine is really streaming in through that window!\n")
            player.inMain = False
            direction = input("Head to the kitchen(4), or back to the restroom(2).\n: ")
            return direction
        else:
            err()





            # def err(self):
            #     print("You have to be closer to that room to enter it.")
            #     direction = input("Where to next?\n: ")
            #     return direction
