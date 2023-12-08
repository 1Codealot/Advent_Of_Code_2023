import pprint

f = open("./day_7/input_text.txt", 'r')
hands = f.readlines()
f.close()

bids:dict[str, int] = {}

for hand in hands:
    # sortedHand = hand.split(" ")[0].split()
    # sortedHand.sort()
    # sortedHand = str([c for c in sortedHand])
   
    bids[hand.split(" ")[0].strip()] = int(hand.split(" ")[1])

def getHandType(hand:str):
    hand = ''.join(sorted(hand.split(" ")[0]))
    # 1 = High card
    # 2 = One pair
    # 3 = Two pair
    # 4 = Three of a kind
    # 5 = Full house
    # 6 = Four of a kind
    # 7 = Five of a kind

    handType = 0
   
    uniqueCards = []
    for card in hand:
        if card not in uniqueCards:
            uniqueCards.append(card)

    for card in uniqueCards:
        if hand.count(card) == 5:
            handType = 7
            break

        elif hand.count(card) == 4:
            handType = 6
            break

        elif hand.count(card) == 3:
            if len(uniqueCards) == 2:
                handType = 5
                break

            elif len(uniqueCards) == 3:
                handType = 4
        
        elif hand.count(card) == 2:
            if len(uniqueCards) == 2:
                handType = 5
                break

            elif len(uniqueCards) == 3:
                handType = 3
                break

            elif len(uniqueCards) == 4:
                handType = 2
                break

        elif hand.count(card) == 1:
            if len(uniqueCards) == 5:
                handType = 1
                break
            else:
                continue



    print(hand, handType)
    return handType
       
       
def compareHands(hand1, hand2):
    order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    
    for i in range(len(hand1)):
        if order.index(hand1[i]) > order.index(hand2[i]):
            #print("qwerty")
            return (hand1, hand2)
        elif order.index(hand1[i]) < order.index(hand2[i]):
            #print("asdfgh")
            return (hand2, hand1)
        else:
            #print("zxcvbn")
            continue
       
def ranks(_hands:list[str]):
    #print("vehsdgfyukwagiu")
    ranks = [[],[],[],[],[],[],[]]
    for hand in _hands:
        ranks[getHandType(hand)-1].append(hand)
        
        
    #print(ranks)
    # Rank by highest card
    for hands in ranks:
        for _ in range(len(hands)): # Bubble sort baby!!!!!!!!!!
            for i in range(0,len(hands)-1):
                hands[i], hands[i+1] = compareHands(hands[i], hands[i+1])[0], compareHands(hands[i], hands[i+1])[1]
            
    final = []

    for group in ranks:
        if len(group) > 0:
            final.extend(group)
    
    return final

final = 0

#pprint.pprint(bids.keys())
idx = 0
for hand in ranks(bids.keys()):
    idx += 1
    final += (bids[hand] * idx)

print(final)
