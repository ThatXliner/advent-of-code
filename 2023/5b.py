from collections import defaultdict
from itertools import zip_longest, batched
from dataclasses import dataclass

seed_ranges = list(
    map(
        # Convert to a [start, end) range
        lambda x: range(x[0], x[0] + x[1]),
        batched(map(int, input().split(": ")[1].split(" ")), 2),
    )
)
maps = defaultdict(dict)


how_to_get_to = {}

input()
# Simply getting input
while True:
    try:
        src, dst = input().split(" ")[0].split("-to-")
    except EOFError:
        break
    maps[src][dst] = []
    how_to_get_to[dst] = src
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line == "":
            break
        orig = tuple(map(int, line.split(" ")))
        maps[src][dst].append((range(orig[1], orig[1] + orig[2]), orig[0] - orig[1]))


# using is a tuple of (source range, and how to transform)
def convert(r: range, using: list[tuple[range, int]]):
    output = []
    # Transformer sources are disjoint
    for source, transform in using:
        if (
            source.start in r
            or source.stop in r
            or r.start in source
            or r.stop in source
        ):
            orig = range(max(r.start, source.start), min(r.stop, source.stop))
            new = range(
                max(r.start, source.start) + transform,
                min(r.stop, source.stop) + transform,
            )
            output.append((orig, new))
    output.sort(key=lambda x: x[0].start)
    if len(output) == 0:
        return [r]

    last_start = r.start
    final_output = []
    for i, transformed in enumerate(output):
        if last_start < transformed[0].start:
            final_output.append(range(last_start, transformed[0].start))
        final_output.append(transformed[1])
        last_start = transformed[0].stop
        if i == len(output) - 1:
            if last_start < r.stop:
                final_output.append(range(last_start, r.stop))
    return final_output


# Build a path from location to seed
# just in case
cursor = "location"
path = []
while cursor != "seed":
    path.append(cursor)
    cursor = how_to_get_to[cursor]
# To convert it to seed to location we need to reverse it
path.reverse()


location = 999999999999999999
for seed_range in seed_ranges:
    cursor = "seed"
    o = [seed_range]
    for p in path:
        no = []
        for seed in o:
            no.extend(convert(seed, maps[cursor][p]))
        cursor = p
        o = no
    location = min(location, min(map(lambda x: x.start, o)))
print(location)
