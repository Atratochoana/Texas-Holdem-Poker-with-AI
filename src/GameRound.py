class GameRound():

    def __init__(self, startingPlayer, table, shoe):
        self._pot = 0
        self._startingPlayer = startingPlayer
        self._communityCards = [None, None, None, None, None]
        self._table = table
        self._shoe = shoe
        self.nextPlayer = startingPlayer
        self.playersOut = []

    def playerAction(self, bet, player):
        if player != self._table._players[
                self.nextPlayer] or player in self.playersOut:
            return

        if bet == False:
            self.playersOut.append(player)
            if len(self.playersOut) == (len(self._table._players) - 1):
                self.calcWinner()

        else:
            self._pot += bet

        if (self.nextPlayer + 1) >= self._table._numPlayers:
            self.dealCommunity()
            self.nextPlayer = 0
        else:
            self.nextPlayer += 1

        count = 0
        subCount = 0
        while self._table._players[self.nextPlayer + count] in self.playersOut:
            count += 1
            subCount += 1
            if count > self._table._numPlayers:
                self.calcWinner()
                break

            if (self.nextPlayer + count) >= self._table._numPlayers:
                self.nextPlayer = 0
                subCount = 0

    def start(self):
        self._shoe.shuffleShoe()
        for player in self._table.getPlayers(
        ):  # clears players hand and adds new cards
            player.clearHand()
            for x in range(2):
                player.addCard(self._shoe.pop())
            player.setGameRound(
                self
            )  #allows for interaction between this game round and each player.

    def dealCommunity(self):
        if self._communityCards[0] == None:
            self.dealFlop()
        elif self._communityCards[3] == None:
            self.dealTurn()
        elif self._communityCards[4] == None:
            self.dealRiver()

    def dealFlop(self):
        for card in range(3):
            self._communityCards[card] = self._shoe.pop()

    def dealTurn(self):
        self._communityCards[3] = self._shoe.pop()

    def dealRiver(self):
        self._communityCards[4] = self._shoe.pop()

    def finishCommunity(self):
        for x in range(len(self._communityCards)):
            if self._communityCards[x] == None:
                self._communityCards[x] = self._shoe.pop()

    def calcWinner(self):
        for player in self._table._players:
            if player in self.playersOut:
                continue
            allCards = player._hand
            for card in self._communityCards:
                if card != None:
                    allCards.append(card)
                else:
                    index = self._communityCards.index(card)
                    self.finishCommunity()
                    allCards.append(self._communityCards[index])
            allCards.sort(key=lambda x: x._value, reverse=True)
            for x in range(len(allCards)):
                print(allCards[x].getName(), "", allCards[x].getValue())
            self.handVal(allCards)

    def handVal(self,hand):  #will return dict
        handVal = {
            "RF": 0,
            "SF": 0,
            "4OfKind": 0,
            "FullHouse": 0,
            "Flush": 0,
            "Straight": 0,
            "ThreeOfKind": 0,
            "TwoPair": 0,
            "Pair": 0,
            "High": 0,
        }
        print(self.checkStraight(hand))
        

    def checkStraight(self,list):
        straightCards = []
        for x in range(0,len(list)-5):
            count = 0
            end = False

            while list[x + count]._value == list[x + 1 + count] and end == False:
                count += 1
                if count >= 5:
                    end = True
                    straightCards.append(x)
                if len(list) <= x + 1 + count:
                    end = True
        return straightCards