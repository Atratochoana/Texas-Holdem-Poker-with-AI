class TreeNode:
    def __init__(self,player,action=None,card=[]):
        self.action = action #actions taken place
        self.player = player #player index
        self.cards = card #cards visible at the time of play
        self.children = [] #children connected to this action

    def addChild(self,Node):
        self.children.append(Node)

    def removeChild(self,child):
        if child in self.children:
            self.children.pop(self.children.index(child))
            return True
        else:
            return False


        
