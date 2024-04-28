n = int(input())

def printNum(n):
    if n == 0:
        return 
    
    print("* " * n, end=" ")
    print()
    printNum(n-1)
    print("* " * n, end=" ")
    print()

printNum(n)