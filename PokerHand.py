from __future__ import print_function, division

from Card import Hand, Deck
"""
When you run this code, it deals seven 7-card poker hands and checks to see if any contains a flush
"""

class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False
    
    
    def rank_hist(self):
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    
    def has_pair(self):
        #returns true if the hand has a pair
        self.rank_hist()
        for val in self.ranks.values():
            print(val)
            if val == 2:
                print(val)
                return True
            return False

#    def has_twopair(self):
#        #returns true if the hand has a pair
#        self.rank_hist()
#        print(self.ranks.get(2, 0))
#            
#        for val in self.ranks.values():
#            if val == 2:
#                return True
#            return False        


if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print(hand)
        print(hand.has_flush())
        print('')
        print(hand.has_pair())

