class TreeNode:
    """[player]: index of the player making the action
       [action]: actions taking place E.G. call,check,fold,raise
       [card]: current cards in player in list first 2 indexs of list are for hole rest community, list len dont matter"""

    def __init__(self, player, action=None, card=[]):
        self.action = action  #actions taken place
        self.player = player  #player index
        self.cards = card  #cards visible at the time of play
        self.children = []  #children connected to this action

    def addChild(self, Node):
        self.children.append(Node)

    def removeChild(self, child):
        if child in self.children:
            self.children.pop(self.children.index(child))
            return True
        else:
            return False

    def addCall(self, player, cards):
        """[player]: index of the player
           [cards]: current cards in play"""
        self.children.append(TreeNode(player, cards, action="call"))

    def addRaise(self, player, cards):
        """[player]: index of the player
           [cards]: current cards in play"""
        self.children.append(TreeNode(player, cards, action="raise"))

    def addCheck(self, player, cards):
        """[player]: index of the player
           [cards]: current cards in play"""
        self.children.append(TreeNode(player, card=cards, action="check"))

    def addFold(self, player, cards):
        """[player]: index of the player
           [cards]: cuurent cards in player"""
        self.children.append(TreeNode(player, card=cards, action="fold"))


class gameTree:

    def __init__(self):
        self.children = []
        self.players = []

    def addNode(self, bet, lastBet, player, cards):
        print("worked")


game = gameTree()