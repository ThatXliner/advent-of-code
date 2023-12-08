from math import lcm

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
start_from_a = [[x, 0] for x in m if x.endswith("A")]
j = 0
while True:
    if all(cur[0][-1] == "Z" for cur in start_from_a):
        break
    for x in instruction:
        for i, cur in enumerate(start_from_a):
            if cur[0][-1] == "Z":
                continue
            start_from_a[i][0] = m[cur[0]][0] if x == "L" else m[cur[0]][1]
            start_from_a[i][1] += 1
print(lcm(*(x[-1] for x in start_from_a)))
