import re

times = list(map(int, re.split(r"\s+", input())[1:]))
distances = list(map(int, re.split(r"\s+", input())[1:]))
print(times)
print(distances)
total = 1
for i, time in enumerate(times):
    t = 0
    for time_spent_charging in range(time):
        t += time_spent_charging * (time - time_spent_charging) > distances[i]
    total *= t
print(total)
