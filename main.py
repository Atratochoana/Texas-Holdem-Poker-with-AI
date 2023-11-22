from src import Table

# from src import Visual

Table = Table.Table(1)
Table.createPlayer("Ralph")
Table.createPlayer("Test")
Table.createPlayer("Gabby")
Table.createPlayer("Palak")

# GUI = Visual.Visuals()

Table.startRound()


Table.getPlayers()[0].placeBet(50, 80)
print(Table.getPlayers()[0]._balance)

# to do -make actually functions for the game - add more configuration
