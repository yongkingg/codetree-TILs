n = int(input())
def f(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return f(n // 2) + 1
    elif n % 2 != 0:
        return f(n // 3) + 1
print(f(n))