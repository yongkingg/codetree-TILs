def printRec(n,m):
    for index in range(n):
        print("1" * m)
        
n, m = map(int,input().split())
printRec(n,m)