from src import Table
from src import CardManagement

# from src import Visual
Table = Table.Table(1)
Table.createPlayer("Ralph")
Table.createPlayer("Mang Ye")
Table.createPlayer("Gabby")
Table.createPlayer("Palak")

# GUI = Visual.Visuals()

gameRound = Table.startRound()

Table.getPlayers()[0].placeBet(50, 0)
Table.getPlayers()[1].placeBet(30, 0)
Table.getPlayers()[2].placeBet(70, 0)
for x in range(len(Table.getPlayers()[0]._hand)):
    print(Table.getPlayers()[0]._hand[x]._value)
print(" ")
for x in range(len(Table.getPlayers()[1]._hand)):
    print(Table.getPlayers()[1]._hand[x]._value)
print(" ")
for x in range(len(Table.getPlayers()[2]._hand)):
    print(Table.getPlayers()[2]._hand[x]._value)
Table.getPlayers()[3].fold()
gameRound.finishCommunity()
print(" ")
for x in range(len(gameRound._communityCards)):
    print(gameRound._communityCards[x]._value)
gameRound.calcWinner()
Table.getPlayers()[0].fold()
Table.getPlayers()[1].check()
Table.getPlayers()[2].placeBet(100, 0)
Table.getPlayers()[0].fold()
Table.getPlayers()[1].placeBet(300,0)
# testHand = [
#     CardManagement.Card("Heart",14,"Ace",None),
#     CardManagement.Card("Heart",14,"King",None),
#     CardManagement.Card("Heart",13,"Queen",None),
#     CardManagement.Card("Heart",13,"Jack",None),
#     CardManagement.Card("Heart",13,"Ten",None),
#     CardManagement.Card("Heart",10,"Five",None),
#     CardManagement.Card("Heart",4,"Four",None),
# ]

# gameRound.handVal(testHand)
