n = int(input())
rangeValue = [0] * 100
for index in range(n):
    x1, x2 = map(int,input().split())
    for index in range(x1, x2 + 1):
        rangeValue[index] += 1
print(max(rangeValue))