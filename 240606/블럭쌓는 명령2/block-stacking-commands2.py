N, K = map(int,input().split())
blocks = [0 for _ in range(N)]
for _ in range(K):
    Ai, Bi = map(int,input().split())
    for index in range(Ai, Bi + 1):
        blocks[index] += 1


print(max(blocks))