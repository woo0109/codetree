n = int(input())

l = list(map(int,input().split()))

def print_list(l):
    for i in l:
        if i % 2 == 0:
            print(i // 2, end =' ')
        else:
            print(i, end = ' ')

print_list(l)