n = int(input())

class Info:
    def __init__(self, name, score1, score2, score3):
        self.name = name
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3


infoList = []

for index in range(n):
    name, score1, score2, score3 = map(str,input().split())
    infoList.append(Info(name,int(score1),int(score2), int(score3)))


infoList.sort(key=lambda x : x.score1 + x.score2 + x.score3)

for index in range(len(infoList)):
    print(infoList[index].name, infoList[index].score1, infoList[index].score2, infoList[index].score3)