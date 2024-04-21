import numpy as np
import random
import math


def evaluateHand(communityCards, player):
    hand = player._hand
    hand.sort(key=lambda x: x._value, reverse=True)
    comCards = communityCards
    allCards = []  # call cards including hand and community cards
    allCards.append(hand[0])
    allCards.append(hand[1])
    lenUnique = 2
    comVal = []  # community cards values
    comSuit = []  # community cards suits
    cardLen = len(
        player._gameRound._shoe._decks
    ) * 52  # shoe length with all cards  not the ones that have been kicked out yet
    handPair = False

    if hand[0]._value == hand[1]._value:
        lenUnique -= 1
        handPair = True

    for card in comCards:
        if card == None or card in allCards:
            continue
        if card._value != hand[0]._value and card._value != hand[
                1]._value and card._value not in comVal:
            lenUnique += 1

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

    #chance to get a straight
    sOut = 0
    for card in range(len(allCards) - 1):
        if allCards[card]._value == allCards[card + 1]._value:
            continue
        sOut += (allCards[card]._value - allCards[card + 1]._value) - 1
    if lenUnique <= 4:
        sOut += 1

    if sOut >= 3:
        chance["Straight"] = 0
    else:
        chance["Straight"] = ((4 / (cardLen - len(allCards)))**sOut) * 100

    #chance for a flush
    if len(comSuit) == 3:
        if hand[0]._suit == hand[1]._suit and comSuit.count(
                hand[0]._suit) == 3:
            chance["Flush"] = 100
        elif comSuit.count(hand[0]._suit) == 3 or comSuit.count(
                hand[1]._suit) == 3:
            chance["Flush"] = (10 / (cardLen - 5)) * 100
        elif hand[0]._suit == hand[1]._suit and comSuit.count(
                hand[0]._suit) == 2:
            chance["Flush"] = (10 / (cardLen - 5)) * 100
        elif hand[0]._suit == hand[1]._suit and comSuit.count(
                hand[0]._suit) == 1:
            chance["Flush"] = (11 / (cardLen - 5)) * (10 / (cardLen - 6)) * 100
        elif comSuit.count(hand[0]._suit) == 2 or comSuit.count(
                hand[1]._suit) == 2:
            chance["Flush"] = (11 / (cardLen - 5)) * (10 / (cardLen - 6)) * 100
        else:
            chance["Flush"] = 0
    elif len(comSuit) == 4:
        if hand[0]._suit == hand[1]._suit and comSuit.count(
                hand[0]._suit) >= 3:
            chance["Flush"] = 100
        elif comSuit.count(hand[0]._suit) == 4 or comSuit.count(
                hand[1]._suit) == 4:
            chance["Flush"] = 100
        elif comSuit.count(hand[0]._suit) == 3 or comSuit.count(
                hand[1]._suit) == 3:
            chance["Flush"] = (10 / (cardLen - 6)) * 100
        elif comSuit.count(hand[0]._suit) <= 2 or comSuit.count(
                hand[1]._suit) <= 2:
            chance["Flush"] = 0

    #chance to get a fullHouse - 3 of a kind and 2 of a kind3
    fullUnique = [
    ]  # 2d list with first value being the val second being count
    for card in comVal:
        Changed = False
        for count in fullUnique:
            if count[0] == card:
                count[1] += 1
                Changed = True
        if Changed == False:
            fullUnique.append([card, 1])

    Fchance = 0
    changed0 = False
    changed1 = False
    full = False
    if handPair == True:
        for cards in fullUnique:
            if full == True:
                continue
            if cards[1] == 3:
                full = True
            tempChance = (4 - cards[1]) / (52 - (2 + len(comVal)))
            for x in range(2 - cards[1]):
                tempChance = tempChance * (4 - cards[1] -
                                           x) / (52 - (2 + len(comVal) + x))
            Fchance += tempChance
    else:
        for count in fullUnique:
            if count[0] == hand[0]._value:
                count[1] += 1
                changed0 = True
            if count[0] == hand[1]._value:
                count[1] += 1
                changed1 = True
        if changed0 == False:
            fullUnique.append([hand[0]._value, 1])
        if changed1 == False:
            fullUnique.append([hand[1]._value, 1])
        three = False
        two = False
        for count in fullUnique:
            if count[1] == 3:
                three = True
            if count[1] == 2:
                two = True
        if three and two:
            full = True
        else:
            for count in fullUnique:
                threeChance = (4 - count[1]) / (52 - 2 - len(comVal))
                for x in range(2 - count[1]):
                    threeChance = threeChance * (4 - count[1] - x) / (
                        52 - 2 - len(comVal) - x)
                twoChance = 0
                for count2 in fullUnique:
                    if count2 is not count:
                        if twoChance != 100:
                            if count2[1] == 2:
                                twoChance = 100
                            else:
                                twoChance += 3 / (52 - 2 - len(comVal))
                Fchance += threeChance * twoChance

    chance["FullHouse"] = Fchance
    if full == True:
        chance["FullHouse"] = 100

    #Chance to get 4 of a kind :0
    if handPair == True:
        count = 2
        for val in comVal:
            if val == hand[0]._value:
                count += 1
        if count == 4:
            chance["4OfKind"] = 100
        if count == 3:
            chance["4OfKind"] = 1 / (52 - 2 - len(comVal)) * 100
        else:
            chance["4OfKind"] = (2 / (52 - 2 - len(comVal))) * (
                1 / (52 - 3 - (len(comVal)))) * 100
    else:
        count0 = 1
        count1 = 1
        for val in comVal:
            if val == hand[0]._value:
                count0 += 1
            if val == hand[1]._value:
                count1 += 1
            if count0 == 4 or count1 == 4:
                chance["4OfKind"] = 100
            else:
                tempChance = (4 - count0) / (52 - 2 - len(comVal))
                for x in range(3 - count0):
                    tempChance = tempChance * (4 - count0 - x) / (52 - 2 - x -
                                                                  len(comVal))
                chance["4OfKind"] += tempChance
                tempChance = (4 - count1) / (52 - 2 - len(comVal))
                for x in range(3 - count1):
                    tempChance = tempChance * (4 - count1 - x) / (52 - 2 - x -
                                                                  len(comVal))
                chance["4OfKind"] += tempChance
        chance["4OfKind"] = chance["4OfKind"] * 100.0

    #chance to get a straight flush + Royal Flush
    heart = []
    diamond = []
    club = []
    spade = []
    suits = [heart, diamond, club, spade]
    SFchance = 0
    for card in allCards:
        if card._suit == "heart":
            heart.append(card)
        if card._suit == "diamond":
            diamond.append(card)
        if card._suit == "club":
            club.append(card)
        if card._suit == "spade":
            spade.append(card)

    for suit in suits:
        if (5 - len(suit)) < (5 - len(comVal)):
            out = 0
            for x in range(len(suit) - 1):

                if suit[x]._value - 1 != suit[x + 1]._value:
                    out += 1

            if out == 0:
                chance["SF"] = 100
            else:
                SFchance += ((1 / (52 - 2 - len(comVal)))**out) * 100
                if suit[0]._value == 14:
                    chance["RF"] += ((1 / (52 - 2 - len(comVal)))**out) * 100

    chance["SF"] = SFchance

    print(chance)
    return [chance, evalHand]


