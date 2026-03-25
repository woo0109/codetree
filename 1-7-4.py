n, m = map(int, input().split())

parent = [i for i in range(n + 1)]
num = n

for _ in range(m):
    a, b = map(int, input().split())
    
    if parent[a] != parent[b]:
        for i in range(a, b+1):
            parent[i] = parent[a]
    
    ps = set(parent)
    print(len(ps)-1)
    print(parent)

# def find(x):
#     if parent[x] == x:
#         return x
#     parent[x] = find(parent[x]) 
#     return parent[x]

# def union(a, b):
#     root_a = find(a)
#     root_b = find(b)
#     if root_a != root_b:
#         parent[root_b] = root_a
#         return True 
#     return False 

# for _ in range(m):
#     a, b = map(int, input().split())
    
#     for i in range(a, b):
#         union(i, i + 1)

#     ps = set(parent)
#     print(len(ps)-1)