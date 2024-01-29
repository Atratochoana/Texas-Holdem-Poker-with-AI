class Player():

    def __init__(self, name, balance,gameRound=None):
        self._name = name
        self._balance = balance
        self._hand = []
        self._gameRound = gameRound
        self.handVal = None

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

    def clearHand(self):
        self._hand = []

    def setGameRound(self, GameRound):
        self._gameRound = GameRound
        return

    def checkNext(self):
        next = self._gameRound.nextPlayer
        index = self._gameRound._table.getPlayers().index(self)
        if next == index:
            return True
        return False

    def placeBet(self, Bet, previousBet):
        if self.checkNext() == False:
            return False
        print(f"{self._name}: betted")
        if Bet == 0 or type(Bet) != int:
            return False

        if Bet <= self._balance and Bet >= previousBet:
            self._balance -= Bet
            self._gameRound.playerAction(Bet,self)
            return True
        else:
            return False

    def call(self, previousBet):
        if self.checkNext() == False:
            return False
        print(f"{self._name}: called")
        if self._balance <= previousBet:
            self._gameRound.playerAction(previousBet, self)
            return True
        else:
            return False

    def fold(self):
        if self.checkNext() == False:
            return False
        print(f"{self._name}: folded")
        self._gameRound.playerAction(False, self)
        return True

    def check(self):
        if self.checkNext() == False:
            return False
        print(f"{self._name}: checked")
        self._gameRound.playerAction(0, self)
        return True
