def sum(N):
    num = 0
    for index in range(1,N+1):
        num += index
    num = int(num / 10)
    return num




N = int(input())
print(sum(N))