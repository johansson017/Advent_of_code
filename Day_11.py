"""
Day 11 of Advent of Code
"""

import numpy as np


data = np.array([[int(x) for x in x] for x in open("input_data/day11_data.txt").read().split("\n")])

def neighbour_flash(data):
    flash_count = 0
    dx = [1,1,1,0,0,-1,-1,-1]
    dy = [1,0,-1,1,-1,1,0,-1]

    xlim, ylim = data.shape

    flash_check = np.where(data>9)
    zero_index = list()
    while len(flash_check[0]) != 0:
        for i in range(len(flash_check[0])):
            x = flash_check[0][i]
            y = flash_check[1][i]
            zero_index.append((x,y))
            for j in range(len(dx)):
                xx = x + dx[j]
                yy = y + dy[j]
                if (xx,yy) in zero_index or (xx == xlim or xx < 0) or (yy == ylim or yy < 0):
                    continue
                else:
                    data[xx,yy] += 1

        for coord in zero_index:
            data[coord] = 0

        flash_check = np.where(data>9)

    flash_count = len(zero_index)

    simultaneously = flash_count == data.size

    return data, flash_count, simultaneously

total_flashes = 0
for step in range(2000):
    data += 1
    data, flashes, simultaneously = neighbour_flash(data)
    total_flashes += flashes

    if simultaneously:
        print(step+1)
        break

print(total_flashes)



