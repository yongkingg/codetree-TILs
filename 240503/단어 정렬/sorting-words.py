n = int(input())
textList = []
for index in range(n):
    inputText = input()
    sortText = list(inputText).sort()
    textList.append(sortText)

for index in range(n):
    print(textList[index])