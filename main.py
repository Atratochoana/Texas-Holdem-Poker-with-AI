from src import Table
from src import CardManagement
from src import Visual
from src import AI
from src import Player
from src import GameRound

Shoe = CardManagement.Shoe(3)
#Table = Table.Table(3)
#GameRound = GameRound.GameRound(0, None, Shoe)

player = Player.Player(
    "Test",
    1500,
    GameRound,
)
player._hand = [
    CardManagement.Card("heart", 12, "test", None),
    CardManagement.Card("heart", 13, "test", None)
]
communityCard = [
    CardManagement.Card("heart", 12, "test", None),
    CardManagement.Card("heart", 9, "test", None),
    CardManagement.Card("heart", 9, "test", None)
]

Table = Table.Table(1)
Table.createPlayer("self")

#AI.evaluateHand(communityCard, player)
#AI.playAction(GameRound,player)

GUI = Visual.Visuals(Table)
GUI.attributes("-fullscreen", False)
GUI.mainloop()
