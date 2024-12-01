def HASH(s):
    cur = 0
    for x in s:
        cur += ord(x)
        cur *= 17
        cur %= 256
    return cur


print(sum(map(HASH, input().split(","))))
