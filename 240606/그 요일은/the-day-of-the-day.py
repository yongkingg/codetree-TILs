m1, d1, m2, d2 = map(int, input().split())
A = input().strip()

days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# m1월 d1일이 어떤 요일인지 계산
start_day_of_week = weekdays.index(A)

# 두 날짜 사이의 일수 계산
total_days = 0
for month in range(m1, m2 + 1):
    # 해당 월의 마지막 일수
    end_day = min(days_in_month[month - 1], d2 if month == m2 else days_in_month[month - 1])
    
    # 시작 월이면서 월이 바뀌지 않는 경우
    if month == m1 and month == m2:
        total_days += end_day - d1 + 1
    # 시작 월인 경우
    elif month == m1:
        total_days += days_in_month[month - 1] - d1 + 1
    # 종료 월인 경우
    elif month == m2:
        total_days += d2
    # 중간 월인 경우
    else:
        total_days += days_in_month[month - 1]

# 시작일의 요일을 맞추기 위해 추가로 이동해야 하는 날짜 계산
extra_days = (start_day_of_week - (d1 - 1)) % 7

# 특정 요일이 등장하는 횟수 계산
count = (total_days + extra_days) // 7

print(count)