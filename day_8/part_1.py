f = open("./day_8/input_text.txt",'r')
Map = f.readlines()
f.close()

path = Map[0].strip()
#print(Map)

nodes:dict[str, tuple[str, str]] = {}

for line in Map:
    if line.strip() == '' or line.strip() == path:
        continue
    else:
        line = line.split(" = ")
        nodes[line[0]] = (line[1].strip().split()[0][1:4], line[1].strip().split()[1][:3])
       
       
       
count = 0
currentNode = 'AAA'
while currentNode != 'ZZZ':
    for decision in path:
        #print(f"{currentNode = }")
        count += 1
        currentNode = nodes[currentNode][0 if decision == 'L' else 1]

print(count)
#print(nodes)