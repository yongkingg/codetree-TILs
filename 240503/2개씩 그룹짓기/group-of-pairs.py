N = int(input())
num = list(map(int,input().split()))
num.sort()
emptyList = []

# [n-1]번째와 [2n-1]번째의 수를 매칭해주는게 좋음

for index in range(N):
    emptyList.append(num[index] + num[2*N - 1 - index])
print(max(emptyList))