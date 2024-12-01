import sys

possible = 0
m = {"red": 12, "green": 13, "blue": 14}
for line in sys.stdin.readlines():
    name, game = line.split(": ")
    id = int(name.split(" ")[1])
    bad = False
    for round in game.split("; "):
        for number, color in map(lambda x: x.split(" "), round.split(", ")):
            if int(number) > m[color.strip()]:
                bad = True
                break
        if bad:
            break
    if bad:
        continue
    possible += id
print(possible)
