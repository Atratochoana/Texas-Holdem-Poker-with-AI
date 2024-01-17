import customtkinter as ctk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Visuals(ctk.CTk):

    def __init__(self,table):
        super().__init__()
        self._player = None
        self._testMode = False
        self.table = table
        self.title("Poker")
        self.geometry("1440x810")

        self.settingsButton = settingsButton(self,text="settings")
        self.settingsButton.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="sw")
        
        self.actionBarFrame = ctk.CTkFrame(self,width=360)
        self.actionBarFrame.grid(row=3, column=1,columnspan=2, padx=100, pady=(20, 10), sticky="s")
        self.foldButton = ctk.CTkButton(self.actionBarFrame,text="bet")
        self.foldButton.grid(row=0, column=0, pady=(10, 0), sticky="")
        self.betButton = ctk.CTkButton(self.actionBarFrame,text="check")
        self.betButton.grid(row=0, column=1, pady=(10, 0), sticky="")
        self.checkButton = ctk.CTkButton(self.actionBarFrame,text="fold")
        self.checkButton.grid(row=0, column=2, pady=(10, 0), sticky="")
        

    def enterPlayer(self):
        pass

    def betCallBack(self):
        self.table._players[0]



class settingsButton(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        

    def callBack(self):
        print("worked")





GUI = Visuals(None)
GUI.attributes("-fullscreen", False)
GUI.mainloop()