n = int(input())
Ai = list(map(int,input().split()))
total = []
for point in range(n):
    emptyList = []
    for x in range(n):
        dx = abs(x - point)
        peopleDx = dx * Ai[x]
        emptyList.append(peopleDx)
    total.append(sum(emptyList))
print(min(total))