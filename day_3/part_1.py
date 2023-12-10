import pprint

f = open("./day_3/input_text.txt", 'r')
engine = f.readlines()
engine = list(map(lambda o: o.strip(), engine))
f.close()

pprint.pprint(engine)

ignored_chars = "1234567890."

final = 0


def getNum(y, x):
    idx = 0
    num = 0
    while x + idx != len(engine[y]) and engine[y][x+idx].isdigit():
        num *= 10
        num += int(engine[y][x+idx])
        idx += 1
        

    return num

#print(getNum(0,0))


def isPartNum(y, x):

    print(f"{y = }, {x = }")

    if y > 0:
        for i in range(len(str(getNum(y, x)))):
            if engine[y-1][x+i] not in ignored_chars:
                return True
            
    if y < len(engine)-1:
        for i in range(len(str(getNum(y, x)))):
            if engine[y+1][x+i] not in ignored_chars:
                return True
            
    if x > 0:
        if engine[y][x-1] not in ignored_chars:
            return True
    
        if y > 0:
            if engine[y-1][x-1] not in ignored_chars:
                return True

        if y < len(engine)-1:
            if engine[y+1][x-1] not in ignored_chars:
                return True
        
    if x + len(str(getNum(y, x))) < len(engine[y]):
        print(f"{y = } {x + len(str(getNum(y, x))) = }")
        if engine[y][x + len(str(getNum(y, x)))] not in ignored_chars:
            return True
    
        if y > 0:
            if engine[y-1][x + len(str(getNum(y, x)))] not in ignored_chars:
                return True

        if y < len(engine)-1:
            if engine[y+1][x + len(str(getNum(y, x)))] not in ignored_chars:
                return True



    return False



nums = []

for y in range(len(engine)):
    for x in range(len(engine[y])):
        if engine[y][x].isdigit() and (not engine[y][x-1].isdigit() if x > 0 else True):
            if isPartNum(y, x):
                print(getNum(y,x))
                nums.append(getNum(y,x))

print(nums)

print(sum(nums))