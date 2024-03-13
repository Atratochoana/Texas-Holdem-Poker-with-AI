from src import Table
from src import CardManagement
from src import Visual
from src import AI
from src import Player
from src import GameRound

Shoe = CardManagement.Shoe(3)
GameRound = GameRound.GameRound(0,None,Shoe)

player = Player.Player(
    "Test",
    1500,
    GameRound,
)
player._hand = [
    CardManagement.Card("Heart", 14, "test", None),
    CardManagement.Card("Heart", 14, "test", None)
]
communityCard = [
    CardManagement.Card("Heart", 12, "test", None),
    CardManagement.Card("Heart", 12, "test", None),
    CardManagement.Card("Heart", 12, "test", None),
]

Table = Table.Table(1)
Table.createPlayer("self")

AI.evaluateHand(communityCard, player)

GUI = Visual.Visuals(Table)
GUI.attributes("-fullscreen", False)
GUI.mainloop()
