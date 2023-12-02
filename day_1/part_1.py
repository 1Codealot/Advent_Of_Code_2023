def getNumber(line:str) -> int:
    numAsStr:str = ""
    # Find first number
    for char in line:
        if char.isdigit():
            numAsStr += char
            break

    # Find last number

    for char in reversed(line):
        if char.isdigit():
            numAsStr += char
            break

    return int(numAsStr)

f = open("./day_1/input_text.txt", "r")

print(sum(map(getNumber, f.readlines())))

f.close()
