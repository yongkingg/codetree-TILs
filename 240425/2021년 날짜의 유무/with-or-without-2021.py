# 홀수달은 31일까지, 짝수달은 30일까지. 단, 2월은 28일까지 
def is_correct_day(M,D):
    if M > 12:
        return False
    elif M == 2:
        if D > 28:
            return False
    elif M % 2 == 0:
        if D > 30:
            return False
    else:
        if D > 31:
            return False
    return True




M, D = map(int,input().split())
if is_correct_day(M, D):
    print("Yes")
else:
    print("No")