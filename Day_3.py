"""
Day 3 of AdventofCode
"""
from collections import Counter
with open("input_data/day3_data.txt") as file:
    f = file.read()
    data = f.split("\n")

logg = dict()
for d in data:
    j = 0
    for i in d:
        logg[f"{j}"] = []
        j += 1

for d in data:
    j = 0
    for i in d:
        logg[f"{j}"].append(i)
        j += 1

gamma = []
epsilon = []
for d in logg:
    c = Counter(logg[f"{d}"])

    if c["0"] > c["1"]:
        gamma.append(0)
        epsilon.append(1)
    else:
        gamma.append(1)
        epsilon.append(0)

gammaR = 0
epsilonR = 0
i = 0
for ng, ne in enumerate(zip(reversed(gamma), reversed(epsilon))):
    gammaR += ne[0]*2**ng
    epsilonR += ne[1]*2**ng

print(f"Power consumption is: {gammaR*epsilonR}")


"""
Second part
"""
oxygen = data
scrubber = data

for index in range(len(oxygen[0])):
    ones = 0
    zeros = 0
    saved_ones = []
    saved_zeros = []
    for b in oxygen:
        if b[index] == "1":
            ones += 1
            saved_ones.append(b)
        else:
            zeros += 1
            saved_zeros.append(b)

    if ones >= zeros:
        oxygen = saved_ones
    else:
        oxygen = saved_zeros

    if len(oxygen) == 1:
        o_val = 0
        for i,n in enumerate(reversed(oxygen[0])):
            o_val += int(n) * 2 ** i
        break

for index in range(len(scrubber[0])):
    ones = 0
    zeros = 0
    saved_ones = []
    saved_zeros = []
    for b in scrubber:
        if b[index] == "1":
            ones += 1
            saved_ones.append(b)
        else:
            zeros += 1
            saved_zeros.append(b)

    if ones < zeros:
        scrubber = saved_ones
    else:
        scrubber = saved_zeros

    if len(scrubber) == 1:
        s_val = 0
        for i,n in enumerate(reversed(scrubber[0])):
            s_val += int(n)*2**i
        break



print(f"Life support rating is: {o_val*s_val}")