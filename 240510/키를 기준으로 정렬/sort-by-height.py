n = int(input())

class Info:
    def __init__(self, name, cm, kg):
        self.name = name
        self.cm = cm
        self.kg = kg


infoList = []

for index in range(n):
    name, cm, kg = map(str,input().split())
    infoList.append(Info(name,cm,kg))

infoList.sort(key=lambda x : x.cm)


for index in range(len(infoList)):
    print(infoList[index].name, infoList[index].cm, infoList[index].kg)