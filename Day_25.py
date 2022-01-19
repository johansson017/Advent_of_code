""" Day 25 of Advent of Code """
import numpy as np

def data(file):
    with open(file) as file:
        lines = [x for x in file.read().split("\n")]
        y = len(lines)
        x = len(lines[0])
        grid = np.zeros((y,x),dtype=np.str)

        for row , rowval in enumerate(lines):
            for col, val in enumerate(rowval):
                grid[row,col] = val

    return grid

def movement(grid):
    still_going = True
    num = 0
    while still_going:
        still_going = True
        num += 1
        indsave = []
        for row, rowval in enumerate(grid):
            for col, colval in enumerate(rowval):
                if colval == ">" and grid[row][(col+1)%len(rowval)] == ".":
                    indsave.append(f"{row},{col},{colval}")

        if indsave:
            for val in indsave:
                row, col, sym = val.split(",")
                row = int(row)
                col = int(col)
                grid[row][col] = "."
                if sym == "v":
                    grid[(row+1)%len(grid)][col] = sym
                else:
                    grid[row][(col+1)%len(grid[0])] = sym
        else:
            still_going = False

        for row, rowval in enumerate(grid):
            for col, colval in enumerate(rowval):
                if colval == "v" and grid[(row+1)%len(grid)][col] == ".":
                    indsave.append(f"{row},{col},{colval}")

        # indsave = sorted(indsave, key = lambda x: x[-1])
        
        if indsave:
            for val in indsave:
                row, col, sym = val.split(",")
                row = int(row)
                col = int(col)
                grid[row][col] = "."
                if sym == "v":
                    grid[(row+1)%len(grid)][col] = sym
                else:
                    grid[row][(col+1)%len(grid[0])] = sym
            
            still_going = True
    return num


if __name__ == "__main__":
    grid = data("input_data/day25_data.txt")

    result = movement(grid)
    
    print(result)