n = int(input())
tmpList = []
while True:
    if n < 2:
        tmpList.append(n)
        break
    tmpList.append(n % 2)


for index in range(len(tmpList)):
    print(tmpList[len(tmpList) - 1 - index], end=" ")