# Deck-of-Cards

Copyright <2022> MIT license


Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



This is simply a deck of cards with images and some functionality.
  - Create a deck
  - New deck 
  - Multiple decks (default=1 deck)
  - Jokers (default=False)
  - Shuffle
  - Hit single card. Returns a class card
  - Hit multiple cards (default=2). Returns a list of cards
  
 card class members.
  - suits:'hearts' 'diamonds' 'clubs' 'spades'
  - rank: 0 = joker, 2-10, 11-14 for jack through ace, 1 = ace if not ace high
  - rank name: 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace', 'joker'
  - color: 'red' 'black'
  - image: Display image for card