def evaluateHand(communityCards, player):

    hand = player._hand
    hand.sort(key=lambda x: x._value, reverse=True)
    comCards = communityCards
    allCards = hand
    comVal = []
    comSuit = []
    
    for card in comCards:
        if card == None:
            continue
        comVal.append(card._value)
        comSuit.append(card._suit)
        allCards.append(card)
    allCards.sort(key=lambda x: x._value, reverse=True)
    evalHand = player._gameRound.handVal(allCards)

    handVal = 0  # handVal will be based on chance for each action. EG; 1-10 is % chance for HighCard win, so 100% is 10 for expample has an Ace in hand, 1-10 for pair wins
    # it will give a 1-10 for chance of what its going to get * by its order in list, then segment handVals value, 1-20 fold, 20-30 low bet, 30-50 high bet, 50+ all in.

    evalIndex = ["RF","SF","4OfKind","FullHouse","Flush","Straight","ThreeOfKind","TwoPair","Pair","High"]
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

    print(evalHand)
    
    for x in range(len(evalHand),0,-1):
        if evalHand[evalIndex[x-1]] != []:
            print(evalHand[evalIndex[x-1]][0])
            handVal += cardVals[str(evalHand[evalIndex[x-1]][0])] * x
            print(cardVals[str(evalHand[evalIndex[x-1]][0])])
            
    
    
    
        
    print(evalHand)
    print("End:",handVal)
    return
