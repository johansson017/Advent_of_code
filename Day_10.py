"""
Day 10 of Advent of Code
"""

left = ["(", "[", "{", "<"]
right = [")", "]", "}", ">"] #3,57,1197,25137
points = [3,57,1197,25137]
pair = dict()
point_pair = dict()

for l,r in zip(left,right):
    pair[l] = r

for r, p in zip(right,points):
    point_pair[r] = p

with open("input_data/day10_data.txt") as file:
    temp = file.read().split("\n")
    
sum = 0
for line in temp:
    visited = []
    for char in line:
        if char in left:
            visited.append(char)
        elif char in right:
            if char == pair[visited.pop()]:
                continue
            else:
                sum += point_pair[char]
                break
print(sum)






