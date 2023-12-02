def getNumFromStr(string:str):
    num = 0
    for c in string:
        if not c.isdigit():
            break
        else:
            num = num * 10 + int(c)

    return num

def getPower(line:str) -> list[int, int, int]:
    line = line.strip()

    numbers:list[int, int, int] = [0, 0, 0]

    sets = line[line.find(":")+2:].split("; ")

    for set in sets:
        pulls = set.split(", ")

        for pull in pulls:
            count = getNumFromStr(pull)

            match pull[pull.find(" ")+1:]:
                case "red":
                    numbers[0] = count if count > numbers[0] else numbers[0]

                case "green":
                    numbers[1] = count if count > numbers[1] else numbers[1]

                case "blue":
                    numbers[2] = count if count > numbers[2] else numbers[2]

    return numbers[0]*numbers[1]*numbers[2]

f = open("./day_2/input_text.txt", "r")

print(sum(map(getPower, f.readlines())))

f.close()
