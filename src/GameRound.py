class GameRound():

    def __init__(self, startingPlayer, table, shoe):
        self._pot = 0
        self._startingPlayer = startingPlayer
        self._communityCards = [None,None,None,None,None]
        self._table = table
        self._shoe = shoe

    def playerBet(self,bet,player):
        pass

    def start(self): 
        self._shoe.shuffleShoe()
        for player in self._table.getPlayers(): # clears players hand and adds new cards
            player.clearHand()
            for x in range(2):
                player.addCard(self._shoe.pop())
            player.setGameRound(self) #allows for interaction between this game round and each player.

        self.roundOne()
    
    def roundOne(self):
        for card in range(3):
            self._communityCards()[card] = self._shoe.pop()
        