import sys
import re
from functools import cache

# print(any([2 ** x.count("?") > 1e9 for x in sys.stdin.read().splitlines()]))
total = 0


def validate(things: str, amounts: list[int]) -> bool:
    for i, found in enumerate(re.findall(r"#+", things)):
        if len(found) != amounts[i]:
            return False
    return True


cache = {}


# @cache
def get_counts(things: str, amounts: tuple[int]) -> None:
    global total
    breakpoint()
    # if key := (things, amounts) in cache:
    #     return cache[key]
    # cache[key] = None
    if len(amounts) == 1:
        output = (
            re.search(
                r"^\.*(\?|#){" + str(amounts[0]) + r"}(\.)*$",
                things,
                flags=re.MULTILINE,
            )
            is not None
        )
        total += output
        return
        # return output
    # output = 0
    for chunk in re.finditer(r"(\?|#)+", things):
        start = chunk.start()
        if things[:start].count("#") != 0:
            break
        end = chunk.start() + amounts[0]
        while end <= chunk.end():
            get_counts(things[end:], amounts[1:])
            end += 1
            start += 1
    # for i, x in enumerate(things):
    #     if x != "?":
    #         continue
    #     try_hash = things[:i] + "#" + things[i + 1 :]
    #     if len(re.search(r"#+", try_hash).group(0)) == amounts[0]:
    #         output += max(0, get_counts(try_hash[i + 1 :], amounts[1:]))

    #     try_none = things[:i] + "." + things[i + 1 :]
    #     if len(re.search(r"#+", try_none).group(0)) == amounts[0]:
    #         output += max(0, get_counts(try_none[i + 1 :], amounts[1:]))
    # return output


a_total = 0
for l_count, line in enumerate(sys.stdin.read().splitlines()):
    things, amounts_raw = line.split(" ")
    amounts = [int(x) for x in amounts_raw.split(",")] * 5
    output = ""
    for _ in range(5):
        output += things + "?"
    output = output[:-1]
    print("hey", output)
    get_counts(output, tuple(amounts))
    a_total += total
    total = 0
    cache = {}
print(a_total)
