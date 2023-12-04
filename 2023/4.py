import sys

total = 0
for card in sys.stdin.read().splitlines():
    game = card.split(":")[1].strip()
    win, you = game.split(" | ")
    win = set(map(int, (x for x in win.strip().split(" ") if x)))
    you = list(map(int, (x for x in you.strip().split(" ") if x)))
    score = 0
    for item in you:
        if item in win:
            if score == 0:
                score = 1
            else:
                score *= 2
    total += score
print(total)
