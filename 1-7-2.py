n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def serial(a, b):
    for i in range(len(a)):
        if a[i : i+len(b)] == b:
            return True
    return False

if serial(a, b):
    print("Yes")
else:
    print("No")