import pprint

def getMatches(card):
    splitted = card.split("|")
    splitted[0] = splitted[0][splitted[0].find(": ")+2:].strip().split(" ")
   
    splitted[1] = splitted[1].strip().split(" ")
   
   
    # Remove empty strings
   
    while '' in splitted[0]:
        splitted[0].remove('')
       
    while '' in splitted[1]:
        splitted[1].remove('')
   
    idx = 0
    for m in splitted[0]:
        splitted[0][idx] = int(m)
        idx += 1
   
    idx = 0
    for n in splitted[1]:
        splitted[1][idx] = int(n)
        idx += 1
       
    matches = 0
    for x in splitted[1]:
        if x in splitted[0]:
            matches +=1

    return matches

f = open("./day_4/input_text.txt",'r')

cards = f.readlines()

countOfEachCard:dict[str, int] = {}
countOfEachCard["Card: 1"] = 1

cardNum = 1
for card in cards:
    if f"Card: {cardNum}" not in countOfEachCard:
        countOfEachCard[f"Card: {cardNum}"] = 0

    countOfEachCard[f"Card: {cardNum}"] += 1 if f"Card: {cardNum}" != "Card: 1" else 0

    for i in range(countOfEachCard[f"Card: {cardNum}"]):
        for x in range(1, getMatches(card)+1):
            if f"Card: {cardNum+x}" not in countOfEachCard:
                countOfEachCard[f"Card: {cardNum+x}"] = 0

            countOfEachCard[f"Card: {cardNum+x}"] += 1

    cardNum+=1
    #pprint.pprint(countOfEachCard) # NOTE: This is hella slow as is, definatly do NOT uncomment this line lmao



print(sum(countOfEachCard.values()))
f.close()