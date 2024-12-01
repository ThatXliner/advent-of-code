import sys

print(
    sum(
        [
            int(str((e := [int(x) for x in line if x in "1234567890"])[0]) + str(e[-1]))
            for line in sys.stdin.readlines()
        ]
    )
)
