a, b = map(int, input().split())
n = int(input())
# 처음에 a진수로 표현된걸 b진수로 바꾸면 됨 ..

tmpList = list(str(n))
num = 0
for index in range(len(tmpList)):
    num = num * a + int(tmpList[index])
tmpList = []
while True:
    if num < b:
        tmpList.append(num)
        break

    tmpList.append(num % b)
    num //= b

for index in range(len(tmpList)):
    print(tmpList[len(tmpList) - 1 - index], end="")