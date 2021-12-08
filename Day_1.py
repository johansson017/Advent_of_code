"""
Day1 of AdventofCode
"""
import numpy as np

with open("input_data/sonar_data.txt") as file:
    f = file.read()
    sonar = list(map(int, f.split("\n")))

# part 1
increases = 0
prev = 0
for ind, val in enumerate(sonar):
    if ind == 0:
        continue
    elif val > prev:
        increases += 1
    prev = val

print(increases)

# part 2
increases = 0
vals = []
for ind, val in enumerate(sonar):
    vals.append(val)
    if len(vals) == 4:
        if np.sum(vals[-3:]) > np.sum(vals[0:3]):
            increases += 1
        vals.remove(vals[0])

print(increases)