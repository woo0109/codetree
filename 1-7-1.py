a, b = map(int, input().split())
sum = 0

l = [True] * 101
l[1] = False

for i in range(2, 11):
    if not l[i]:
        continue
    for j in range(2*i, 101, i):
        l[j] = False

def even(n):
    if ((n % 10) + (n // 10)) % 2 == 0:
        return True

for i in range(a, b+1):
    if even(i) and l[i]:
        sum += 1

print(sum)