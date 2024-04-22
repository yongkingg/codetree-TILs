def is_prime(n):
    if n == 1:
        return False
    for index in range(2, n):
        if n % index == 0:
            return False
    return True


a, b = map(int,input().split())
sum_val = 0
for i in range(a, b+1):
    if is_prime(i):
        sum_val += i 
print(sum_val)