import math

f = open("./day_8/input_text.txt",'r')
Map = f.readlines()
f.close()

path = Map[0].strip()
#print(Map)

nodes = {}

for line in Map:
    if line.strip() == '' or line.strip() == path:
        continue
    else:
        line = line.split(" = ")
        nodes[line[0]] = (line[1].strip().split()[0][1:4], line[1].strip().split()[1][:3])
       
def isFinished(nodesAt):
    finished = True
    for node in nodesAt:
        if node[-1] != "Z":
           finished = False
    return finished
       

def doPath(start):
    count = -1
    pathIndex = -1
    while True:
        count += 1
        if isFinished([start]):
            return count
        else:
            pathIndex += 1
            start = nodes[start][0 if path[pathIndex % len(path)] == 'L' else 1]



# count = 0
# currentNodes = []
# for key in nodes.keys():
#     if key[-1] == "A":
#         currentNodes.append(key)

# while not isFinished(currentNodes):
    
#     for decision in path:
#         for i in range(len(currentNodes)):
#             count += 1
#             currentNodes[i] = nodes[currentNodes[i]][0 if decision == 'L' else 1]
            

startPos = [key for key in nodes.keys() if key[-1] == 'A']
endCounts = list(map(doPath, startPos))
print(endCounts)

# https://stackoverflow.com/questions/37237954/calculate-the-lcm-of-a-list-of-given-numbers-in-python
lcm = 1

for x in endCounts:
    lcm = lcm*x//math.gcd(lcm, x)

print(lcm)


# print(doPath(key for key in nodes.keys() if key[-1] == 'A'))
