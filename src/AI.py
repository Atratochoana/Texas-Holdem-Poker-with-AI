import numpy as np
import pandas as pd


def evaluateHand(communityCards, player):

    hand = player._hand
    hand.sort(key=lambda x: x._value, reverse=True)
    comCards = communityCards
    allCards = []  # call cards including hand and community cards
    allCards.append(hand[0])
    allCards.append(hand[1])
    comVal = []  # community cards values
    comSuit = []  # community cards suits
    cardLen = len(
        player._gameRound._shoe._decks
    ) * 52  # shoe length with all cards  not the ones that have been kicked out yet

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
        "Pair": [0, 0],
        "High": 0
    }

    for x in range(len(evalHand), 0, -1):
        if evalHand[evalIndex[x - 1]] != []:
            handVal += cardVals[str(evalHand[evalIndex[x - 1]][0])] * x

    #how close to getting pair
    tempIndex = 0

    if hand[0]._value == hand[1]._value:
        handPair = True
    for card in hand:
        if card._value in comVal:
            chance["Pair"][tempIndex] = 100
        else:
            numVal = comVal.count(card._value)
            numVal = 4 - hand.count(card._value) - numVal
            chance["Pair"][tempIndex] = numVal / (
                (len(player._gameRound._shoe._decks) * 52) - 2 -
                len(comVal)) * 100
        tempIndex += 1

    #chance to two
    pairs = 0
    if handPair == True:
        for val in comVal:
            if comVal.count(val) >= 2:
                chance["TwoPair"] = 100

        if chance["TwoPair"] != 100:
            chance["TwoPair"] = len(
                np.unique(comVal)) / (cardLen - len(comVal) - 2)
    else:
        for card in comVal:
            for hcard in hand:
                if card == hcard._value:  #checks if card is a pair with a card in the hand
                    pairs += 1
            if comVal.count(card) >= 2:
                pairs += 0.5

        if pairs == 1:
            chance["TwoPair"] = ((numVal + (3 * len(np.unique(comVal)))) /
                                 (cardLen - 2 - len(comVal))) * 100
        if pairs == 0:
            if len(comVal) >= 4:
                chance["TwoPair"] = 0
            else:
                chance["TwoPair"] = ((15 / (52 - 5)) * (6 / (52 - 6))) * 100
        if pairs == 2:
            chance["TwoPair"] = 100

    #chance for three of kind
    if handPair == True:  # if you have two of the same cards in ur hand, chance to get same type over multiple goes
        if comVal.count(hand[0]._value) >= 1:
            chance["ThreeOfKind"] = 100
        else:
            chance["ThreeOfKind"] = (2 / (cardLen - len(comVal) - 2)) * 100
    else:
        for card in hand:
            if comVal.count(card._value) >= 2:
                chance["ThreeOfKind"] = 100
            if comVal.count(card._value) == 1:
                chance["ThreeOfKind"] = ((2 / (cardLen - len(comVal) - 2)) +
                                         (2 / (cardLen - len(comVal) - 3)) +
                                         ((3 / (cardLen - len(comVal) - 2)) *
                                          (2 /
                                           (cardLen - len(comVal) - 2)))) * 100
            if comVal.count(card._value) == 0:
                if len(comVal) == 4:
                    chance["ThreeOfKind"] = 0
                    break
                chance["ThreeOfKind"] = (6 / (cardLen - len(comVal) - 2)) * (
                    2 / (cardLen - len(comVal) - 3)) * 100

    #chance to get a straight - WIP
    sOut = 0
    cVal = 0
    print(allCards)
    for card in range(len(allCards) - 1):
        sOut += allCards[card]._value - allCards[card - 1]._value

    print(sOut)

    #chance to get a straight flush - WIP
    leftMatch = False
    rightMatch = False
    if comSuit.count(hand[0]._suit) >= 2:
        leftMatch = True
    if comSuit.count(hand[1]._suit) >= 2:
        leftMatch = True

    matchingSuit = []
    if leftMatch:
        for x in range(len(comSuit)):
            if hand[0]._suit == comSuit[x]:
                matchingSuit.append(communityCards[x])
        matchingSuit.append(hand[0])
    elif rightMatch:
        for x in range(len(comSuit)):
            if hand[1]._suit == comSuit[x]:
                matchingSuit.append(communityCards[x])
        matchingSuit.append(hand[1])

    if hand[0]._suit == hand[1]._suit:
        matchingSuit.append(hand[1])

    matchingSuit.sort(key=lambda x: x._value, reverse=True)

    if leftMatch or rightMatch:
        out = 0
        for cards in matchingSuit:
            pass

    else:
        chance["Straight"] = 0

    # print("mathcingsuits : ", matchingSuit)
    # print("left: ",leftMatch)
    # print("right: ",rightMatch)

    print(evalHand)
    print("End:", handVal)
    print(chance)
    return
