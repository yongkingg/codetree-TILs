N, B = map(int,input().split())
tmpList = []
while True:
    if N < B:
        tmpList.append(N)
        break

    tmpList.append(N % B)
    N //= B


for index in range(len(tmpList)):
    print(tmpList[len(tmpList) - 1 - index], end="")