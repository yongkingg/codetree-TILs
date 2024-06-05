m1, d1, m2, d2 = map(int,input().split())
A = input()
days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
type = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

days_dif = (sum(days[:m2 - 1]) + d2) - (sum(days[:m1 - 1]) + d1)
day_idx = type.index(A)



tmpType = int((days_dif + day_idx + 1) / 7)


# count = 0
# for index in range(abs(days_dif)):
#     tmpType = type[int((index + day_idx + 1) % 7)]
#     if tmpType == A:
#         count += 1

print(tmpType)