# dx and dy for 8 directions
dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]
import sys

matrix = [list(line) for line in sys.stdin.read().splitlines()]
symbol_cords = []
for i, line in enumerate(matrix):
    for j, character in enumerate(line):
        if character in "1234567890.":
            continue
        symbol_cords.append((i, j))
numbers = []
done = set()
for symbol in symbol_cords:
    x, y = symbol
    print(matrix[x][y], end="")
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if (nx, ny) in done:
            continue
        if (
            0 <= nx < len(matrix)
            and 0 <= ny < len(matrix[nx])
            and matrix[nx][ny] in "1234567890"
        ):
            # Find the number
            done.add((nx, ny))
            digits = matrix[nx][ny]
            e = ny - 1
            while e >= 0:
                if matrix[nx][e] not in "1234567890":
                    break
                done.add((nx, e))
                digits = matrix[nx][e] + digits
                e -= 1
            ny += 1
            while ny < len(matrix[nx]):
                # print(nx, ny, len(matrix), len(matrix[0]), len(matrix[nx]))
                if matrix[nx][ny] not in "1234567890":
                    break
                done.add((nx, ny))
                digits += matrix[nx][ny]
                ny += 1
            print(digits)
            numbers.append(int(digits))
print("A", len(set(numbers)))
print("B", len(numbers))
print(sum(numbers))
