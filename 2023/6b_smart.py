from math import floor
import re

time = int("".join(re.split(r"\s+", input())[1:]))
distance = int("".join(re.split(r"\s+", input())[1:]))
print(time)
print(distance)
# Solve the quadratic
# time_spent_charging * (time - time_spent_charging) > distance =
# time_spent_charging * time - time_spent_charging^2 > distance =
# -time_spent_charging^2 + time * time_spent_charging - distance > 0
# Now use the quadratic formula to solve for time_spent_charging:
time_spent_charging = (-time + (time**2 - 4 * -1 * -distance) ** 0.5) / -2, (
    (-time - (time**2 - 4 * -1 * -distance) ** 0.5) / -2
)
print(floor(time_spent_charging[1] - time_spent_charging[0]))
