import sys

x = 0
for line in sys.stdin.readlines():
    e = [int(x) for x in line if x in "1234567890"]
    x += int(str(e[0]) + str(e[-1]))
print(x)
