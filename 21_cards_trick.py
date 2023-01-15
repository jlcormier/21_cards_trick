import random

def intro():

    print("________________________________________________")
    print()
    print("               THE 21 CARDS TRICK               ")
    print("________________________________________________")

    print("\nWelcome to the 21 Cards Trick.\n")

    name = input("What is your name? ")

    print("\nThank you",  name, "for challenging the computer to guess your card.")
    print("You may enter the letter q to quit this game at anytime.\n")

    continue_options()

    print("INSTRUCTIONS:\n")

    print("Only 21 cards are needed for this challenge.\nThey have been taken from a shuffled full deck of cards.\n")

    print("You will pick a single card from the 21 cards.\nThe computer will then divide the cards into 3 columns, \nwith 7 cards in each column, and ask you which column\nyour card is in. This will repeat two more times\nand the computer will guess your card.\n")

    print("Let's get started", name +"!\n")

    continue_options()

    return name


"""The following function allows the user to either continue or quit the program."""

def continue_options():

    while True:

        option = input ("Press ENTER to continue or q to quit.\n")

        if option == "":
            return

        elif option == "q":
            print("Thanks for playing", name + "!")
            quit()

        else:
            print("Invalid entry.")


""" INHERATANCE CLASSES"""

""" Two inhertance classes are used to build a deck of 52 cards with 4 suits from 2 to Ace.
    The parent class, Card-face, provides the value and suit attributes along with print format(what each card will look).

    The child class, Deck, inherits the value and suit attributes and uses the attributes to build the card range (suits and values) and appends a suit to each value, which is passed back to the parent class to print.

    The Deck class also serves as a parent class to the Trick class, which provides the trick's setup."""

class Card_face:
    def __init__(self, suit, value):

        self.suit = suit
        self.value = value

    def show_all(self):
        print("        {}-{}".format(self.value, self.suit))


class Deck:
    def __init__(self):

        """ Initialize the attributes that will be used in the classes."""
        self.cards = []
        self.build_deck()
        self.dict21 = {}
        self.cards21 = []
        self.col1 = []
        self.col2 = []
        self.col3 = []
        self.cards_21()


    def build_deck(self):

        """ Append suits to numbers and royals."""

        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:

            for value in range(2, 11):
                self.cards.append((Card_face(suit,value)))

            for value in ["Jack", "Queen", "King", "Ace"]:
                self.cards.append(Card_face(suit, value))


    def cards_21(self):

        """ Only 21 cards are needed for this trick. This method splices the cards list and retains the first 21 elements of the list."""

        random.shuffle(self.cards)
        self.cards = list(self.cards)[:21]

        """To ensure the cards are not shuffled with each iteration of the next inherited class (Trick), the card descriptions are stored as 21 keys in a dictionary that are retrieval by numbers ranging 0 to 21."""

        self.cards_values = list(range(0,21))

        for key in self.cards:
            for value in self.cards_values:
                self.dict21[key] = value
                self.cards_values.remove(value)
                break

        self.cards21 = list(self.dict21.keys())

        """ The cards21 list is spliced in three different sections to provide an output of three columns with seven cards in each column each."""

        self.col1 = self.cards21[0:7]
        self.col2 = self.cards21[7:14]
        self.col3 = self.cards21[14:20+1]

        """To print the suit and values together, the show_all method in the Card_face class must be called."""

        print()
        print("________________________________________________")
        print()
        print("            PICK A CARD, ANY CARD!            ")
        print("________________________________________________")
        print()

        for c in self.cards21:
            c.show_all()

        print()
        print("Choose and remember one of the cards above.")
        continue_options()


""" The class, Trick, provides the run order, algorithm, and user questions required to execute this card trick and find the target card."""

