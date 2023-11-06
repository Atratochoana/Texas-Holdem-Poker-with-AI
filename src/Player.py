class Player():

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self._hand = []

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name
        return

    def getBalance(self):
        return self._balance

    def setBalance(self, balance):
        self._balance = balance
        return

    def getHand(self):
        return self._hand

    def setHand(self, hand):
        self._hand = hand
        return

    def addCard(self, card):
        self._hand.append(card)
        return