def getNumFromStr(string:str):
    num = 0
    for c in string:
        if not c.isdigit():
            break
        else:
            num = num * 10 + int(c)

    return num

def isPossible(line:str):
    line = line.strip()
    possible = True

    sets = line[line.find(":")+2:].split("; ")
    # print(sets)

    for set in sets:
        pulls = set.split(", ")
        # print(pulls)

        for pull in pulls:
            count = getNumFromStr(pull)

            match pull[pull.find(" ")+1:]:
                case "red":
                    if count > 12:
                        possible = False
                case "green":
                    if count > 13:
                        possible = False
                case "blue":
                    if count > 14:
                        possible = False

    # print(line, "\n" + possible, "\n\n")
    print(f"{line}\n{possible}")

    return possible
                
def getGameNum(gameLine:str):
    num = 0
    if isPossible(gameLine): num = getNumFromStr(gameLine[gameLine.find(" ")+1:])
    print(f"{num=}\n")
    return num


#print(getNumFromStr("33 blue"))
#print(isPossible("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"))
#print(getGameNum("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"))

f = open("./day_2/input_text.txt", "r")

print(sum(map(getGameNum, f.readlines())))

f.close()
