n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
count = 0

for i in range(n-2):
    for j in range(n-2):
        current = 0
        for row in range(i, i+3):
            for col in range(j, j+3):
                if grid[row][col] == 1:
                    current += 1
        
        if current > count:
            count = current

print(count)