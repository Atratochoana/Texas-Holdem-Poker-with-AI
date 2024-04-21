from src import AI


class GameRound():

    def __init__(self, startingPlayer, table, shoe):
        self._pot = 0
        self._startingPlayer = startingPlayer
        self._communityCards = [None, None, None, None, None]
        self._table = table
        self._shoe = shoe
        self.nextPlayer = startingPlayer
        self.playersOut = []
        self.lastBet = 0
        self.started = False

    def playerAction(self, bet, player):
        AI.evaluateHand(self._communityCards, player)
        if player != self._table._players[
                self.nextPlayer] or player in self.playersOut:
            return

        cards = [player._hand[0], player._hand[1]]
        for card in self._communityCards:
            if card is not None:
                cards.append(card)

        if bet == False:
            self.playersOut.append(player)
            if len(self.playersOut) == (len(self._table._players) - 1):
                self.calcWinner()
        else:
            self._pot += bet
            self.lastBet = bet

        lastPlayer = self._table._numPlayers - 1  #index of last player
        while self._table._players[lastPlayer] in self.playersOut:
            lastPlayer -= 1
            if lastPlayer == 0:
                break

        if self._communityCards[4] != None and self.nextPlayer == lastPlayer:
            self.calcWinner()
            return

        if (self.nextPlayer + 1) >= self._table._numPlayers:
            self.dealCommunity()
            self.nextPlayer = 0
        else:
            self.nextPlayer += 1
            AI.playAction(self,self._table._players[self.nextPlayer])

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
        self.started = True
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
        else:
            self.calcWinner()

    def dealFlop(self):
        for card in range(3):
            self._communityCards[card] = self._shoe.pop()

    def dealTurn(self):
        self._communityCards[3] = self._shoe.pop()
        self._table._visuals.cardImages.upd6(self._communityCards[3]._suit,
                                             self._communityCards[3]._value)

    def dealRiver(self):
        self._communityCards[4] = self._shoe.pop()
        self._table._visuals.cardImages.upd7(self._communityCards[4]._suit,
                                             self._communityCards[4]._value)

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
                if card != None and card not in allCards:
                    allCards.append(card)
                else:
                    index = self._communityCards.index(card)
                    self.finishCommunity()
                    allCards.append(self._communityCards[index])
            allCards.sort(key=lambda x: x._value, reverse=True)
            player.handVal = self.handVal(allCards)
        winner = []
        for player in self._table._players:
            if player in self.playersOut:
                continue
            if winner == []:
                winner = [player]
                continue
            for key in winner[0].handVal:
                value = winner[0].handVal[key]
                if value == []:
                    continue
                if value == player.handVal[key]:
                    winner.append(player)
                    continue
                if value <= player.handVal[key]:
                    winner = [player]
                    continue

        self._table._visuals.endRound(winner)
        for player in winner:
            player._balance = player._balance + (self._pot / len(winner))
        return winner

    def handVal(
        self, hand
    ):  #will return dict with highest value of respective kind, list for incase multiple of it
        handVal = {
            "RF":
            [],  # false cos it can only be true or false still in list for ease
            "SF": [],  #can only be one but gonna keep it as list for ease
            "4OfKind": [],
            "FullHouse": [],
            "Flush": [],
            "Straight": [],
            "ThreeOfKind": [],
            "TwoPair": [],
            "Pair": [],
            "High": [],
        }
        if self.checkRoyal(hand, 0):
            handVal["RF"] = [14]
            return handVal
        House = self.checkHouse(hand)
        if House != False:
            handVal["FullHouse"] = [House[0], House[1]]
        sFlush = self.checkStraightFlush(hand)
        if sFlush != False:
            handVal["SF"] = [sFlush]
        FourKind = self.checkFour(hand)
        if FourKind != False:
            handVal["4OfKind"] = [FourKind]
        Flush = self.checkFlush(hand)
        if Flush != False:
            handVal["Flush"] = [Flush]
        Straight = self.checkStraight(hand)
        if Straight != False:
            handVal["Straight"] = hand[Straight[0]]._value
        Three = self.checkThree(hand)
        if Three != False:
            for x in range(len(Three)):
                handVal["ThreeOfKind"].append(hand[Three[x]]._value)
        Pair = self.checkTwo(hand)
        for index in Pair:
            handVal["Pair"].append(hand[index]._value)
        if len(Pair) >= 2:
            handVal["TwoPair"] = [hand[Pair[0]]._value, hand[Pair[1]]._value]

        for x in range(len(hand) - 2):
            handVal["High"].append(hand[x]._value)

        return handVal

    def checkRoyal(
            self, list,
            startingIndex):  #checks for royal flush returns true or false
        cVal = 14
        suit = list[startingIndex]._suit
        for card in range(startingIndex, startingIndex + 5):
            if list[card]._value != cVal or list[card]._suit != suit:
                return False
            cVal -= 1
        return True

    def checkStraightFlush(self, list):
        sequenceCards = self.checkStraight(list)
        if sequenceCards == False:
            return False
        for card in range(sequenceCards[0], sequenceCards[0] + 5):
            if list[card]._suit != list[card + 1]._suit:
                return False
        return list[sequenceCards[0]]._value

    def checkFour(self, list):
        four = False
        for card in range(0, len(list) - 4):
            for x in range(4):
                if x == 3:
                    four = list[card]._value
                    break
                if list[card + x]._value != list[card + x + 1]._value:
                    break
        return four

    def checkHouse(self, list):
        three = self.checkThree(list)
        two = self.checkTwo(list)
        Highest = [0, 0]
        if len(two) < 2 or len(three) < 1:
            return False

        for index in two:
            if index not in three and list[index]._value != list[
                    three[0]]._value:
                Highest[1] = list[index]._value
                Highest[0] = list[three[0]]._value
                return Highest
        if len(three) >= 2:
            if list[three[0]]._value != list[three[1]]._value:
                Highest[0] = list[three[0]]._value
                Highest[1] = list[three[1]]._value
                return Highest
        return False

    def checkFlush(
        self, list
    ):  #checks for flush and returns either false = nada or value of highest card in flush
        for index in range(len(list) - 4):
            count = 0
            for x in range(5):
                if list[index]._suit != list[index + x]._suit:
                    continue
                else:
                    count += 1
                if count == 5:
                    return list[index]._value
        return False

    def checkStraight(
        self, list
    ):  #checks for straight returns either index of first or false // doesnt factor in ace for 1 or 14 yet
        straightCards = []
        for x in range(0, len(list) - 5):
            count = 0
            end = False
            while list[x + count]._value - 1 == list[
                    x + 1 + count]._value and end == False:
                count += 1
                if count == 4:
                    end = True
                    straightCards.append(x)
                if len(list) <= x + 1 + count:
                    end = True

        if len(straightCards) == 0:
            return False
        else:
            return straightCards

    def checkThree(self, list):
        three = []
        for card in range(0, len(list) - 2):
            for x in range(3):
                if x == 2:
                    three.append(card)
                    break
                if list[card + x]._value != list[card + x + 1]._value:
                    break
        return three

    def checkTwo(self, list):
        two = []
        for card in range(0, len(list) - 1):
            for x in range(2):
                if x == 1:
                    two.append(card)
                    break
                if list[card + x]._value != list[card + x + 1]._value:
                    break
        return two
