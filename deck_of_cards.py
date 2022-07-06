import random
from PIL import Image


# create a deck of cards.
# multi-decks can be used supply by passing the constructor a number of decks
class DeckOfCards:
    def __init__(self, decks=1, jokers=False, ace_high=True):
        self.deck = []
        self.include_jokers = jokers
        self.ace_high = ace_high
        self.new_deck(decks)

    class Card:
        def __init__(self, suit, rank, color, rank_name):
            self.suit = suit
            self.rank = rank
            self.rank_name = rank_name
            self.color = color
            if suit == 'joker':
                self.image = Image.open(f'deck/{self.color}_joker.png')
            elif rank == 1:
                self.image = Image.open(f'deck/ace_of_{self.suit}.png')
            elif rank < 11:
                self.image = Image.open(f'deck/{self.rank}_of_{self.suit}.png')
            else:
                self.image = Image.open(f'deck/{self.rank_name}_of_{self.suit}.png')

    def shuffle(self):
        random.shuffle(self.deck)

    def hit_single(self):
        return self.deck.pop()

    def hit_multi(self, number=2):
        return_list = []
        for i in range(number):
            return_list.append(self.hit_single())

        return return_list

    def new_deck(self, decks=1):
        self.deck.clear()
        for i in range(decks):

            # jokers
            if self.include_jokers:
                self.deck.append(self.Card('joker', 0, 'red', 'joker'))
                self.deck.append(self.Card('joker', 0, 'black', 'joker'))

            # Hearts
            self.deck.append(self.Card('hearts', 2, 'red', 'two'))
            self.deck.append(self.Card('hearts', 3, 'red', 'three'))
            self.deck.append(self.Card('hearts', 4, 'red', 'four'))
            self.deck.append(self.Card('hearts', 5, 'red', 'five'))
            self.deck.append(self.Card('hearts', 6, 'red', 'six'))
            self.deck.append(self.Card('hearts', 7, 'red', 'seven'))
            self.deck.append(self.Card('hearts', 8, 'red', 'eight'))
            self.deck.append(self.Card('hearts', 9, 'red', 'nine'))
            self.deck.append(self.Card('hearts', 10, 'red', 'ten'))
            self.deck.append(self.Card('hearts', 11, 'red', 'jack'))
            self.deck.append(self.Card('hearts', 12, 'red', 'queen'))
            self.deck.append(self.Card('hearts', 13, 'red', 'king'))
            r = 14 if self.ace_high else 1
            self.deck.append(self.Card('hearts', r, 'red', 'ace'))

            # diamonds
            self.deck.append(self.Card('diamonds', 2, 'red', 'two'))
            self.deck.append(self.Card('diamonds', 3, 'red', 'three'))
            self.deck.append(self.Card('diamonds', 4, 'red', 'four'))
            self.deck.append(self.Card('diamonds', 5, 'red', 'five'))
            self.deck.append(self.Card('diamonds', 6, 'red', 'six'))
            self.deck.append(self.Card('diamonds', 7, 'red', 'seven'))
            self.deck.append(self.Card('diamonds', 8, 'red', 'eight'))
            self.deck.append(self.Card('diamonds', 9, 'red', 'nine'))
            self.deck.append(self.Card('diamonds', 10, 'red', 'ten'))
            self.deck.append(self.Card('diamonds', 11, 'red', 'jack'))
            self.deck.append(self.Card('diamonds', 12, 'red', 'queen'))
            self.deck.append(self.Card('diamonds', 13, 'red', 'king'))
            r = 14 if self.ace_high else 1
            self.deck.append(self.Card('diamonds', r, 'red', 'ace'))

            # Clubs
            self.deck.append(self.Card('clubs', 2, 'black', 'two'))
            self.deck.append(self.Card('clubs', 3, 'black', 'three'))
            self.deck.append(self.Card('clubs', 4, 'black', 'four'))
            self.deck.append(self.Card('clubs', 5, 'black', 'five'))
            self.deck.append(self.Card('clubs', 6, 'black', 'six'))
            self.deck.append(self.Card('clubs', 7, 'black', 'seven'))
            self.deck.append(self.Card('clubs', 8, 'black', 'eight'))
            self.deck.append(self.Card('clubs', 9, 'black', 'nine'))
            self.deck.append(self.Card('clubs', 10, 'black', 'ten'))
            self.deck.append(self.Card('clubs', 11, 'black', 'jack'))
            self.deck.append(self.Card('clubs', 12, 'black', 'queen'))
            self.deck.append(self.Card('clubs', 13, 'black', 'king'))
            r = 14 if self.ace_high else 1
            self.deck.append(self.Card('clubs', r, 'black', 'ace'))

            # Spades
            self.deck.append(self.Card('spades', 2, 'black', 'two'))
            self.deck.append(self.Card('spades', 3, 'black', 'three'))
            self.deck.append(self.Card('spades', 4, 'black', 'four'))
            self.deck.append(self.Card('spades', 5, 'black', 'five'))
            self.deck.append(self.Card('spades', 6, 'black', 'six'))
            self.deck.append(self.Card('spades', 7, 'black', 'seven'))
            self.deck.append(self.Card('spades', 8, 'black', 'eight'))
            self.deck.append(self.Card('spades', 9, 'black', 'nine'))
            self.deck.append(self.Card('spades', 10, 'black', 'ten'))
            self.deck.append(self.Card('spades', 11, 'black', 'jack'))
            self.deck.append(self.Card('spades', 12, 'black', 'queen'))
            self.deck.append(self.Card('spades', 13, 'black', 'king'))
            r = 14 if self.ace_high else 1
            self.deck.append(self.Card('spades', r, 'black', 'ace'))


d = DeckOfCards(jokers=True, decks=1, ace_high=False)

print(len(d.deck))

for i in range(54):
    card = d.hit_single()
    print(f'{card.rank} of {card.suit}')


print(len(d.deck))
