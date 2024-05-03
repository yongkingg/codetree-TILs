class info:
    def __init__(self, code, place, time):
        self.code = code
        self.place = place
        self.time = time

        print("secret code : " + self.code)
        print("meeting point : " + self.place)
        print("time : " + self.time)

code, place, time = map(str,input().split())
info(code,place,time)