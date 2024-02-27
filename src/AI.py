import numpy as np

def evaluateHand(communityCards, player):

    hand = player._hand
    hand.sort(key=lambda x: x._value, reverse=True)
    comCards = communityCards
    allCards = []
    allCards.append(hand[0])
    allCards.append(hand[1])
    comVal = []
    comSuit = []
    handPair = False
    cardLen = len(player._gameRound._shoe._decks) * 52
    

    for card in comCards:
        if card == None or card in allCards:
            continue
        comVal.append(card._value)
        comSuit.append(card._suit)
        allCards.append(card)

    allCards.sort(key=lambda x: x._value, reverse=True)
    evalHand = player._gameRound.handVal(allCards)

    handVal = 0  # handVal will be based on chance for each action. EG; 1-10 is % chance for HighCard win, so 100% is 10 for expample has an Ace in hand, 1-10 for pair wins
    # it will give a 1-10 for chance of what its going to get * by its order in list, then segment handVals value, 1-20 fold, 20-30 low bet, 30-50 high bet, 50+ all in.

    evalIndex = [
        "RF", "SF", "4OfKind", "FullHouse", "Flush", "Straight", "ThreeOfKind",
        "TwoPair", "Pair", "High"
    ]
    cardVals = {
        "14": 10,
        "13": 9,
        "12": 9,
        "11": 8,
        "10": 8,
        "9": 7,
        "8": 6,
        "7": 5,
        "6": 5,
        "5": 4,
        "4": 3,
        "3": 2,
        "2": 2,
    }
    chance = {
        "RF": 0,
        "SF": 0,
        "4OfKind": 0,
        "FullHouse": 0,
        "Flush": 0,
        "Straight": 0,
        "ThreeOfKind": 0,
        "TwoPair": 0,
        "Pair": [0,0],
        "High": 0
    }





    

    for x in range(len(evalHand), 0, -1):
        if evalHand[evalIndex[x - 1]] != []:
            handVal += cardVals[str(evalHand[evalIndex[x - 1]][0])] * x

    #how close to getting pair
    tempIndex = 0
    
    if hand[0]._value == hand[1]._value:
        handPair = True
        print("Pair hand")
    for card in hand:
        if card._value in comVal:
            chance["Pair"][tempIndex] = 100
            print(f"{card._name} Pair")
        else:
            numVal = comVal.count(card._value)
            numVal = 4 - hand.count(card._value) - numVal
            chance["Pair"][tempIndex] = numVal/((len(player._gameRound._shoe._decks)*52)-2-len(comVal))*100
            print(f"{card._name} Pair chance: {numVal/(cardLen-2-len(comVal))*100}")
        tempIndex += 1
        
    #chance to two
    pairs = 0
    if handPair == True:
        for val in comVal:
            if comVal.count(val) >= 2:
                chance["TwoPair"] = 100

        if chance["TwoPair"] != 100:
            chance["TwoPair"] = len(np.unique(comVal))/(cardLen - len(comVal) - 2)
    else:
        for card in comVal:
            for hcard in hand: 
                if card == hcard._value: #checks if card is a pair with a card in the hand
                    pairs += 1
            if comVal.count(card) >= 2:
                pairs += 0.5

        if pairs == 1:
            chance["TwoPair"] = (numVal + (3 * len(np.unique(comVal))) /(cardLen-2-len(comVal))*100)
        if pairs == 0:
            chance["TwoPair"] =  ((3 + len(comVal) / (cardLen - len(comVal) - 2)) ** 2) * 100

        if pairs == 2:
            chance["TwoPair"] = 100
                
    print(int(pairs))
    
    
    
    print(evalHand)
    print("End:", handVal)
    print(chance)
    return
