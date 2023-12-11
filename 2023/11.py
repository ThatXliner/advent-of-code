import sys


matrix = [list(line) for line in sys.stdin.read().splitlines()]
i = 0
# Expand the cosmos
while i < len(matrix):
    line = matrix[i]
    if all(char == "." for char in line):
        matrix.insert(i, ["."] * len(line))
        i += 1
    i += 1
i = 0
# Expand the cosmos
while i < len(matrix[0]):
    if all(matrix[x][i] == "." for x in range(len(matrix))):
        for j in range(len(matrix)):
            matrix[j].insert(i, ".")
        i += 1
    i += 1
# Find shotest paths between every pair of "#"
# First, fine the coordinates of all "#"
coords = [
    (i, j)
    for i, line in enumerate(matrix)
    for j, char in enumerate(line)
    if char == "#"
]
# Now, find the shortest path between every pair of coordinates via subtracting the coordinates
# and taking the absolute value of the difference
distance = [
    abs((first := coords[i])[0] - (second := coords[j])[0]) + abs(first[1] - second[1])
    for i in range(len(coords))
    for j in range(i, len(coords))
    if i != j
]
print(sum(distance))
