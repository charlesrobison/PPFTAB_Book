'''
Created on Apr 24, 2016

@author: robisoc
'''
# Blackjack
# From 1 to 7 players compete against a dealer

import cards, games

class BJ_Card(cards.Card):
    """ A Blackjack Card. """
    ACE_VALUE = 1
    
    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10      
        else:
            v = None
        return v
    
class BJ_Deck(cards.Deck):
    """ A Blackjack Deck. """
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))
                
class BJ_Hand(cards.Hand):
    """ A Blackjack Hand. """
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name
        
    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep
    
    @property
    def total(self):
        # If a card in the hand has value of None, then total is None.
        for card in self.cards:
            if not card.value:
                return None
            
        # Add up card values.  Treat each Ace as 1.
        t = 0
        for card in self.cards:
            t += card.value
            
        # Determine if hand contains an Ace.
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True
                
        # If hand contains Ace and total is low enough, treat Ace as 11.
        if contains_ace and t <= 11:
            # add only 10 since we've already added 1 for the Ace
            t += 10
            
        return t
    
    def is_busted(self):
        return self.total > 21
    
class BJ_Player(BJ_Hand):
    """ A Blackjack Player."""
    def is_hitting(self):
        response = games.ask_yes_no("\n" + self.name + ", do you want a hit? (Y/N): ")
        return response == "y"
    
    def bust(self):
        print(self.name, "busts.")
        
    def lose(self):
        print(self.name, "loses.")
        
    def win(self):
        print(self.name, "wins.")
        
    def push(self):
        print(self.name, "pushes.")
        
class BJ_Dealer(BJ_Hand):
    """ A Blackjack Dealer. """
    def is_hitting(self):
        return self.total < 17
    
    def bust(self):
        print(self.name, "busts.")
        
    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()
        
        