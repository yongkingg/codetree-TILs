N = int(input())


def printText(n):
    if n == 0:
        return
    
    print("HelloWorld")
    printText(n-1)


printText(N)