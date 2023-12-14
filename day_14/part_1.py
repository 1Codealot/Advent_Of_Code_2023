

import pprint

f = open("./day_14/input_text.txt", 'r')
platform = f.readlines()
platform = list(map(list,list(map(lambda o: o.strip(), platform))))
f.close()

pprint.pprint(platform)
print("\n\n")

for x in range(len(platform[0])):
    # G down the list and find 'O'
    for y in range(len(platform)):
        if platform[y][x] == "O":
        # Bring it up (To 0).
            c = y-1 #                     My favorite python feature, negative indexing has betrayed me.
            while platform[c][x]=="." and c >= 0:
                platform[c][x], platform[c+1][x] = platform[c+1][x], platform[c][x]
                c-=1

                   
       
pprint.pprint(platform)

# Get score
score = 0
lineNum = len(platform)
for line in platform:
    score += line.count("O")*lineNum
    lineNum -= 1

print(score)