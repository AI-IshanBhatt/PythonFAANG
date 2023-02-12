print("Creating Grid")
print("EASY WRONG WAY")

rows,cols = 4,5

grid = [[0]*cols]* rows
grid[0][1] = 55
# This will set first element in all rows as 55 because * creates 5 references to same row, so if you change any, all of them gets changed
print(grid)

print("THE RIGHT WAY")
grid = [[0]*cols for _ in range(rows)]
grid[0][1] = 99
print(grid)


def get_neighbors(i, j):
    return [(nr, nc) for nr,nc in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)] if 0 <= nr < rows and 0 <= nc < cols]


print(get_neighbors(3,4))
print(get_neighbors(1,1))