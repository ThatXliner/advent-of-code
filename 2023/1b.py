import sys
import regex as re

f = 0
e = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for line in sys.stdin.readlines():
    a = []
    for x in re.findall(r"[0-9]|(?:" + "|".join(e) + ")", line, overlapped=True):
        print(x)
        if x in e:
            a.append(e.index(x) + 1)
        else:
            try:
                a.append(int(x))
            except:
                pass
    print(a)
    f += int(str(a[0]) + str(a[-1]))
print(f)
