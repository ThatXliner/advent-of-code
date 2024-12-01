import sys
import re

# print(any([2 ** x.count("?") > 1e9 for x in sys.stdin.read().splitlines()]))
total = 0

for l_count, line in enumerate(sys.stdin.read().splitlines()):
    things, amounts_raw = line.split(" ")
    amounts = [int(x) for x in amounts_raw.split(",")]
    # done = set()
    for i in range(1 << things.count("?")):
        # Given every set of whether or not to replace a question mark, we can
        # calculate the total number of contiguous subsequences that matches
        # the lengths specified by amounts
        # q_count = 0
        test = things
        for j, x in enumerate(things):
            if x == "?":
                if i & (1 << things.count("?", 0, j)):
                    test = test[:j] + "#" + test[j + 1 :]
                else:
                    test = test[:j] + "." + test[j + 1 :]
        # if test in done:
        # break
        # done.add(test)
        # q_count += 1
        # find the lengths of all contiguous subsequences of "#"
        lengths = []
        for x in re.findall(r"#+", test):
            if x.strip():
                # print("e", x.strip())
                lengths.append(len(x))
        # print(test, end=" ")
        print(things, bin(i), test, lengths, amounts)
        if lengths == amounts:
            total += 1
    print(l_count, total)
print(total)
