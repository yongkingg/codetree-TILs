N = int(input())
infoList = []

class Student:
    def __init__(self,h, w, number):
        self.h = h
        self.w = w
        self.number = number

for index in range(N):
    h, w = map(int,input().split())
    infoList.append(Student(h,w, index + 1))

infoList.sort(key= lambda x : (x.h, x.w))


for index in range(len(infoList)):
    print(infoList[index].h, infoList[index].w, infoList[index].number)