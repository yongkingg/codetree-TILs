m1, d1, m2, d2 = map(int, input().split())
A = input()
days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekend = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

days_dif =(sum(days[:m2-1]) + d2) - (sum(days[:m1-1]) + d1)
count = 0
for index in range(days_dif):
    if (weekend[(index+1) % 7] == A):
        count += 1

print(count)