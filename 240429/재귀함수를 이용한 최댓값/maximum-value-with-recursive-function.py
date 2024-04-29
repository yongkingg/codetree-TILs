n = int(input())
M = list(map(int,input().split()))

def f(n):
    if n == 0:
        return M[0]
    
    return max(f(n-1), M[n])


print(f(n-1))