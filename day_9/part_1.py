f = open("./day_9/input_text.txt", 'r')
histories = f.readlines()
f.close()

histories = list(map(lambda obj:obj.strip(), histories))
for i in range(len(histories)):
    histories[i] = list(map(int, histories[i].split(" ")))


print(histories)
areAllElemsTheSame = lambda x, n: x.count(n) == len(x)

print(areAllElemsTheSame([3,3,3,3,3],3))

def findDifferences(history):
    # history = list(map(int, history.split()))
    differences = []
    for i in range(len(history)-1):
        differences.append(history[i+1] - history[i])

    return differences

def extrapolate(history):
    historyDifferences = [history, findDifferences(history)]

    # print(f"{not areAllElemsTheSame(historyDifferences[-1])}\n{historyDifferences[-1][0] != 0}")

    while not areAllElemsTheSame(historyDifferences[-1], 0):
        historyDifferences.append(findDifferences(historyDifferences[-1]))

    # print(historyDifferences)

    # Go through backwards, appending
    for x in range(len(historyDifferences)-1, 0, -1):
        historyDifferences[x-1].append(historyDifferences[x][-1] + historyDifferences[x-1][-1])

    return historyDifferences[0][-1]

print(sum(list(map(extrapolate, histories))))