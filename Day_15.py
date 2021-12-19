"""
Day 15 Advent of Code
"""
from queue import PriorityQueue
import numpy as np

def data(file):
    arrays = [x for x in open(file).read().split("\n")]
    x = len(arrays[0])
    y = len(arrays)
    grid = np.array([int(x) for x in [x for x in open(file).read().replace("\n","")]]).reshape(x,y)
    valgrid = dict()
    prevgrid = dict()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            valgrid[(i,j)] = np.inf
            prevgrid[(i,j)] = list()

    return grid, valgrid, prevgrid

def part2grid(grid):
    grid = np.concatenate((grid, grid+1, grid + 2, grid + 3, grid + 4), axis = 1)
    grid = np.concatenate((grid, grid+1, grid+2, grid+3, grid+4))
    grid = grid % 9
    ind = grid == 0
    grid[ind] = 9
    
    valgrid = dict()
    prevgrid = dict()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            valgrid[(i,j)] = np.inf
            prevgrid[(i,j)] = list()

    return grid, valgrid, prevgrid

def pathing(grid, valgrid, prevgrid, start, end):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    
    valgrid[(0,0)] = 0

    qSet = PriorityQueue()
    qSet.put((valgrid[0,0], (0,0)))

    while not qSet.empty():
        
        u = qSet.get()
        
        y,x = u[1]

        if u == end:
            break
        
        for i in range(len(dx)):
            ny = y + dy[i]
            nx = x + dx[i]

            if nx < 0 or ny < 0 or nx > end[1] or ny > end[0]:
                continue
            
            temp = valgrid[(y,x)] + grid[(ny,nx)]
            if temp < valgrid[(ny,nx)]:
                qSet.put((valgrid[(ny,nx)], (ny,nx)))
                valgrid[(ny,nx)] = temp

    return valgrid[(end)]

if __name__ == "__main__":
    """ Part 1 """
    scores = list()
    grid, valgrid, prevgrid = data("input_data/day15_data.txt")
    rowmax = len(grid)-1
    colmax = len(grid[0])-1
    end = (rowmax,colmax)
    start = (0,0)
    score1 = pathing(grid, valgrid, prevgrid, start, end)

    """ Part 2 """
    grid, valgrid, prevgrid = part2grid(grid)
    rowmax = len(grid)-1
    colmax = len(grid[0])-1
    end = (rowmax,colmax)
    start = (0,0)
    score2 = pathing(grid, valgrid, prevgrid, start, end)

    print(f"Part 1 Solution: {score1}\nPart 2 Solution: {score2}")



