n = int(input())
num = list(map(int,input().split()))

emptyList = []
for index in range(1,n+1):
    emptyList.append(num[index-1])
    if index % 2 != 0:
        sortList = sorted(emptyList)
        print(sortList[index // 2], end=" ")