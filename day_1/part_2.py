def getNumber(line:str) -> int:
    first = last = 0
    for x in range(len(line)):
        if line[x].isdigit():
            first = line[x]
            break


        elif line[x:x+3] == "one" or line[x:x+3] == "two" or line[x:x+3] == "six": 
            first = line[x:x+3]
            break

        elif line[x:x+4] == "four" or line[x:x+4] == "five" or line[x:x+4] == "nine":
            first = line[x:x+4]
            break

        elif line[x:x+5] == "three" or line[x:x+5] == "seven" or line[x:x+5] == "eight":
            first = line[x:x+5]
            break

    line = line[::-1]

    for x in range(len(line)):
        if line[x].isdigit():
            last = line[x]
            break

        elif line[x:x+3] == "one"[::-1] or line[x:x+3] == "two"[::-1] or line[x:x+3] == "six"[::-1]: 
            last = line[x:x+3]
            break

        elif line[x:x+4] == "four"[::-1] or line[x:x+4] == "five"[::-1] or line[x:x+4] == "nine"[::-1]:
            last = line[x:x+4]
            break

        elif line[x:x+5] == "three"[::-1] or line[x:x+5] == "seven"[::-1] or line[x:x+5] == "eight"[::-1]:
            last = line[x:x+5]
            break


    last = last[::-1]

    match first:
        case "one":
            first = 1
        case "two":
            first = 2
        case "three":
            first = 3
        case "four":
            first = 4
        case "five":
            first = 5
        case "six":
            first = 6
        case "seven":
            first = 7
        case "eight":
            first = 8
        case "nine":
            first = 9

    match last:
        case "one":
            last = 1
        case "two":
            last = 2
        case "three":
            last = 3
        case "four":
            last = 4
        case "five":
            last = 5
        case "six":
            last = 6
        case "seven":
            last = 7
        case "eight":
            last = 8
        case "nine":
            last = 9

    first = int(first)
    last = int(last)

    num = first*10 + last

    print(first, last, num)

    return num



f = open("./day_1/input_text.txt", "r")

#print(sum(map(getNumber, f.readlines())))

print(sum(map(getNumber, f.readlines())))

f.close()

