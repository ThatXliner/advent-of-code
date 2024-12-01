import sys

total = 0
games = {}


def do_win(id, score):
    global total
    total += 1
    for g in range(id + 1, id + score + 1):
        do_win(g, games[g])


for game_id, card in enumerate(sys.stdin.read().splitlines(), start=1):
    game = card.split(":")[1].strip()
    win, you = game.split(" | ")
    win = set(map(int, (x for x in win.strip().split(" ") if x)))
    you = list(map(int, (x for x in you.strip().split(" ") if x)))
    score = 0
    for item in you:
        if item in win:
            score += 1
    games[game_id] = score
for game, score in games.items():
    do_win(game, score)
print(total)
