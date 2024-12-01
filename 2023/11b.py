import sys


matrix = [list(line) for line in sys.stdin.read().splitlines()]
i = 0
# First, find the coordinates of all "#"
coords = [
    (i, j)
    for i, line in enumerate(matrix)
    for j, char in enumerate(line)
    if char == "#"
]
# Get expansions
x_expansions = [i for i, line in enumerate(matrix) if all(char == "." for char in line)]
y_expansions = [
    i
    for i in range(len(matrix[0]))
    if all(matrix[x][i] == "." for x in range(len(matrix)))
]

# Now, find the shortest path between every pair of coordinates via subtracting the coordinates
# and taking the absolute value of the difference
# But we have to account for the expansions
ONE_MILLION = 1000000
total_distance = 0
for i, first in enumerate(coords):
    for j, second in enumerate(coords):
        if i == j:
            continue
        min_x = min(first[0], second[0])
        min_y = min(first[1], second[1])
        max_x = max(first[0], second[0])
        max_y = max(first[1], second[1])
        while min_x < max_x:
            if min_x in x_expansions:
                total_distance += ONE_MILLION
            else:
                total_distance += 1
            min_x += 1
        while min_y < max_y:
            if min_y in y_expansions:
                total_distance += ONE_MILLION
            else:
                total_distance += 1
            min_y += 1
print(total_distance // 2)
