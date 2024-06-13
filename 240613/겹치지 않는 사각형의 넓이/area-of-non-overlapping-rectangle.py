A = list(map(int,input().split()))
B = list(map(int,input().split()))
M = list(map(int,input().split()))

for index in range(4):
    A[index] += 1000
    B[index] += 1000
    M[index] += 1000

cord = [[0 for _ in range(2000)] for _ in range(2000)]


for x in range(A[0], A[2]):
    for y in range(A[1], A[3]):
        cord[x][y] = 1

for x in range(B[0], B[2]):
    for y in range(B[1], B[3]):
        cord[x][y] = 1

for x in range(M[0], M[2]):
    for y in range(M[1], M[3]):
        if cord[x][y] == 1:
            cord[x][y] += 1


count = 0
for x in range(0,2000):
    for y in range(0,2000):
        if cord[x][y] == 1:
            count += 1

print(count)