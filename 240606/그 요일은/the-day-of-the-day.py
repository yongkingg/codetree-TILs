m1, d1, m2, d2 = map(int, input().split())
A = input()
days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
type = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# m1월 d1일의 요일 계산
start_weekday = type.index(A)

# 목표 요일 계산
target_weekday = type.index(A)

# 두 날짜 사이의 날 수 계산
total_days = 0
for month in range(m1, m2 + 1):
    # 현재 월의 마지막 날짜
    if month == m2:
        last_day = d2
    else:
        last_day = days[month - 1]
    
    # 현재 월에서 A요일이 몇 번 등장하는지 계산
    for day in range(1, last_day + 1):
        if (start_weekday + day - 1) % 7 == target_weekday:
            total_days += 1

# 결과 출력
print(total_days)