N = int(input())


def printText1(n):
    if n == 0:
        return
    
    print(n, end=" ")
    printText1(n-1)

def printText2(n):
    if n == 0:
        return
    
    printText1(n -1)
    print(n, end=" ")

printText2(N)
print()
printText1(N)