a, b, c = map(int,input().split())


def f(n):
    if n // 10 == 0:
        return n 
    
    return f(n // 10) + (n % 10)



print(f(int(a*b*c)))