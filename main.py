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


