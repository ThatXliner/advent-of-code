patterns = []
pattern = []
while True:
    try:
        line = input()
    except EOFError:
        break
    if not line:
        patterns.append(pattern)
        pattern = []
        continue
    pattern.append(line)
if pattern:
    patterns.append(pattern)


def find_x_reflection_index(pattern):
    # this is a what I call the Searcher Pattern
    for i in range(1, len(pattern) + 1):
        section_left = pattern[:i]
        section_right = pattern[i:]
        length = min(len(section_left), len(section_right))
        print(section_left[:length], section_right[:length][::-1])
        if section_left[:length] == section_right[:length][::-1]:
            break
    else:
        print("not doun")
        return -1
    print("FOUND", i)
    return i


def find_y_reflection_index(pattern):
    # this is a what I call the Searcher Pattern
    for i in range(len(pattern)):
        section_top = [row[i] for row in pattern[:i]]
        section_bottom = [row[i] for row in pattern[i:]]
        length = min(len(section_top), len(section_bottom))
        print(section_top[:length], section_bottom[:length:-1])
        if section_top[:length] == section_bottom[:length:-1]:
            break
    else:
        print("ynot doun")
    print("yFOUND", i)
    return i


total = 0
for pattern in patterns:
    print("pat\n" + "\n".join(pattern))
    x_reflection_index = find_x_reflection_index(pattern)
    y_reflection_index = find_y_reflection_index(pattern)
    print(x_reflection_index + 1, y_reflection_index + 1)
    total += y_reflection_index + 1
    total += (x_reflection_index + 1) * 100
print(total)
