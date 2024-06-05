m1, d1, m2, d2 = map(int,input().split())

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
type = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


days_dif = (sum(days[:m2-1]) + d2) - (sum(days[:m1-1]) + d1)

print(type[(days_dif % 7)])