def playAction(gameRound, player):
    if gameRound._table._players.index(player) != gameRound.nextPlayer:
        print(f"Not {player._name} turn yet")
        return

    hand = player._hand
    handEval = evaluateHand(gameRound._communityCards, player)
    handVal = handEval[1]
    handEval = handEval[0]

    bluff = random.randint(0, 3)
    if bluff == 1:
        secondBluff = random.randint(1, 4)
        if secondBluff == 1:
            gameRound.playerAction(gameRound.lastBet, player)
        elif secondBluff == 2:
            val = gameRound.lastBet + math.floor(gameRound._pot / 4)
            gameRound.playerAction(val, player)
        elif secondBluff == 3:
            val = gameRound.lastBet + math.floor(gameRound._pot / 2)
            gameRound.playerAction(val, player)
        elif secondBluff == 4:
            val = gameRound._pot
            gameRound.playerAction(val, player)

    try:
        if handVal["RF"] == 100 or handVal["SF"] == 100 or handVal[
                "4OfKind"] == 100 or handVal["FullHouse"] == 100 or handVal[
                    "Flush"] == 100 or handVal["Straight"] == 100:
            val = gameRound._pot
            gameRound.playerAction(val, player)
        elif handEval["RF"] > 2 or handEval["SF"] > 2 or handEval["4OfKind"] > 2 or handEval["FullHouse"] > 4 or handEval["Flush"] > 4 or handEval["Straight"] > 8:
            val = gameRound.lastBet + math.floor(gameRound._pot / 2)
            gameRound.playerAction(val, player)
        elif handEval["Straight"] > 4 or handEval["ThreeOfKind"] > 4:
            val = gameRound.lastBet + math.floor(gameRound._pot / 4)
            gameRound.playerAction(val, player)
        elif handVal["ThreeOfKind"] == 100 or handVal["TwoPair"] == 100:
            val = gameRound.lastBet + math.floor(gameRound._pot / 2)
            gameRound.playerAction(val, player)
        else:
            gameRound.playerAction(False,player)
    except:
        val = gameRound.lastBet
        gameRound.playerAction(val, player)
