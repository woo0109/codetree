m, d = map(int, input().split())

def distinguish(m, d):
    l = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if 1 <= m <= 12:
        return d <= l[m]
    else:
        return False

if distinguish(m, d):
    print("Yes")
else:
    print("No")