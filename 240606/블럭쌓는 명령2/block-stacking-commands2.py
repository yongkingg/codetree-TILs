N, K = map(int,input().split())
blocks = [0 for _ in range(N+1)]
for _ in range(K):
    Ai, Bi = map(int,input().split())
    for index in range(Ai, Bi + 1):
        blocks[index] += 1


print(max(blocks))


# 세로를 추가하라는 얘기가 아니라, 한줄에서 계속 반복..