def evaluateHand(communityCards, player):

    hand = player._hand
    hand.sort(key=lambda x: x._value, reverse=True)
    comCards = communityCards
    allCards = []
    allCards.append(hand[0])
    allCards.append(hand[1])
    comVal = []
    comSuit = []
    pocket = False

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

    for x in range(len(evalHand), 0, -1):
        if evalHand[evalIndex[x - 1]] != []:
            handVal += cardVals[str(evalHand[evalIndex[x - 1]][0])] * x

    #how close to getting pair

    if hand[0]._value == hand[1]._value:
        pocket = True
        print("Pocket Pair [{hand[0]._name}]")
    for card in hand:
        if card._value in comVal:
            print(f"{card._name} Pair")
        else:
            numVal = comVal.count(card._value)
            numVal = 4 - hand.count(card._value) - numVal
            print(f"{card._name} Pair chance: {numVal/((len(player._gameRound._shoe._decks)*52)-2-len(comVal))*100}")

    #chance to two
    if pocket == True:
        for val in -comVal:
            if comVal.count(val) >= 2:
                print(f"Two Pair {val}, {val}")

    
    print(evalHand)
    print("End:", handVal)
    return
