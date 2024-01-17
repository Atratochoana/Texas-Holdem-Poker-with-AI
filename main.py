from src import Table
from src import CardManagement
from src import Visual

Table = Table.Table(1)
Table.createPlayer("Ralph")
Table.createPlayer("Mang Ye")
# Table.createPlayer("Gabby")
# Table.createPlayer("Palak")
gameRound = Table.startRound()

GUI = Visual.Visuals(Table)
GUI.attributes("-fullscreen", False)
GUI.mainloop()



# Table.getPlayers()[0].placeBet(50, 0)
# Table.getPlayers()[1].placeBet(30, 0)
# Table.getPlayers()[2].placeBet(70, 0)
# Table.getPlayers()[0].fold()
# Table.getPlayers()[1].check()
# Table.getPlayers()[2].placeBet(100, 0)
# Table.getPlayers()[0].fold()
# Table.getPlayers()[1].placeBet(300,0)
# testHand = [
#     CardManagement.Card("spades",14,"Ace",None),
#     CardManagement.Card("Heart",14,"Ace",None),
#     CardManagement.Card("Heart",14,"Ace",None),
#     CardManagement.Card("Heart",12,"Ace",None),
#     CardManagement.Card("Heart",12,"Ace",None),
#     CardManagement.Card("Heart",12,"Ace",None),
#     CardManagement.Card("Heart",9,"Ace",None),
#            ]
