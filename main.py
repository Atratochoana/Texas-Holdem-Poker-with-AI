from src import Table
from src import CardManagement
# import Visual

# Table = Table.Table(CardManagement.Shoe(1))
# GUI = Visual.Visuals(Table)

# Table.startRound()

shoe = CardManagement.Shoe(3)
shoe.shuffleShoe()
shoe.pop()
print(len(shoe._shoe))
print(shoe._usedCards)

# to do -make actually functions for the game - add more configuration
