def isMagicNum(n):
    divideNum = list(map(int,str(n))) 
    cal = 0
    for index in range(len(divideNum)):
        cal += divideNum[index]
    if cal % 2 == 0:
        return True
    return False


def isPrimeNum(n):
    if n == 1:
        return False
    else:
        for index in range(2,n):
            if n % index == 0:
                return False
    return True




a, b = map(int,input().split())
count = 0
for index in range(a,b+1):
    if isMagicNum(index) and isPrimeNum(index):
        count += 1
print(count)