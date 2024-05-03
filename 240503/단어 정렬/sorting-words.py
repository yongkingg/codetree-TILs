n = int(input())
emptyList = []
for index in range(n):
    text = input()
    emptyList.append(text)

emptyList.sort()
for index in range(n):
    print(emptyList[index])