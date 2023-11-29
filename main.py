from src import Table

# from src import Visual

Table = Table.Table(1)
Table.createPlayer("Ralph")
Table.createPlayer("Test")
Table.createPlayer("Gabby")
Table.createPlayer("Palak")

# GUI = Visual.Visuals()

gameRound = Table.startRound()

Table.getPlayers()[0].placeBet(50, 80)
print(gameRound.nextPlayer)
Table.getPlayers()[1].placeBet(30,50)
print(gameRound.nextPlayer)
Table.getPlayers()[2].placeBet(50,60)
print(gameRound.nextPlayer)
Table.getPlayers()[3].fold()
print(gameRound.nextPlayer)
Table.getPlayers()[0].fold()
print(gameRound.nextPlayer)
# print(gameRound.playersOut)
gameRound.calcWinner()


