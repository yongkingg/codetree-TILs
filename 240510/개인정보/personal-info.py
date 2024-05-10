class Info:
    def __init__(self, name, h, w):
        self.name = name
        self.h = h
        self.w = w

infoList = []

for index in range(5):
    name, h, w = map(str,input().split())
    infoList.append(Info(name, int(h),float(w)))


infoList.sort(key=lambda x : x.name)
print("name")
for index in range(len(infoList)):
    print(infoList[index].name, infoList[index].h, infoList[index].w)

print()
infoList.sort(key=lambda x : -x.h)
print("height")
for index in range(len(infoList)):
    print(infoList[index].name, infoList[index].h, infoList[index].w)