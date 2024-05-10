N = int(input())

number = list(map(int,input().split()))
info = []

class Number:
    def __init__(self, number, befPos, aftPos):
        self.number = number
        self.befPos = befPos
        self.aftPos = aftPos





for index in range(len(number)):
    info.append(Number(number[index], index+1, 0))


sortedInfo = sorted(info,key= lambda x : x.number)


for index in range(len(number)):
    # info[index].aftPos = index
    # print(info[index].aftPos, end=" ")

    sortedInfo[index].aftPos = index + 1

for index in range(len(number)):
    print(info[index].aftPos, end=" ")
    
# print()
# for index in range(len(number)):
#     print("SortedInfo : ", end=" ")
#     print(info[index].number, info[index].befPos, info[index].aftPos)


# print()
# for index in range(len(number)):
#     print(info[index].aftPos, end=" ")