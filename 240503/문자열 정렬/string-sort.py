n = int(input())
emptyList = []
for index in range(n):
    text = input()
    text = list(text)
    text.sort()
    print(text)
    sortText = ''.join(text)

    emptyList.append(sortText)
for index in range(n):
    print(emptyList[index])