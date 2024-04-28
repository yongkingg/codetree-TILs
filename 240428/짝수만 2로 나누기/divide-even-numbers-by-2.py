def divide(M):
    for index in range(len(M)):
        if M[index] % 2 == 0:
            M[index] = int(M[index] / 2)
    return M



N = int(input())
M = list(map(int,input().split()))
print(*divide(M))