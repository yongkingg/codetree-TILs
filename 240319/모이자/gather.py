n = int(input())
Ai = input()
aiList = Ai.split()
total = []

for point in range(n):
    cal = []
    for x in range(0,n):
        dx = abs(x - point)
        peopleDx = dx * int(aiList[x])
        cal.append(peopleDx)
    total.append(sum(cal))


print(min(total))