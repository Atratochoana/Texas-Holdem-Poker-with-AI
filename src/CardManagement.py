import random


class Card():

    def __init__(self, suit, value, name, deck):
        self._suit = suit
        self._value = value
        self._name = name
        self._deck = deck

    def getSuit(self):
        return self._suit

    def setSuit(self, suit):
        self._suit = suit
        return

    def getValue(self):
        return self._value

    def setValue(self, value):
        self._value = value
        return

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name
        return

    def getDeck(self):
        return self._deck

    def setDeck(self, deck):
        self._deck = deck
        return

    def setUsed(self):
        self._deck.addUsedCard(self)
        shoe = self._deck.getShoe()
        shoe.addUsedCard(self)
        return


class Deck():

    def __init__(self, makeDeck, shoe):
        self._cards = []
        self._usedCards = []
        self._shoe = shoe
        if makeDeck == True:
            self.makeDeck()

    def getCards(self):
        return self._cards

    def setCards(self, cards):
        self._cards = cards
        return

    def getUsedCards(self):
        return self._usedCards

    def setUsedCards(self, usedCards):
        self._usedCards = usedCards
        return

    def addUsedCard(self, card):
        self._usedCards.append(card)
        return

    def getShoe(self):
        return self._shoe

    def setShoe(self, shoe):
        self._shoe = shoe
        return

    def makeDeck(self):  #resets deck and recreates it
        self._cards = []
        self._usedCards = []
        suit = ["heart", "diamond", "club", "spade"]
        value = [14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        name = [
            "Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
            "Nine", "Ten", "Jack", "Queen", "King"
        ]
        for x in suit:
            count = 0
            for i in value:
                card = Card(x, i, name[count], self)
                self._cards.append(card)
                count += 1


class Shoe():

    def __init__(self, numDecks):
        self._shoe = []  #all cards that can be played
        self._decks = []  #each decks on there own should not be randomised
        self._usedCards = []  #all of the used cards
        for x in range(numDecks):
            self.createDeck()

    def getShoe(self):
        return self._shoe

    def setShoe(self, shoe):
        self._shoe = shoe
        return

    def getDecks(self):
        return self._decks

    def setDecks(self, decks):
        self._decks = decks
        return

    def addUsedCard(self, card):
        self._usedCards.append(card)
        return

    def getUsedCards(self):
        return self._usedCards

    def setUsedCards(self, cards):
        self._usedCards = cards

    def addDeck(self, deck):  #deck has to be a object of cards
        self._decks.append(deck)
        for card in deck.getCards():
            self._shoe.append(card)

    def createDeck(self):
        self.addDeck(Deck(True, self))

    def shuffleShoe(self):
        random.shuffle(self._shoe)

    def pop(self):
        card = self.getShoe().pop(0)
        card.setUsed()
        return card
