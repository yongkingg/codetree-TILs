n = int(input())

class Score:
    def __init__(self,name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math


infoList = []

for index in range(n):
    name, kor, eng, math = map(str,input().split())
    infoList.append(Score(name, int(kor),int(eng),int(math)))

infoList.sort(key=lambda x : (-x.kor, -x.eng, -x.math))


for index in range(len(infoList)):
    print(infoList[index].name, infoList[index].kor, infoList[index].eng, infoList[index].math)