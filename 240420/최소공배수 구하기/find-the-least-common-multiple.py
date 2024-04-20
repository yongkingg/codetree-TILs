n, m = map(int,input().split())

def solv(n,m):
    value = 0
    for index in range(1, min(n,m) + 1):
        if n % index == 0 and m % index == 0:
            value = (n * m) / index

    print(value)


solv(n,m)