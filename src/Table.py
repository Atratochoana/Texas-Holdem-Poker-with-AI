import json
from .GameRound import GameRound


class Table():

    def __init__(self, Shoe):
        self._players = []
        self._numPlayers = len(self._players)
        self._shoe = Shoe
        self._defaultBal = None  #will be changed instantly based on config file
        self._minimumBet = None
        self.setupConfig()
        self._startingPlayer = 0

    def getPlayers(self):
        return self._players

    def setPlayers(self, players):
        self._players = players
        return

    def addPlayer(
        self, player
    ):  #cant autocreate due to them needing paramenters that cannot be autocreated
        self._players.append(player)
        self._numPlayers += 1
        return

    def getNumPlayers(self):
        return self._numPlayers

    def setNumPlayers(self, numPlayers):
        self._numPlayers = numPlayers
        return

    def getShoe(self):
        return self._shoe

    def setShoe(self, shoe):
        self._shoe = shoe
        return

    def setDefaultBal(self, bal):
        self._defaultBal = bal
        return

    def getDefaultBal(self):
        return self._defaultBal

    def getMinBet(self):
        return self._minimumBet

    def setMinBet(self, bet):
        self._minimumBet = bet
        return

    def rotateStartingPlayer(self):
        if self._startingPlayer + 1 <= self._numPlayers:
            self._startingPlayer += 1
        else:
            self._startingPlayer = 0

    def setupConfig(self):
        with open("Config.json", "r") as f:
            config = json.load(f)
        self.setDefaultBal(config['startingMoney'])
        self.setMinBet(config["minimumBet"])

    def startRound(self):
        gameRound = GameRound(None, self, self.getShoe())
        gameRound.start()
        self.rotateStartingPlayer()
