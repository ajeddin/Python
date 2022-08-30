#  BLACKJACK
# player can stand or hit, player must be able to pick how much to bet, keep track of player money, alert plater of loses,wins, busts. 
from operator import truediv
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}
playing=True
class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    def __str__(self):
        return self.rank + " of " + self.suit
class Deck:
    def __init__(self):
        self.allcards=[]
        for suit in suits:
            for rank in ranks:
                self.allcards.append(Card(suit,rank))
    def __str__(self):
        deck_comp=''
        for card in self.allcards:
            deck_comp+='\n'+ card.__str__()
        return'The Deck has: ' +deck_comp
    def shuffle(self):
         random.shuffle(self.allcards)
    def deal(self):
        singlecard=self.allcards.pop()
        return singlecard
class Hand:
    def __init__(self):
        self.cards= []
        self.value=0
        self.aces=0
    def addcard(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces +=1

    def ace(self):
        while self.value>21 and self.aces:
            self.value-=10
            self.aces-=1 
class Chip:
    def __init__(self,total=100):
        self.total= total
        self.bet=0
    def win_bet(self):
        self.total +=self.bet
    def losebet(self):
        self.total-=self.bet
        self.total-=self.bet
