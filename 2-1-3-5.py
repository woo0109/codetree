a = int(input())

l = list(map(int, input().split()))

def ab(l):
    for i in range(len(l)):
        l[i] = abs(l[i])
    return l

ab(l)
print(*l)