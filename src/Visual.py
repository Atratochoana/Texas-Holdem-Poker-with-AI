import customtkinter as ctk
from PIL import ImageTk, Image
import os


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class Visuals(ctk.CTk):

    def __init__(self, table):
        super().__init__()
        self._player = None
        self._testMode = False
        self.table = table
        self.title("Poker")
        self.geometry("1440x810")

        self.settingsButton = settingsButton(self, text="settings")
        self.settingsButton.grid(row=0,
                                 column=0,
                                 padx=10,
                                 pady=(10, 0),
                                 sticky="sw")

        self.actionBarFrame = ctk.CTkFrame(self, width=360)
        self.actionBarFrame.grid(row=3,
                                 column=1,
                                 columnspan=2,
                                 padx=100,
                                 pady=(20, 10),
                                 sticky="s")
        self.foldButton = ctk.CTkButton(self.actionBarFrame,
                                        text="FOLD",
                                        command=self.foldCallBack)
        self.foldButton.grid(row=0, column=0, pady=(10, 0), sticky="")
        self.betButton = ctk.CTkButton(self.actionBarFrame,
                                       text="BET",
                                       command=self.betCallBack)
        self.betButton.grid(row=0, column=1, pady=(10, 0), sticky="")
        self.checkButton = ctk.CTkButton(self.actionBarFrame,
                                         text="CHECK",
                                         command=self.checkCallBack)
        self.checkButton.grid(row=0, column=2, pady=(10, 0), sticky="")
        self.entry = ctk.CTkEntry(self.actionBarFrame,
                                  placeholder_text="Bet amount")
        self.entry.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="sw")
        self.cardImages = cardImages(self)
        self.cardImages.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="sw")

    def enterPlayer(self):
        pass

    def betCallBack(self):
        self.table.getPlayers()[0].placeBet(self.entry.get(), 0)

    def foldCallBack(self):
        self.table.getPlayers()[0].fold()

    def checkCallBack(self):
        self.table.getPlayers()[0].check()


class settingsButton(ctk.CTkButton):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

    def callBack(self):
        print("worked")

class cardImages(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        card1img = ImageTk.PhotoImage(Image.open("src\Assets\Cards\card_back.png"))
        card1 = ctk.CTkLabel(self,image=card1img)
        card1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="sw")


class actionBar(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        pass
