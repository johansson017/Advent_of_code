"""
Day 12 of Advent of Code
"""
<<<<<<< Updated upstream

data = [x.split("-") for x in [x for x in open("input_data/day12_testdata.txt").read().split("\n")]]
paths = dict()
for k,v in data:
    if k in paths:
        paths[k].append(v)
    else:
        paths[k] = [v]

for k,v in [[x[1], x[0]] for x in data]:
    if k in paths:
        paths[k].append(v)
    else:
        paths[k] = [v]

paths2 = paths.copy()

del_keys = list()
for key in paths.keys():
    if len(paths[key]) == 1:
        if paths[key][0].islower():
            del_keys.append(key)
        else:
            continue

for k in del_keys:
    del paths[k]



# def possible_path(paths, key, tour = []):
#     tour.append(key)
#     for val in paths[key]:
#         if val.islower() and val in tour or val not in paths:
#             continue
#         else:
#             possible_path(paths, val, tour.copy())

#     pathing.append(tour)


def part2_paths(paths2, val, tour = [], visited = set(), can_twice_visit = True):
    # if val.islower() and val in tour:
    #             small_cave = True
    
=======
def data_part(part = 1):
    data = [x.split("-") for x in [x for x in open("input_data/day12_data.txt").read().split("\n")]]
    paths = dict()
    for k,v in data:
        if k in paths:
            paths[k].append(v)
        else:
            paths[k] = [v]

    for k,v in [[x[1], x[0]] for x in data]:
        if k in paths:
            paths[k].append(v)
        else:
            paths[k] = [v]

    paths2 = paths.copy()

    del_keys = list()
    for key in paths.keys():
        if len(paths[key]) == 1:
            if paths[key][0].islower():
                del_keys.append(key)
            else:
                continue

    for k in del_keys:
        del paths[k]
    
    if part == 1:
        return paths
    else:
        return paths2


def part1(paths, key, tour = []):
    tour.append(key)
    for val in paths[key]:
        if val.islower() and val in tour or val not in paths:
            continue
        else:
            part1(paths, val, tour.copy())
        
    if key == "end":
        pathing.append(tour)


def part2(paths, val, tour = [], visited = [], can_twice_visit = True):
>>>>>>> Stashed changes
    if val.islower():
        if val in visited:
            if can_twice_visit and val != "start" and val != "end":
                can_twice_visit = False
            else:
                return None

<<<<<<< Updated upstream
        visited.add(val)

    tour.append(key)

    if key == "end":
        return tour

    pathing = list()
    for val in paths2[key]:
        v1 = part2_paths(paths2, val, tour.copy(), visited.copy(), can_twice_visit)
        if v1 != None:
            pathing.append(tour)
    
    return pathing
    
        
p2 = part2_paths(paths2, "start")
print(p2)

# p1 = ["ab", "ac", "ah", "BC", "A", "T", "n", "n"]
# x = []
# for v in p1:
#     if v.islower():
#         x.append(v)
# print(Counter(x).most_common()[0][1])

#pathing = list()


#tour = list()
#tour.append("start")
#print(paths["b"])
# part2_paths(paths2, "start")
# print(pathing)
# for x in sorted(pathing):
#     print(f"{x}")
#print(pathing)
#print(len(pathing))
#pathing = [x for x in pathing if x[-1] == "end"]
#print(len(pathing))





# ind = list()
# for i,p in enumerate(pathing):
#     if p[-1] != "end":
#         ind.append(i)
# for i in ind:
#     pathing[i] = []

# print(pathing)
=======
        visited.append(val)

    tour.append(val)
    if val == "end":
        return tour

    for v in paths[val]:
        p = part2(paths, v, tour.copy(), visited.copy(), can_twice_visit)
        if p != None:
            pathing.append(p)

if __name__ == "__main__":
    pathing = list()
    paths = data_part()
    part1(paths, "start")
    answer1 = len(pathing)

    pathing = list()
    paths = data_part(2)
    part2(paths, "start")
    answer2 = len(pathing)

    print(f"Part 1 solution: {answer1}\nPart 2 solution: {answer2}")
>>>>>>> Stashed changes

        




