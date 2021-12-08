"""
Day 7 of Advent of Code
"""

def data_read(txt):
    with open(txt) as file:
        data = list(map(int, file.read().strip().split(",")))
    return data

def horizontal_dist(data, part2=False):
    best_diff = None
    for i in range(min(data), round(max(data))):
        diff = 0
        for d in data:
            temp = abs(d-i)
            if part2:
                diff += ((float(1+temp))*float((temp/2)))
            else:
                diff += temp

        if best_diff == None:
            best_diff = diff
        elif diff < best_diff:
            best_diff = diff

    return int(best_diff)

if __name__== "__main__":
    data = data_read("input_data/day7_data.txt")
    print(f"Least distance for crabs part 1: {horizontal_dist(data)}, part 2: {horizontal_dist(data,True)}")
