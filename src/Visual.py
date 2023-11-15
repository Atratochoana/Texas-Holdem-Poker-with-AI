import customtkinter as ctk


class Visuals(ctk.CTk):

    def __init__(self):
        super().__init__()
        self._player = None
        self._players = []
        self._testMode = False
        self.title("Poker")
        self.geometry("600x500")
        self.frame = ctk.CTkFrame()

    def enterPlayer(self):
        pass
