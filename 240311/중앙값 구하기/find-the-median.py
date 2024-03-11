a, b, c = map(int, input().split())
emptyList = [a, b, c]
## 선택정렬
for index in range(len(emptyList) - 1):
    minIndex = index
    for seq in range(index + 1, len(emptyList)):
        if(emptyList[seq] < emptyList[minIndex]):
            minIndex = seq
    emptyList[index],emptyList[minIndex] = emptyList[minIndex],emptyList[index]
print(emptyList[1])