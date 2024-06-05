m1, d1, m2, d2 = map(int, input().split())
A = input()
days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
type = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# 시작 날짜의 요일을 계산합니다.
start_day_of_week = type.index(A)

# 결과를 저장할 변수를 초기화합니다.
count = 0

# 주어진 범위 내의 각 날짜에 대해 요일을 계산하고, A 요일이면 count를 증가시킵니다.
for month in range(m1, m2 + 1):
    start_day = d1 if month == m1 else 1
    end_day = d2 if month == m2 else days[month - 1]
    
    for day in range(start_day, end_day + 1):
        # 현재 날짜의 요일을 계산합니다.
        current_day_of_week = (start_day_of_week + day - d1) % 7
        
        # A 요일과 같으면 count를 증가시킵니다.
        if current_day_of_week == type.index(A):
            count += 1

print(count)