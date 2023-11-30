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
        for card in self._communityCards:
            if card == None:
                card = self._shoe.pop()

    def calcWinner(self):
        print("worked")
        for player in self._table._players:
            if player in self.playersOut:
                continue
            allCards = player._hand
            allCards += self._communityCards
            allCards.sort()
