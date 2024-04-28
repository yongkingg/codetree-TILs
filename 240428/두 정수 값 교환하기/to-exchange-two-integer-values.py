def swap(n, m):
    emptyList = [m, n]
    return emptyList
    


n, m = map(int,input().split())
print("{} {}".format(swap(n,m)[0], swap(n,m)[1]))