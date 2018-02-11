"""
Implement a CardHand class that supports a person arranging a group of
cards in his or her hand. The simulator should represent the sequence of
cards using a single positional list ADT so that cards of the same suit are
kept together. Implement this strategy by means of four “fingers” into the
hand, one for each of the suits of hearts, clubs, spades, and diamonds,
so that adding a new card to the person’s hand or playing a correct card
from the hand can be done in constant time. The class should support the
following methods:
• add card(r, s): Add a new card with rank r and suit s to the hand.
• play(s): Remove and return a card of suit s from the player’s hand;
if there is no card of suit s, then remove and return an arbitrary card
from the hand.
• iter ( ): Iterate through all cards currently in the hand.
• all of suit(s): Iterate through all cards of suit s that are currently in
the hand.
"""
from PositionalList import PositionalList
from random import randint


class EndOfTheGame(Exception):
    pass


class CardHand:
    class Suit:
        def __init__(self, deck):
            deck.add_last(None)
            self.cursor = deck.last()
            self.deck = deck
            self.size = 0

        def add(self, r):
            self.size += 1
            self.deck.add_after(self.cursor, r)
            self.cursor = self.deck.after(self.cursor)

        def remove(self):
            if self.size > 0:
                prev = self.cursor
                self.cursor = self.deck.before(prev)
                self.size -= 1
                return self.deck.delete(prev)

        def __iter__(self):
            cursor = self.cursor
            while cursor is not None:
                yield cursor
                cursor = self.deck.before(cursor)

        def __len__(self):
            return self.size

    def __init__(self):
        self._cards = PositionalList()
        self._suits = {suit: self.Suit(self._cards) for suit in
                       'hearts clubs spades diamonds'.split()}

    def add_card(self, r, s):
        self._suits[s].add(r)

    def play(self, s):
        if len(self._suits[s]) > 0:
            return self._suits[s].play()
        else:
            not_empty = []
            for name, suit in self._suits.items():
                if len(suit) > 0:
                    not_empty.append(suit)
            if len(not_empty) > 0:
                # chose randomly
                new = not_empty[randint(0, len(not_empty) - 1)]
                what = new.remove()
                return what
            else:
                raise EndOfTheGame()

    def __iter__(self):
        for card in reversed(self._cards):
            if card is not None:
                yield card

    def all_of_suit(self, s):
        for card in self._suits[s].cursor:
            yield card


hand = CardHand()
hand.add_card(2, 'hearts')
hand.add_card(3, 'hearts')
hand.add_card(4, 'hearts')
print(hand.play('spades'))
