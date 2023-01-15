from email.utils import collapse_rfc2231_value
import random
from re import A, I, S

""" With modification, Card and Deck classes from source: youtube.com, Python OOP Deck of Cards, Eli Byers"""

"""The class Card, creates the format for each card based on the card's suit and value and determines how each card will apear when printed."""

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show_all(self):
        print("        {}-{}".format(self.value, self.suit))

    

""" Build a deck of 52 cards of 4 suits from 2 to Ace."""

class Deck:
    def __init__(self):
        """ Initialize the attribute, cards, with an empty list for building the deck."""
        self.cards = []
        self.dict21 = {}
        self.build()

        self.col1 = []
        self.col2 = []
        self.col3 = []
        
        self.first_cut()
        self.target_column()

        self.combo = []
        self.decisions()


        
    def build(self):

        """ Append suits to number cards and royal cards."""

        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:

            for v in range(1, 11):
                self.cards.append((Card(s,v)))

            for v in ["Jack", "Queen", "King", "Ace"]:
                self.cards.append(Card(s, v))

        
        """ Use the Fisher Yates shuffling algorithm that makes sure each card has an equal likelihood of ending up in every other position.
        
        For “i in (range(len(self.cards)) minus 1 (the minus 1 is the last element that will run to zero from the last element backawards (-1 decrement)”. Running the loop would output values 51 to 1, because when accessing elements in an array, start with the length minus 1 because the index starts at 0. In this case starting at 1, by the time every other card is shuffled, the 0 index is also going to be shuffled, rather than shuffling it by itself.

        By creating a random number "r = random.randit(0,i)", the range is being passed 0 to i. However, in this case, since the run is starting to the right of the list and iterating backwards, a random index will be picked that is to the left of that. Therefore, the card at "i" must be swapped with the card at "r"."""
        
        for i in range(len(self.cards) -1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]


        """ Only 21 cards are needed for this game. Splice all cards following card 21 (index 20) in the deck. Then, to ensure the 21 cards are not shuffled and remain static convert the list into a dictionary."""

        self.cards = list(self.cards)[:21]

        self.cards_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

        for key in self.cards:
            for value in self.cards_values:
                self.dict21[key] = value
                self.cards_values.remove(value)
                break
        
        self.cards21 = list(self.dict21.keys())

        f""" The 21 cards will first be divided into three columns with seven cards each. To reorder and sub-group the dictionary, convert the dictionary keys into a list."""

        self.col1 = list(self.cards21)[:7]
        self.col2 = list(self.cards21)[7:14]
        self.col3 = list(self.cards21)[14:20+1]

    def target_column(self):
        
        self.target = input("\n\nWhich of the columns, above, is your card in? ")

        if self.target == "1":
            self.combo = self.col3 + self.col1 + self.col2

        elif self.target == "2":
            self.combo = self.col1, self.col2, self.col3

        elif self.target == "3":
            self.combo = self.col2 + self.col3 + self.col1
    
    def decisions(self):

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
        self.col2g = self.combo[18:20]

        self.col3a = self.combo[2:3]
        self.col3b = self.combo[5:6]
        self.col3c = self.combo[8:9]
        self.col3d = self.combo[11:12]
        self.col3e = self.combo[14:15]
        self.col3f = self.combo[17:18]
        self.col3g = self.combo[20:20+1]

        self.col1 = list(self.col1a + self.col1b + self.col1c + self.col1d + self.col1e + self.col1f + self.col1g)
        self.col2 = list(self.col2a + self.col2b + self.col2c + self.col2d + self.col2e + self.col2f + self.col2g)
        self.col3 = list(self.col3a + self.col3b + self.col3c + self.col3d + self.col3e + self.col3f + self.col3g)

        self.guess = self.combo[10:11]

    def show_dict21(self):
        for c in self.cards21:
            c.show_all()
    
    def show_col1(self):
        for c in self.col1:
            c.show_all()

    def show_col2(self):
        for c in self.col2:
            c.show_all()

    def show_col3(self):
        for c in self.col3:
            c.show_all()

    def show_guess(self):
        for c in self.guess:
            c.show_all


    """ END OF CLASSES """


# Function for continuing or quiting game

def game_action():
    
    option = input ("Press ENTER to continue.\n")
    
    if option == "":
        return True

    elif option == "q":
        print("Thanks for playing!")
             
    elif option != "" or option != "q":
        invalid = input("Press ENTER to continue\nor enter the letter q to quit game.\n")
        if (invalid == ""):
            return True
        if (invalid == "q"):
            print("Thanks for playing!")
            quit()     
        else:
            print("You have entered two invalid entries in a row.\n")
            print("Thanks for playing!", name)
            quit()


# ----------------MAIN CODE------------------

print("_____________________________________________________")
print()
print("                THE 21 CARDS TRICK                  ")
print("______________________________________________________")

print("\nWelcome to the 21 Cards Trick.\n")

name = input("What is your name? ")

print("\nThank you", name, "for challenging the computer to guess your card.\n\n")

print("INSTRUCTIONS\n")
print("Only 21 cards are needed for this challenge.\nThey have been taken from a thoroughly shuffled, full deck of cards \n")

print(name + ", if you get get too scared to follow through with this challenge,\nyou may enter the letter q to quit this game at anytime.\n")


game_action()


cards = Deck()
cards.build()
cards.show_dict21()

print()
print(name, "choose a card from the list above.\nMemorize the card or write it down.\n")


game_action()


print("The 21 cards have been grouped into\n3 columns with 7 cards each.\n")


print("Column 1")
cards.show_col1()

print("\Column 2")
cards.show_col2()

print("\Column 3")
cards.show_col3()

i = 0
while i < 4:

    cards.target_column()
    cards.decisions()

    print("Column 1")
    cards.show_col1()

    print("\Column 2")
    cards.show_col2()

    print("\Column 3")
    cards.show_col3()

    i += 1

cards.decisions()

print("The card you picked is", str(cards.show_guess) + ".")













