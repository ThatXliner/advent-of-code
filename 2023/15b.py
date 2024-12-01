from collections import defaultdict


def HASH(s):
    cur = 0
    for x in s:
        cur += ord(x)
        cur *= 17
        cur %= 256
    return cur


hashmap = defaultdict(list)
for x in input().split(","):
    if x[-1] == "-":
        key = x[:-1]
        # remove relevant key
        hashmap[HASH(key)] = [y for y in hashmap[HASH(key)] if y[0] != key]
    elif "=" in x:
        key, value = x.split("=")
        for i, x in enumerate(hashmap[HASH(key)]):
            if x[0] == key:
                hashmap[HASH(key)][i] = key, int(value)
                break
        else:
            hashmap[HASH(key)].append((key, int(value)))
print(hashmap)
total = 0
for box_number, lenses in hashmap.items():
    for i, x in enumerate(lenses, start=1):
        total += (1 + box_number) * (i) * x[1]
print(total)
