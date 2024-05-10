N = int(input())

class Info:
    def __init__(self, h, w, number):
        self.h = h
        self.w = w
        self.number = number

infoList = []

for index in range(N):
    h, w = map(str,input().split())
    infoList.append(Info(int(h),int(w), index+1))


infoList.sort(key=lambda x : (-x.h, -x.w, x.number))

for index in range(len(infoList)):
    print(infoList[index].h, infoList[index].w, infoList[index].number)