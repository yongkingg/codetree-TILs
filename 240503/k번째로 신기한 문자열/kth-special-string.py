n, k, T = map(str, input().split())
wordList = []
for index in range(int(n)):
    word = input()
    word = list(word)
    if word[:len(list(T))] == list(T):
        word = ''.join(word)
        wordList.append(word)


wordList.sort()
print(wordList[int(k)])