class Trick(Deck):
    def __init__(self):
        super().__init__()


        self.combo = []
        self.guess = []



    def algorithm(self):

        """The algorithm must execute three times, with the reorganized lists at the end of the loop being used for the next iternation. However, before the algorithm runs for the first time, the list of 21 cards must be printed and then divided into seven columns."""


        self.show_columns()
        self.target = input("Which of the above columns is your card in? ")
        i = 1
        while i < 3:

            while True:

                if self.target == "1":
                    self.combo = self.col3 + self.col1 + self.col2
                    break

                elif self.target == "2":
                    self.combo = self.col1 + self.col2 + self.col3
                    break

                elif self.target == "3":
                    self.combo = self.col2 + self.col3 + self.col1
                    break

                elif self.target == "q":
                    print("Thanks for playing!")
                    quit()

                else:
                    print("Invalid entry.")
                    self.target = input("\n\nWhich of the above columns is your card in? ")
                    continue

            self.col1a = self.combo[0:1]
            self.col1b = self.combo[3:4]
            self.col1c = self.combo[6:7]
            self.col1d = self.combo[9:10]
            self.col1e = self.combo[12:13]
            self.col1f = self.combo[15:16]
            self.col1g = self.combo[18:19]

            self.col2a = self.combo[1:2]
            self.col2b = self.combo[4:5]
            self.col2c = self.combo[7:8]
            self.col2d = self.combo[10:11]
            self.col2e = self.combo[13:14]
            self.col2f = self.combo[16:17]
            self.col2g = self.combo[19:20]

            self.col3a = self.combo[2:3]
            self.col3b = self.combo[5:6]
            self.col3c = self.combo[8:9]
            self.col3d = self.combo[11:12]
            self.col3e = self.combo[14:15]
            self.col3f = self.combo[17:18]
            self.col3g = self.combo[20:20+1]

            self.col1 = self.col1a + self.col1b + self.col1c + self.col1d + self.col1e + self.col1f + self.col1g
            self.col2 = self.col2a + self.col2b + self.col2c + self.col2d + self.col2e + self.col2f + self.col2g
            self.col3 = self.col3a + self.col3b + self.col3c + self.col3d + self.col3e + self.col3f + self.col3g

            self.show_columns()
            i += 1
            self.target = input("Which of the above columns is your card in? ")

        """ For the last iteration, the target question is used in a different boolean function to identify and print the target card. """

        self.guess_card()


    def guess_card(self):

        while True:

            if self.target == "1":
                self.guess = self.col1d
                break
            elif self.target == "2":
                self.guess = self.col2d
                break
            elif self.target == "3":
                self.guess = self.col3d
                break
            elif self.target == "q":
                print("Thanks for playing", name + "!")
                quit()
            else:
                print("Invalid entry.")
                continue

        print("\n" + name + ", are you ready for the computer to reveal your card?")
        continue_options()

        print("The card you picked is:\n")

        for c in self.guess:
            c.show_all()

        choice = input("\nIs this the card you picked?  1) yes  2) no  ").lower()

        if choice == "1" or choice == "1)" or choice == "yes":

            print("\nHooray !!\n")

            return

        else:

            if choice == "2" or choice == "2)" or choice == "no":

                print("\nNow wait a minute", name + ". The computer does not make mistakes.\nYou either have fat fingers or your memory is slipping.\n")
                print("Maybe try writing your card down next time.\n")
                play_again()

    def show_columns(self):

        print("\n\nColumn 1")
        for c in self.col1:
            c.show_all()

        print("\nColumn 2")
        for c in self.col2:
            c.show_all()

        print("\nColumn 3")
        for c in self.col3:
            c.show_all()

        print()


"""    END OF INHERITANCE CLASSES
   ----------------------------------"""

"""The retry input question in the class Trick, method guess_card, calls the following function. This function soley serves as a way to direct the program to the driver code, so  the introduction part of the game is not replayed."""

def play_again():
    return

name = intro()

while True:

    """--- DRIVER CODE ---"""

    cards = Trick()
    cards.algorithm()

    again = input("\nWould you like to see this card trick again?  1) yes  2) no  ")

    if again == "1":
        continue
    else:
        while True:
            if again == "2" or again == "q":
                print("\nThanks for playing", name +"!")
                quit()
            else:
                print("Invalid entry.")
                continue