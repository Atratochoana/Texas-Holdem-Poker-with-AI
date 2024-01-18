import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class Visuals(ctk.CTk):

    def __init__(self, table):
        super().__init__()
        self._player = None
        self._gameRound = None
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
        self.cardImages.grid(row=1,
                             column=1,
                             padx=10,
                             pady=(10, 0),
                             sticky="sw")
        self.startButton = ctk.CTkButton(self,command=self.startButtonCallBack)
        self.startButton.grid(row=1,column=0,padx=10,pady=(10,0),sticky="sw")

    def enterPlayer(self):
        pass

    def betCallBack(self):
        self.table.getPlayers()[0].placeBet(self.entry.get(), 0)

    def foldCallBack(self):
        self.table.getPlayers()[0].fold()

    def checkCallBack(self):
        self.table.getPlayers()[0].check()

    def startButtonCallBack(self):
        if self._gameRound != None:
            return
        print("worked")
        gameRound = self.table.startRound()
        self._gameRound = gameRound
        return


class settingsButton(ctk.CTkButton):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

    def callBack(self):
        print("worked")


class cardImages(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        #self cards
        card1img = ctk.CTkImage(
            light_image=Image.open("src/Assets/Cards/card_back.png"),
            size=(64, 64))
        card1 = ctk.CTkLabel(self, image=card1img, text="")
        card1.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="sw")
        card2img = ctk.CTkImage(
            light_image=Image.open("src/Assets/Cards/diamond/card_diamonds_02.png"),
            size=(64, 64))
        card2 = ctk.CTkLabel(self, image=card2img, text="")
        card2.grid(row=1, column=3, padx=10, pady=(10, 0), sticky="sw")

        #community cards

        card3img = ctk.CTkImage(
            light_image=Image.open("src/Assets/Cards/card_back.png"),
            size=(64, 64))
        card3 = ctk.CTkLabel(self, image=card3img, text="")
        card3.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="sw")
        card4img = ctk.CTkImage(
            light_image=Image.open("src/Assets/Cards/card_back.png"),
            size=(64, 64))
        card4 = ctk.CTkLabel(self, image=card4img, text="")
        card4.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="sw")
        card5img = ctk.CTkImage(
            light_image=Image.open("src/Assets/Cards/card_back.png"),
            size=(64, 64))
        card5 = ctk.CTkLabel(self, image=card5img, text="")
        card5.grid(row=0, column=2, padx=10, pady=(10, 0), sticky="sw")
        card6img = ctk.CTkImage(
            light_image=Image.open("src/Assets/Cards/card_back.png"),
            size=(64, 64))
        card6 = ctk.CTkLabel(self, image=card6img, text="")
        card6.grid(row=0, column=3, padx=10, pady=(10, 0), sticky="sw")
        card7img = ctk.CTkImage(
            light_image=Image.open("src/Assets/Cards/card_back.png"),
            size=(64, 64))
        card7 = ctk.CTkLabel(self, image=card7img, text="")
        card7.grid(row=0, column=4, padx=10, pady=(10, 0), sticky="sw")


class actionBar(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        pass
