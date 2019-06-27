class Player:

    def __init__(self, name):
        self.name = name
        self.tired = False
        self.thirsty = False
        self.hungry = True
        self.rested = True
        self.inMain = True

    def drink_water():
        print("You drink a glass of nice cold water and are refreshed.  Now you can workout some more if you'd like!")
        self.thirsty = False

    def workout():
        print("You lift some weights, and feel a bit stronger because of it!  Now you are thirsty.")
        self.thirsty = True

    def snack():
        print("Yum, there's a ham and cheese sandwich prepared on the table.  You eat it with some chips.")
        self.hungry = False

    def rest():
        print("Ohh what a nice recliner there is!  You sit down, play a little Sudoku, and rest for a bit. ")
        self.rested = True
