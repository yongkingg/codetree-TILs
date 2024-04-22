def is_yoon(n):
    if n % 4 == 0 and n % 400 == 0:
        return True
    return False

n = int(input())
if is_yoon(n):
    print("true")
else:
    print("false")