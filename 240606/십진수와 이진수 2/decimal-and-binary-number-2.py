N = int(input())
tmpList = list(str(N))

num = 0
for index in range(len(tmpList)):
    num = num * 2 + int(tmpList[index])

tmpList = []
N = num * 17
while True:
    if N < 2:
        tmpList.append(N)
        break
    tmpList.append(N % 2)
    N //= 2


for index in range(len(tmpList)):
    print(tmpList[len(tmpList) - 1 - index], end="")