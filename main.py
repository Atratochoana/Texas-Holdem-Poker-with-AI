from src import Table
from src import CardManagement
from src import Visual

Table = Table.Table(1)
Table.createPlayer("User")
# Table.createPlayer("Mang Ye")
# Table.createPlayer("Gabby")
# Table.createPlayer("Palak")

GUI = Visual.Visuals(Table)
GUI.attributes("-fullscreen", False)
GUI.mainloop()

# gameRound = Table.startRound()

# Table.getPlayers()[0].placeBet(50, 0)
# Table.getPlayers()[1].placeBet(30, 0)
# Table.getPlayers()[2].placeBet(70, 0)
# Table.getPlayers()[0].fold()
# Table.getPlayers()[1].check()
# Table.getPlayers()[2].placeBet(100, 0)
# Table.getPlayers()[0].fold()
# Table.getPlayers()[1].placeBet(300,0)
# gameRound.calcWinner()
