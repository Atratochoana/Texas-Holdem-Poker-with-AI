import customtkinter as ctk


class Visuals(ctk.CTk):

    def __init__(self, table):
        super().__init__()
        self.table = table
        self._player = None
        self._AI = None
        self._AIVisable = False
        self.title("Poker")
        self.geometry("600x500")
        self.frame = ctk.CTkFrame()

    # def enterPlayer(self):
    #     pass
