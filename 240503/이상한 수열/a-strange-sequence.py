n = int(input())

def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    
    return f(n // 3) + f(n-1)


print(f(n))