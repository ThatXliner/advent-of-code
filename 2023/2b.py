import sys

possible = 0

for line in sys.stdin.readlines():
    name, game = line.split(": ")
    id = int(name.split(" ")[1])
    m = {"red": 0, "green": 0, "blue": 0}
    for round in game.split("; "):
        for number, color in map(lambda x: x.split(" "), round.split(", ")):
            m[color.strip()] = max(m[color.strip()], int(number))
    possible += m["red"] * m["green"] * m["blue"]
print(possible)
