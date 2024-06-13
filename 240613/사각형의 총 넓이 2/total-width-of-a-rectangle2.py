n = int(input())
cord = [[0 for _ in range(200)] for _ in range(200)]
recList = []
offset = 100
for _ in range(n):
    rec = list(map(int,input().split()))
    for index in range(len(rec)):
        rec[index] += 100
    recList.append(rec)

for index in range(len(recList)):
    for x in range(recList[index][0], recList[index][2]):
        for y in range(recList[index][1], recList[index][3]):
            cord[x][y] = 1

area = 0
for x in range(0, 200):
    for y in range(0, 200):
        if cord[x][y]:
            area += 1

print(area)