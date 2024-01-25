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
        self.startButton = ctk.CTkButton(self,
                                         text="start",
                                         command=self.startButtonCallBack)
        self.startButton.grid(row=1,
                              column=0,
                              padx=10,
                              pady=(10, 0),
                              sticky="sw")
        self.info = infoLabales(self)
        self.info.grid(row=2,
                       columnspan=2,
                       column=1,
                       padx=10,
                       pady=(10, 0),
                       sticky="sw")
        self.addPlayer = addPlayer(self,text="Add Player")
        self.addPlayer.grid(row=3,
                       column=0,
                       padx=10,
                       pady=(10, 0),
                       sticky="sw")


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
        gameRound = self.table.startRound()
        #starts the gameRound by running all the functions
        self._gameRound = gameRound
        self._gameRound.start()
        self._gameRound.dealCommunity()
        #update the hand card visuals
        self.cardImages.upd1(self.table._players[0]._hand[0]._suit,
                             self.table._players[0]._hand[0]._value)
        self.cardImages.upd2(self.table._players[0]._hand[1]._suit,
                             self.table._players[0]._hand[1]._value)
        #update the community cards
        self.cardImages.upd3(self._gameRound._communityCards[0]._suit,
                             self._gameRound._communityCards[0]._value)
        self.cardImages.upd4(self._gameRound._communityCards[1]._suit,
                             self._gameRound._communityCards[1]._value)
        self.cardImages.upd5(self._gameRound._communityCards[2]._suit,
                             self._gameRound._communityCards[2]._value)

        print(self._gameRound.nextPlayer)
        self.info.updBal(self.table._players[0]._balance)

        return

