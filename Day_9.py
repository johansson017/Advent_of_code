"""
Day 9 of Advent of Code
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from functools import reduce

def explore(x, y, mapBinary):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    queue = []
    visited = []
    queue.append((x,y))
    while queue:
        x,y = queue.pop()
        visited.append((x,y))

        for ind in range(4):
            xx = x + dx[ind]
            yy = y + dy[ind]
            if xx == lrow or xx == -1 or yy == lcol or yy == -1:
                continue
            if mapBinary[xx][yy] == 1:
                mapBinary[xx][yy] = 2
                if (xx,yy) not in visited:
                    queue.append((xx,yy))
    return visited

def part1(x,y,mapNumbers):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    if mapNumbers[x,y] == 9:
        return False

    for ind in range(4):
        xx = x + dx[ind]
        yy = y + dy[ind]
        if xx == lrow or xx == -1 or yy == lcol or yy == -1:
            continue
        if mapNumbers[xx,yy] < mapNumbers[x,y]:
            return False
    return True

def plotting(mapBinary):
    ax = sns.heatmap(mapBinary, linewidths=0.5, square=True, cmap="binary", cbar=False, xticklabels=False, yticklabels=False)
    plt.show()

def day_9(mapNumbers, mapBinary, plot=False):
    sum = 0
    basins = []
    for i, row in enumerate(mapNumbers):
        for j, data_col in enumerate(row):
            if part1(i,j,mapNumbers):
                sum += mapNumbers[i,j]+1
                basins.append(len(explore(i, j, mapBinary)))

    basins = sorted(basins, reverse=True)

    if plot:
        plotting(mapBinary)

    return sum, reduce(lambda x,y: x*y, basins[:3])

if __name__ == "__main__":
    grid = [grid for grid in open("input_data/day9_data.txt").read().split("\n")]
    lrow = len(grid)
    lcol = len(grid[0])

    mapBinary = np.array([1 if x != "9" else 0 for x in grid for x in x])
    mapBinary = mapBinary.reshape([(lrow), (lcol)])

    mapNumbers = np.array([int(x) for x in grid for x in x])
    mapNumbers = mapNumbers.reshape([lrow, lcol])

    result1, result2 = day_9(mapNumbers, mapBinary, False)
    print(f"~~~~~~~~~~ Results for Day 9 ~~~~~~~~~~\nPart 1: {result1}\nPart 2: {result2}\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


