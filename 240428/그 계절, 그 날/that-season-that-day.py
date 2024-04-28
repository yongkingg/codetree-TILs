# 윤년 == 2월이 29일까지 있음.
# 짝수달 => 30일까지, 홀수달 => 31일까지
def is_yoon_year(Y):
    if (Y % 4 == 0 and Y % 100 != 0) or (Y % 4 == 0 and Y % 100 == 0 and Y % 400 == 0):
        return True
    else:
        return False


def is_correct_day(yoon, M,D):
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
    if M >= 3 and M <= 5:
        print("Spring")
    elif M >= 6 and M <= 8:
        print("Summer")
    elif M >= 9 and M <= 11:
        print("Fall")
    else:
        print("Winter")

Y, M, D = map(int,input().split())
isYoon = is_yoon_year(Y)
if isYoon:
    isCorrect = is_correct_day(isYoon, M, D)
    if isCorrect:
        is_weather(M)
else:
    print("-1")