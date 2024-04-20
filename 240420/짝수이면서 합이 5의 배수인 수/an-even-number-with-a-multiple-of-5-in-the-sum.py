def isNum(n):
    sum = list(map(int,str(n)))
    if n % 2 == 0 and (sum[0] + sum[1]) % 5 == 0:
        return "Yes"
    else:
        return "No"


n = int(input())
print(isNum(n))