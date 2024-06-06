n = int(input())
tmpList = list(str(n))

num = 0
for index in range(len(tmpList)):
    num = num * 2 + int(tmpList[index])

print(num)