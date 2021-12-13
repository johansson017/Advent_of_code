"""
Day 13 of Advent of Code
"""
import numpy as np
with open("input_data/day13_data.txt") as file:
    data = []
    for line in file.readlines():
        data.append(line.strip())

folds = []
for i, x in enumerate(data):
    if x == "\n":
        data[i] = ""
    elif "fold" in x:
        folds.append(x)
        data[i] = ""

data = list(map(lambda x: [int(x[0]), int(x[1])], map(lambda x: x.split(","),[x for x in data if x != ""])))
folds = list(map(lambda x: [x[0], int(x[1])], map(lambda x: x.split("="),[x.partition("fold along ")[2] for x in folds])))
#folds = dict((v[0], v[1]) for v in folds)

xmax = max(data,key=lambda x: x[0])[0]
ymax = max(data, key = lambda x: x[1])[1]
coords = np.zeros((ymax+1,xmax+1))

for d in data:
    coords[d[1],d[0]] = 1

#print(np.where(coords == 1)[1])
#print(coords)

def foldings(coords, axis, val):
    old_shape = coords.shape
    if axis == "x":
        index = np.where(coords==1)
        xchange = index[1]
        ychange = index[0]
        new_coords = []
        for x,y in zip(xchange,ychange):
            if x > val:
                newx = coords.shape[1]-x-1
                if [y,x] in new_coords:
                    continue
                new_coords.append([y,newx])
            else:
                if [y,x] in new_coords:
                    continue
                new_coords.append([y,x])
        #print(int(((old_shape[1]-1)/2)))
        coords = np.zeros((old_shape[0],val))
                
    elif axis == "y":
        index = np.where(coords==1)
        xchange = index[1]
        ychange = index[0]
        new_coords = []
        for x,y in zip(xchange,ychange):
            if y > val:
                newy = coords.shape[0]-y-1
                if [y,x] in new_coords:
                    continue
                new_coords.append([newy,x])
            else:
                if [y,x] in new_coords:
                    continue
                new_coords.append([y,x])
                #(int((old_shape[0]-1)/2)
        coords = np.zeros((val,old_shape[1]))

    for d in new_coords:
        coords[d[0],d[1]] = 1
    return coords

for axis,val in folds:
    coords = foldings(coords, axis, val)
    print(sum(sum(coords)))

#with open("code.txt", "w") as file:
#    for line in coords:
#        file.write(f"{line}")