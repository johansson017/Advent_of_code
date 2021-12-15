"""
Day 15 Advent of Code
"""
import numpy as np

def data(file):
    arrays = [x for x in open(file).read().split("\n")]
    x = len(arrays[0])
    y = len(arrays)
    return np.array([int(x) for x in [x for x in open(file).read().replace("\n","")]]).reshape(x,y)


def part(grid, x, y):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    undiscovered = [(y,x)]
    # grid(sy,sx) -> row(y),col(x)
    visited = []
    gtemp = 10000

    score = 0
    while undiscovered:
        if x == 9 and y == 9:
            break

        y,x = undiscovered.pop()

        visited.append((y,x))
        score += grid[(y,x)]

        for i in range(len(dx)):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or ny < 0 or nx > 9 or ny > 9 or (ny,nx) in visited:
                continue
            
            temp = score + grid[(ny,nx)]
            if temp < gtemp:
                gtemp = temp
                best = (ny,nx)

        y,x = best
        undiscovered.append((y,x))
        


        


def recursive(grid, y, x):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    visited = []
    visited.append((y,x))

    score = 0
    score += grid[(y,x)]

    if x == 9 and y == 9:
        return score

    for i in range(len(dx)):
        ny = y + dy[i]
        nx = x + dx[i]

        if nx < 0 or ny < 0 or nx > 9 or ny > 9 or (ny,nx) in visited:
            continue

        sum = recursive(grid, ny, nx, visited.copy(), score.copy())
        if sum != None:
            scores.append(sum)




if __name__ == "__main__":
    scores = list()
    grid = data("input_data/day15_testdata.txt")
    print(grid)
    part(grid, 0, 0)



