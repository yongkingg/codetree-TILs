N, k = map(int,input().split())
Num = list(map(int,input().split()))

Num.sort()
kNum = Num[k-1]
print(kNum)