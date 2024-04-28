A = input()

def isMagicText(A):
    text = list(A)
    count = 0

    for index in range(1, len(text)):
        standard = text[0]
        if standard != text[index]:
            count += 1
    
    return count

if isMagicText(A):
    print("Yes")
else:
    print("No")