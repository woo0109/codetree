import sys

sys.setrecursionlimit(200000)
input = sys.stdin.readline

n, m = map(int, input().split())

parent = list(range(n + 2))

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x]) 
    return parent[x]

current_count = n

for _ in range(m):
    a, b = map(int, input().split())
    
    curr = find(a)
    while curr < b:
        next_node = find(curr + 1)
        parent[curr] = next_node
        current_count -= 1
        curr = next_node 
    
    print(current_count)