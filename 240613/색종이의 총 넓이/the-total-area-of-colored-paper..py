n = int(input())
cord = [[0 for _ in range(200)] for _ in range(200)]
pointList = []
dx = 8
dy = 8
for index in range(n):
    point = list(map(int,input().split()))
    pointList.append(point)

for index in range(len(pointList)):
    startX = pointList[index][0]
    startY = pointList[index][1]
    for x in range(startX, startX + dx):
        for y in range(startY, startY + dy):
            cord[x][y] = 1

count = 0
for x in range(200):
    for y in range(200):
        if cord[x][y] == 1:
            count += 1


print(count)