grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]

k = 4

grid = [list(i) for i in zip(*grid)]

print(grid)

for i in range(k):
    last_row = [grid[-1][-1]] + grid[-1][:-1]
    grid = [last_row] + grid[:-1]


grid = [list(i) for i in zip(*grid)]
print(grid)