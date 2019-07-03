class Player:

    def __init__(self, name):
        self.name = name
        self.tired = False
        self.thirsty = False
        self.hungry = True
        self.inMain = True
        self.direction = "JUST ENTERED..."


    def enter_room_1(self):
        print("\nYou're back in the mainroom!  Type 'Goodbye' if you're ready to leave,\n ")
        print("Or continue exploring.")
        self.direction = input("You can go to the restroom(2), the kitchen(4), or the workout room(6).\n  Where to?\n: ")


    def enter_room_2(self):
        print("\nYou washed up in the restroom.  What a nice smelling soap this house has!")
        self.inMain = False
        print("Now you can go to the living room(3) or back to the mainroom(1).")
        if self.thirsty == True:
            print("You took a sip from a dixie cup and are refreshed.  You are able to workout some more.")
            self.thirsty == False
            self.direction = input("Where to next?  You can go to the mainroom(1) or the livingroom(3)\n: ")
            return
        self.direction = input("Where to next?\n: ")


    def enter_room_3(self):
        print("\nYou're in the livingroom.  It's really nice with great furniture and tall drapes.\n")
        print("The sunshine is really streaming in through that window!\n")
        if self.tired == True:
            print("Ohh what a nice recliner there is!  You sit down, play a little Sudoku, and rest for a bit.")
            print("Whoa, where did the time go??  You dozed off for a minute!  A bite to eat seems to be in order now.")
            print("Where's that diningroom?")
            self.tired = False
            self.hungry = True
            self.direction = input("Where to next?  You can go to the bathroom(2) or the kitchen(4)\n: ")
            return
        self.direction = input("Head to the kitchen(4), or back to the restroom(2).\n: ")


    def enter_room_4(self):
        print("\nYou're in the Kitchen!  This is a nice area with marble countertops and recently updated cabinets.")

        if self.thirsty == True:
            print("You drink a glass of nice cold water and are refreshed.  ")
            self.direction = input("Where to next?  You can go to the mainroom(1), the livingroom(3), or the diningroom(5)\n: ")
            return
        print("You're satisfied so no need for a drink of water for ya now.")
        self.direction = input("Head to the livingroom(3), the diningroom(5), or back to the mainroom(1).\n: ")


    def enter_room_5(self):
        if self.hungry == True:
            print("MMM there's freshly cooked ham on a platter for you to enjoy.")
            print("You grab a slice, and a piece of the pineapple that's on it too.  Mmm mm, that was satisfying!")
            self.hungry = False
            self.direction = input("You can go to the Workoutroom(6) or the kitchen(4) from here.\n:  ")
            return
        print("You're not hungry, but maybe in a bit you can have a piece!")
        self.direction = input("Workoutroom(6), kitchen(4)\n:  ")


    def enter_room_6(self):
        print("You enter the workout room.")
        if self.tired == True:
            print("\nYou're too tired to lift and run, after you rest you should be good to go though!")
            print("A nice chair to sink into should do the trick.")
            self.direction = input("You can go to the Diningroom(5) or the mainroom(1) from here.\n:  ")
            return
        if self.hungry == True:
            print("\nMm, you need a snack for some strength before you hit the iron.")
            print("Try and look around for something to munch on.")
            self.direction = input("You can go to the Diningroom(5) or the mainroom(1) from here.\n:  ")
            return
        if self.thirsty == True:
            print("\nHere's the workout room, but ahh, you're parched and there's no watertank in here!")
            print("You need a refreshment before you get going with any workouts.")
            print("Try searching some other rooms for something to help with that")
            self.direction = input("You can go to the Diningroom(5) or the mainroom(1) from here.\n:  ")
            return
        print("\nYou're in the exercise room now.  Look at you go!\n")
        print("Whoa, did you stretch?  Alright, alright!  You are really doing a great job.")
        print("  That definately tired you out.  You could use something to drink, and maybe a snack too")
        print("if you want to workout some more.  The kitchen might be a good place make your way to.")
        self.tired = True
        self.hungry = True
        self.thirsty = True
        self.direction = input("You can go to the Diningroom(5) or the mainroom(1) from here.\n:  ")
