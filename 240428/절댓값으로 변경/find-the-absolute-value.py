N = int(input())
nList = list(map(int,input().split()))

def getIndex(nList):
    for index in range(len(nList)):
        if nList[index] < 0:
            nList[index] = int(nList[index] * -1)
        else: 
            pass
    return nList


print(getIndex(nList))