N = int(input())
dotList = []


class dot:
    def __init__(self, leng, index):
        self.leng = leng
        self.index = index

    
def length(x,y):
    return int(abs(x) + abs(y))

for index in range(N):
    x, y = map(int,input().split())
    dotList.append(dot(length(x,y),index+1))

dotList.sort(key= lambda x : x.leng)

for index in range(N):
    print(dotList[index].index)