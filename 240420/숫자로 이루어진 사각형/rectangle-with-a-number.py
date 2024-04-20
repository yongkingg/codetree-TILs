def printRec(N):
    firstNum = 1
    for column in range(N):
        for num in range(N):
            if firstNum > 9:
                firstNum = 1
            print(firstNum, end=" ")
            firstNum += 1

        print()


N = int(input())
printRec(N)