class infoLabales(ctk.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        self.width = 360

        self.potLabel = ctk.CTkLabel(self,text="Pot: 00000")
        self.potLabel.grid(row=0,column=0,padx=10,pady=(10,0),sticky="sw")
        self.lastBetLabel = ctk.CTkLabel(self,text="LastBet: 00000")
        self.lastBetLabel.grid(row=0,column=1,padx=10,pady=(10,0),sticky="sw")
        self.balanceLabel = ctk.CTkLabel(self,text="Balance: 00000")
        self.balanceLabel.grid(row=0,column=2,padx=10,pady=(10,0),sticky="sw")

    def updBal(self,balance):
        self.balanceLabel.configure(text=f"Balance: {balance}")

class cardImages(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        #self cards
        card1img = ctk.CTkImage(
            light_image=Image.open("src/Assets/Cards/card_back.png"),
            size=(64, 64))
        self.card1 = ctk.CTkLabel(self, image=card1img, text="")
        self.card1.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="sw")
        card2img = ctk.CTkImage(
            light_image=Image.open("src/Assets/Cards/card_back.png"),
            size=(64, 64))
        self.card2 = ctk.CTkLabel(self, image=card2img, text="")
        self.card2.grid(row=1, column=3, padx=10, pady=(10, 0), sticky="sw")

        #community cards

        card3img = ctk.CTkImage(
            light_image=Image.open("src/Assets/Cards/card_back.png"),
            size=(64, 64))
        self.card3 = ctk.CTkLabel(self, image=card3img, text="")
        self.card3.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="sw")
        card4img = ctk.CTkImage(
            light_image=Image.open("src/Assets/Cards/card_back.png"),
            size=(64, 64))
        self.card4 = ctk.CTkLabel(self, image=card4img, text="")
        self.card4.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="sw")
        card5img = ctk.CTkImage(
            light_image=Image.open("src/Assets/Cards/card_back.png"),
            size=(64, 64))
        self.card5 = ctk.CTkLabel(self, image=card5img, text="")
        self.card5.grid(row=0, column=2, padx=10, pady=(10, 0), sticky="sw")
        card6img = ctk.CTkImage(
            light_image=Image.open("src/Assets/Cards/card_back.png"),
            size=(64, 64))
        self.card6 = ctk.CTkLabel(self, image=card6img, text="")
        self.card6.grid(row=0, column=3, padx=10, pady=(10, 0), sticky="sw")
        card7img = ctk.CTkImage(
            light_image=Image.open("src/Assets/Cards/card_back.png"),
            size=(64, 64))
        self.card7 = ctk.CTkLabel(self, image=card7img, text="")
        self.card7.grid(row=0, column=4, padx=10, pady=(10, 0), sticky="sw")

    def upd1(self, suit, value):
        root = "src/Assets/Cards/" + suit + "/card_" + suit + "s_"
        if value <= 9:
            root += "0" + str(value) + ".png"
        else:
            if value == 10:
                root += str(value) + ".png"
            elif value == 11:
                root += "J" + ".png"
            elif value == 12:
                root += "Q" + ".png"
            elif value == 13:
                root += "K" + ".png"
            elif value == 14:
                root += "A" + ".png"

        self.card1.configure(
            image=ctk.CTkImage(light_image=Image.open(root), size=(64, 64)))

    def upd2(self, suit, value):
        root = "src/Assets/Cards/" + suit + "/card_" + suit + "s_"
        if value <= 9:
            root += "0" + str(value) + ".png"
        else:
            if value == 10:
                root += str(value) + ".png"
            elif value == 11:
                root += "J" + ".png"
            elif value == 12:
                root += "Q" + ".png"
            elif value == 13:
                root += "K" + ".png"
            elif value == 14:
                root += "A" + ".png"

        self.card2.configure(
            image=ctk.CTkImage(light_image=Image.open(root), size=(64, 64)))

    def upd3(self, suit, value):
        root = "src/Assets/Cards/" + suit + "/card_" + suit + "s_"
        if value <= 9:
            root += "0" + str(value) + ".png"
        else:
            if value == 10:
                root += str(value) + ".png"
            elif value == 11:
                root += "J" + ".png"
            elif value == 12:
                root += "Q" + ".png"
            elif value == 13:
                root += "K" + ".png"
            elif value == 14:
                root += "A" + ".png"

        self.card3.configure(
            image=ctk.CTkImage(light_image=Image.open(root), size=(64, 64)))

    def upd4(self, suit, value):
        root = "src/Assets/Cards/" + suit + "/card_" + suit + "s_"
        if value <= 9:
            root += "0" + str(value) + ".png"
        else:
            if value == 10:
                root += str(value) + ".png"
            elif value == 11:
                root += "J" + ".png"
            elif value == 12:
                root += "Q" + ".png"
            elif value == 13:
                root += "K" + ".png"
            elif value == 14:
                root += "A" + ".png"

        self.card4.configure(
            image=ctk.CTkImage(light_image=Image.open(root), size=(64, 64)))

    def upd5(self, suit, value):
        root = "src/Assets/Cards/" + suit + "/card_" + suit + "s_"
        if value <= 9:
            root += "0" + str(value) + ".png"
        else:
            if value == 10:
                root += str(value) + ".png"
            elif value == 11:
                root += "J" + ".png"
            elif value == 12:
                root += "Q" + ".png"
            elif value == 13:
                root += "K" + ".png"
            elif value == 14:
                root += "A" + ".png"

        self.card5.configure(
            image=ctk.CTkImage(light_image=Image.open(root), size=(64, 64)))

    def upd6(self, suit, value):
        root = "src/Assets/Cards/" + suit + "/card_" + suit + "s_"
        if value <= 9:
            root += "0" + str(value) + ".png"
        else:
            if value == 10:
                root += str(value) + ".png"
            elif value == 11:
                root += "J" + ".png"
            elif value == 12:
                root += "Q" + ".png"
            elif value == 13:
                root += "K" + ".png"
            elif value == 14:
                root += "A" + ".png"

        self.card6.configure(
            image=ctk.CTkImage(light_image=Image.open(root), size=(64, 64)))

    def upd7(self, suit, value):
        root = "src/Assets/Cards/" + suit + "/card_" + suit + "s_"
        if value <= 9:
            root += "0" + str(value) + ".png"
        else:
            if value == 10:
                root += str(value) + ".png"
            elif value == 11:
                root += "J" + ".png"
            elif value == 12:
                root += "Q" + ".png"
            elif value == 13:
                root += "K" + ".png"
            elif value == 14:
                root += "A" + ".png"

        self.card7.configure(
            image=ctk.CTkImage(light_image=Image.open(root), size=(64, 64)))

    
class addPlayer(ctk.CTkButton):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.configure(command=self.callBack)

    def callBack(self):
        dialog = ctk.CTkInputDialog(text="Enter the name of the Player",title="add Player")
        text = dialog.get_input()
        self.master.table.createPlayer(text)
        for player in self.master.table._players:
            print(player._name)


class settingsButton(ctk.CTkButton):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.configure(command=self.callBack)

    def callBack(self):
        dialog = ctk.CTkInputDialog(text="Action: int = bet, F = fold, C = check",title="cheater")
        text = dialog.get_input()
        if str(text).upper() == "F":
            self.master.table.getPlayers()[self.master._gameRound.nextPlayer].fold()
        elif str(text).upper() == "C":
            self.master.table.getPlayers()[self.master._gameRound.nextPlayer].check()
        elif str(text).upper() == "CARD":
            for card in self.master.table.getPlayers()[self.master._gameRound.nextPlayer]._hand:
                print(str(card._value) + " : " + str(card._suit))
        else:
            self.master.table.getPlayers()[self.master._gameRound.nextPlayer].placeBet(int(text),self.master._gameRound.lastBet)
            potText = self.master.info.potLabel.cget("text")
            potVal = int(potText[5:]) + int(text)
            potText = potText[:5]
            if len(str(potVal)) >= 5:
                potText += str(potVal)
            else:
                potText += "0" * (5 - len(str(potVal)))
                potText += str(potVal)
            self.master.info.potLabel.configure(text=potText)
        