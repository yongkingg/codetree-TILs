n1 = input()
n2 = input()

n1 = list(n1)
n1.sort()

n2 = list(n2)
n2.sort()

if n1 == n2:
    print("Yes")
else:
    print("No")