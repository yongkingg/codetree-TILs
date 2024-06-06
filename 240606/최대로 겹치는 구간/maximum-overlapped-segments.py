maximumR = 200
rangeValue = 100
tmpList = [0] * maximumR
n = int(input())
for _ in range(n):
    x1, x2 = map(int,input().split())
    x1 += rangeValue
    x2 += rangeValue
    for index in range(x1, x2):
        tmpList[index] += 1

print(max(tmpList))