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
if o == "*":
    print(plus(a, o, c))
elif o == "-":
    print(minus(a,o,c))
elif o == "*":
    print(minus(a,o,c))
elif o == "/":
    print(divide(a,o,c))
else:
    print("False")