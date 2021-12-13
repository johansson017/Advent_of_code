"""
Day 10 of Advent of Code
"""
def day10(file):
    left = ["(", "[", "{", "<"]
    right = [")", "]", "}", ">"]

    points = [3,57,1197,25137]
    points2 = [1,2,3,4]

    pair, point_pair1, point_pair2 = dict(), dict(), dict()
    for l,r in zip(left,right):
        pair[l] = r
    for r, p in zip(right,points):
        point_pair1[r] = p
    for r,p in zip(right,points2):
        point_pair2[r] = p

    strings = [line for line in open(file).read().split("\n")]
    
    scores = list()
    sum = 0
    for line in strings:
        visited = list()
        for i, char in enumerate(line):
            if char in left:
                visited.append(char)
            elif char in right:
                if char == pair[visited.pop()]:
                    if i != len(line)-1:
                        continue
                else:
                    sum += point_pair1[char]
                    break
            if i == len(line)-1:
                score = 0
                for char in reversed(visited):
                    score = score*5+point_pair2[pair[char]]
                scores.append(score)

    mid_num = sorted(scores)[int(len(scores)/2-0.5)]

    return sum, mid_num

if __name__ == "__main__":
    test = False
    part1,part2 = day10(("input_data/day10_testdata.txt" if test == True else "input_data/day10_data.txt"))
    print(f"Result for part 1: {part1}\nResult for part 2: {part2}")









