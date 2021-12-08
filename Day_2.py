"""
Day 2 of AdventofCode
"""

with open("input_data/day2_data.txt") as file:
    f = file.read()
    temp = f.split("\n")

data = []
for d in temp:
    t = d.split(" ")
    data.append([t[0], int(t[1])])

depth = 0
hori = 0
for direc, val in data:
    if direc == "forward":
        hori += val
    elif direc == "down":
        depth += val
    elif direc == "up":
        depth -= val

print(f"total value for part 1 is: {hori*depth}")

hori = 0
depth = 0
aim = 0
for direc, val in data:
    if direc == "forward":
        hori += val
        depth += val*aim
    elif direc == "down":
        aim += val
    elif direc == "up":
        aim -= val

print(f"total value for part 2 is: {hori*depth}")


