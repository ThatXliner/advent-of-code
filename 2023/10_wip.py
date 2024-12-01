import sys

matrix = [list(line) for line in sys.stdin.read().splitlines()]
S = None
for i, line in enumerate(matrix):
    for j, char in enumerate(line):
        if char == "S":
            S = (i, j)
            break
    if S is not None:
        break

cur_distance = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
x, y = S
visited = set()
print(matrix[x][y])
while True:
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if (nx, ny) in visited:
            continue
        visited.add((nx, ny))
        if nx < 0 or nx >= len(matrix) or ny < 0 or ny >= len(matrix[0]):
            continue
        # print("tryt", (matrix[nx][ny]))
        # print(matrix[nx][ny], nx, ny)
        if matrix[nx][ny] == ".":
            continue
        if matrix[x][y] == "L" and not ((y > ny and x == nx) or (nx > x and y == ny)):
            continue
        if matrix[x][y] == "7" and not ((ny < y and x == nx) or (nx > x and y == ny)):
            continue
        if matrix[x][y] == "J" and not ((ny < y and x == nx) or (nx < x and y == ny)):
            continue
        if matrix[x][y] == "F" and not ((y < ny and x == nx) or (nx > x and y == ny)):
            continue
        if matrix[x][y] == "|" and ny != y:
            continue
        if matrix[x][y] == "-" and nx != x:
            continue
        visited.add((nx, ny))
        x = nx
        y = ny
        print(matrix[x][y])
        cur_distance += 1
        break
    else:
        break
    if matrix[x][y] == "S":
        break
print(cur_distance // 2)
