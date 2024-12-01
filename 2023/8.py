instruction = input()
input()
m = {}
while True:
    try:
        e = input()
    except EOFError:
        break
    name, lr = e.split(" = ")
    m[name] = lr[1:-1].split(", ")
cur = "AAA"
i = 0
while True:
    if cur == "ZZZ":
        break
    for x in instruction:
        if x == "L":
            cur = m[cur][0]
        else:
            cur = m[cur][1]
        i += 1
print(i)
