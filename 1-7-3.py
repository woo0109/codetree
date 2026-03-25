m, d = map(int, input().split())

def distinguish(m):
    if m == 2:
        return 2
    elif m in [1,3,5,7,8,10,12]:
        return True
    else:
        return False

if distinguish(m) == 2 and d < 29:
    print("Yes")
elif distinguish(m) != 2 and distinguish(m) and d < 32:
    print("Yes")
elif distinguish(m) != 2 and not distinguish(m) and d < 31:
    print("Yes")
else:
    print("No")