from __future__ import annotations
from typing import TYPE_CHECKING
from enum import Enum

import random

if TYPE_CHECKING:
    from typing import Optional


class Board(Enum):
    FLOP = "Flop"
    TURN = "Turn"
    RIVER = "River"

    # self.board = board
        # for round in [Board.FLOP, Board.TURN, Board.RIVER]:
        #     self.board.append(random.choice(self.cards))
        # for round in ["Flop", "Turn", "River"]:
        #     self.board.append(random.choice(self.cards))\

a = 10
b = 10

class Player:

    def __init__(self, hand: Hand, name: Optional[str] = None, stack: int = 1000):
        self.name = name or input("Player name: ")
        print(self.name, type(self.name))
        self.stack = stack
        self.hand = hand


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self ):
        self.cards = []
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for rank in range(2, 15):
                self.cards.append(Card(suit, rank))
       


class Hand:
    def __init__(self, deck: Deck):
        self.cards = random.choices(deck.cards, k=2)

    def add_card(self, card):
        self.cards.append(card)

    def __repr__(self):
        return ", ".join([repr(card) for card in self.cards])


def start_game():
    deck = Deck()
    player = Player(Hand(deck))
    print(player.hand)


class Game:
    def __init__(self, players, deck, board = ):
        self.