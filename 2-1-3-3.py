a = input()

def palindrome(a):
    b = a[::-1]
    if a == b:
        print("Yes")
    else:
        print("No")

palindrome(a)