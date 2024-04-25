def is_correct(n1_element, n2_element):
    if len(n2_element) > len(n1_element):
        return False
    elif n2_element[0] not in n2_element:
        return False
    else:
        index = n1_element.index(n2_element[0])
        for x in range(n2):
            try:
                if n1_element[index+x] == n2_element[x]:
                    pass
                else:
                    return False
            except:
                return False
        return True

n1, n2 = map(int,input().split())
n1_element = list(map(int,input().split()))
n2_element = list(map(int,input().split()))
if is_correct(n1_element, n2_element):
    print("Yes")
else:
    print("No")