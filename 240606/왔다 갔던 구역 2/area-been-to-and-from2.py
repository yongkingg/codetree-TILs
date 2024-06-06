n = int(input())

xlaxis = [0] * 2000
currentPos = 1000
for _ in range(n):
    command = list(map(str, input().split()))
    direction = command[1]
    if (direction == "R"):
        dx = int(command[0])
        for index in range(currentPos, currentPos + dx):
            xlaxis[index] += 1
        currentPos += dx
    elif (direction == "L"):
        dx = int(command[0])
        for index in range(currentPos - dx, currentPos):
            xlaxis[index] += 1
        currentPos -= dx

count =0
for index in xlaxis:
    if index >= 2:
        count +=1

print(count)