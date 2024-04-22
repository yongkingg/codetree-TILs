def plus(a, o, c):
    result = a + c
    return ("{} {} {} = {}".format(a, o, c, result))
def minus(a, o, c):
    result = a - c
    return ("{} {} {} = {}".format(a, o, c, result))
def multi(a, o, c):
    result = a * c
    return ("{} {} {} = {}".format(a, o, c, result))
def divide(a, o, c):
    result = a / c
    return ("{} {} {} = {}".format(a, o, c, result))



a, o, c = map(str,input().split())
if o == "+":
    print(plus(int(a), o, int(c)))
elif o == "-":
    print(minus(int(a), o, int(c)))
elif o == "*":
    print(multi(int(a), o, int(c)))
elif o == "/":
    print(divide(int(a), o, int(c)))
else:
    print("False")