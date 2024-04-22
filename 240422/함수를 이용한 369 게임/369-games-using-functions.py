def isTrue(a, b):
    magicNumber = 0
    for index in range(a,b+1):
        if index % 3 == 0 or 3 in list(map(int,str(index))) or 6 in list(map(int,str(index))) or 9 in list(map(int,str(index))):
            magicNumber += 1
    return magicNumber


a, b = map(int,input().split())
print(isTrue(a,b))