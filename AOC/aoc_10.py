from collections import deque

directions = {"|": [(-1, 0), (1, 0)], "-": [(0, -1), (0, 1)],
              "7": [(0, -1), (1, 0)], "L": [(-1, 0), (0, 1)], "F": [(1, 0), (0, 1)], "J": [(0, -1), (-1, 0)]}

visited = set()

with open("aoc_input_10") as f:
    lines = [[i for i in l.strip()] for l in f.readlines()]

    directions_move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque()
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "S":
                start = (i, j)
                visited.add(start)
                queue.append(start)

    counter = 0
    while queue:
        counter += 1
        for i in range(len(queue)):
            start = queue.popleft()
            for r, c in directions_move:
                nr, nc = start[0] + r, start[1] + c
                if 0 <= nr < len(lines) and 0 <= nc < len(lines[0]):
                    if (nr, nc) not in visited:
                        if r == -1 and c == 0 and (lines[nr][nc] == "F" or lines[nr][nc] == "7" or lines[nr][nc] == "|"):
                            visited.add((nr, nc))
                            queue.append((nr, nc))
                        elif r == 1 and c == 0 and (lines[nr][nc] == "L" or lines[nr][nc] == "J" or lines[nr][nc] == "|"):
                            visited.add((nr, nc))
                            queue.append((nr, nc))
                        elif r == 0 and c == -1 and (lines[nr][nc] == "F" or lines[nr][nc] == "L" or lines[nr][nc] == "-"):
                            visited.add((nr, nc))
                            queue.append((nr, nc))
                        elif r == 0 and c == 1 and (lines[nr][nc] == "7" or lines[nr][nc] == "J" or lines[nr][nc] == "-"):
                            visited.add((nr, nc))
                            queue.append((nr, nc))

    print(counter-1)

