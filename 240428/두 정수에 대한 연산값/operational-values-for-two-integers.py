def cal(a, b):
    if a > b:
        a += 25, 
        b = b * 2
    else:
        a = a * 2
        b += 25
    return a, b




a, b = map(int, input().split())
print(*cal(a,b))