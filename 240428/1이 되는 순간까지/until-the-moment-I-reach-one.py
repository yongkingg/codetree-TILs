n = int(input())
count = 0
def f(n, count):
    if n == 1:
        return count
    elif n % 2 == 0:
        count += 1
        return f(n // 2, count)
    elif n % 2 != 0:
        count += 1
        return f(n // 3, count)
print(f(n, count))