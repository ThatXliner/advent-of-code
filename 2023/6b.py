import re

time = int("".join(re.split(r"\s+", input())[1:]))
distance = int("".join(re.split(r"\s+", input())[1:]))
print(time)
print(distance)
t = 0
for time_spent_charging in range(time):
    speed = time_spent_charging
    t += speed * (time - time_spent_charging) > distance
print(t)
