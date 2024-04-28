# 윤년 == 2월이 29일까지 있음.
# 짝수달 => 30일까지, 홀수달 => 31일까지
def is_yoon_year(Y):
    if (Y % 4 == 0 and Y % 100 != 0) or (Y % 4 == 0 and Y % 100 == 0 and Y % 400 == 0):
        return True
    else:
        return False

def is_correct_day(yoon, M,D):
    if M > 12 or M < 1:
        return False
    else:
        if yoon:
            if M == 2:
                if D > 29:
                    return False
            elif M % 2 == 0:
                if M == 8:
                    if D > 31:
                        return False
                else:
                    if D > 30:
                        return False
            elif M % 2 != 0:
                if D > 31:
                    return False
            return True
        else:
            if M == 2:
                if D > 28:
                    return False
            elif M % 2 == 0:
                if M == 8:
                    if D > 31:
                        return False
                else:
                    if D > 30:
                        return False
            elif M % 2 != 0:
                if D > 31:
                    return False
            return True

def is_weather(M):
    if M == 3 or M == 4 or M == 5:
        print("Spring")
    elif M == 6 or M == 7 or M == 8:
        print("Summer")
    elif M == 9 or M == 10 or M == 11:
        print("Fall")
    elif M == 12 or M == 1 or M == 2:
        print("Winter")
    else:
        print("-1")

Y, M, D = map(int,input().split())
isYoon = is_yoon_year(Y)
isCorrect = is_correct_day(isYoon, M, D)
if isCorrect:
    is_weather(M)
else:
    print("-1")