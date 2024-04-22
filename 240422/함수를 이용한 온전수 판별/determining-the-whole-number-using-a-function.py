def isMagicNum(n):
    if n % 2 == 0:
        return False
    elif n % 5 == 0:
        return False
    elif n % 3 == 0 and n % 9 != 0:
        return False
    return True






a, b = map(int,input().split())
count = 0
for index in range(a, b+1):
    if isMagicNum(index):
        count += 1
print(count)