def getNum(a,b,c):
    minNum = min(a,b,c)
    return minNum


a, b, c = tuple(map(int,input().split()))
print(getNum(a,b,c))