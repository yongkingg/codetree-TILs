m1, d1, m2, d2 = map(int, input().split())
A = input()
days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
type = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# m1월 d1일의 요일 계산
start_weekday = type.index(A)

# 목표 요일 계산
target_weekday = type.index(A)

# 두 날짜의 총 일수 계산
total_days = (sum(days[:m2 - 1]) + d2) - (sum(days[:m1 - 1]) + d1) + 1

# 특정 요일의 등장 횟수 계산
count = 0
for day_offset in range(total_days):
    if (start_weekday + day_offset) % 7 == target_weekday:
        count += 1

print(count)