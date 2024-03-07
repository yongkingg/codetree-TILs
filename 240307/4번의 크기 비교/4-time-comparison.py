a = int(input())
b, c, d, e = map(int,input().split())

emptyList = [a]
opp = [b, c, d, e]

for index in range(4):
    if(a > opp[index]):
        opp[index] = 1
    else:
        opp[index] = 0
    print(opp[index])