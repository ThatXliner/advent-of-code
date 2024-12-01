from collections import defaultdict

seeds = list(map(int, input().split(": ")[1].split(" ")))
maps = defaultdict(dict)


def convert(original, mapping):
    for m in mapping:
        if m[1] <= original <= (m[1] + m[2]):
            return (m[0] - m[1]) + original
    return original


how_to_get_to = {}
input()
while True:
    try:
        src, dst = input().split(" ")[0].split("-to-")
    except EOFError:
        break
    maps[src][dst] = []
    how_to_get_to[dst] = src
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line == "":
            break
        maps[src][dst].append(tuple(map(int, line.split(" "))))
cursor = "location"
path = []
while cursor != "seed":
    path.append(cursor)
    cursor = how_to_get_to[cursor]
path.reverse()
location = 99999999999
for seed in seeds:
    n = seed
    cursor = "seed"
    for p in path:
        n = convert(n, maps[cursor][p])
        cursor = p
    location = min(location, n)
print(location)
