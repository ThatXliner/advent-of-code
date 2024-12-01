import sys
from collections import deque

matrix = [list(line) for line in sys.stdin.read().splitlines()]
start = None
for i, line in enumerate(matrix):
    for j, cell in enumerate(line):
        if cell == "S":
            matrix[i][j] = "."
            start = (i, j)
            break
    if start:
        break

# Matrix is a flood-fillable
# list of lists where '.' is a traversable cell
# and '#' is a wall.
# BFS and count how many unique ending
# cells are possible after exactly X moves
X = 6
Q = deque([(X, start, (start,))])
dx = 0, 0, 1, -1
dy = 1, -1, 0, 0
output = set()
seen = set()
while Q:
    amount, cord, e = Q.popleft()
    if len(e) % X == 0:
        output.add(e)
    if amount == 0:
        output.add(e)
        continue
    x, y = cord
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (
            0 <= nx < len(matrix)
            and 0 <= ny < len(matrix[0])
            and matrix[nx][ny] == "."
            and (nx, ny) not in seen
        ):
            seen |= {(nx, ny)}
            Q.append((amount - 1, (nx, ny), e + ((nx, ny),)))
print(output)
# more = 0
# for i in list(output):
#     n = X // 2 - 1
#     more += n
print(len(output) * 2)
