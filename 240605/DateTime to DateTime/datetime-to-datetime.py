a, b, c = map(int,input().split())

if ( a < 11 or b < 11 or c < 11):
    print("-1")
else:
    days_dif = a - 11
    hours_dif = abs(b - 11)
    min_dif = abs(c - 11)



    min_dif += days_dif * 24 * 60
    min_dif += hours_dif * 60

    print(min_dif)