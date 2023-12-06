f = open("./day_6/input_text.txt", 'r')

paper = f.readlines()
for l in range(len(paper)):
    paper[l] = paper[l][11:].strip()
   
times = paper[0].split(" ")

while '' in times:
    times.remove('')

records = paper[1].split(" ")

while '' in records:
    records.remove('')

time = ""
record = ""

for t in times:
    time += t
   

for r in records:
    record += r


print(time)
print(record)


times = [int(time)]
records = [int(record)]

waysToBeatRecords = [0 for i in range(len(times))]

i = -1
for t in times:
    i += 1
    for h in range(0, t):
        # h = speed in mm/ms
       
        # Get the distacnce it'll go.
        # s = d / t
        # d = s * t
        # d = h * (t - h)
       
       # print(h * (t-h))
       
        #print(h * (t-h), records[i])
       
        if h * (t-h) > records[i]:
            waysToBeatRecords[i] += 1
       
       
print(waysToBeatRecords)

prod = 1
for w in waysToBeatRecords:
    prod *= w

print(f"========={prod}=========")

f.close()