def isPalindrome(A):
    text = list(A)
    for index in range(len(text)):
        if text[index] != text[len(text) - (index + 1)]:
            return False
    return True

A = input()
if isPalindrome(A):
    print("Yes")
else:
    print("No")