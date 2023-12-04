points = 0

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

for line in f.readlines():
    matches = getMatches(line)

    linescore = 0
    if matches > 0:
        linescore = 1

        for _ in range(matches-1):
            linescore *= 2

    points+=linescore

print(points)
f.close()