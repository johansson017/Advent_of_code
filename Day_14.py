"""
Day 14 Advent of Code
"""
def data(file):
    with open(file) as f:
        seq = f.readline().strip()
        rem = f.readline()
        d = f.readlines()
    pair = dict((k,v) for k,v in [x.strip().split(" -> ") for x in d])
    return seq, pair

def part(seq, pair, steps = 0):
    step = 0
    counts = dict()

    for i in range(len(seq)-1):
        p = seq[i]+seq[i+1]
        if p in counts:
            counts[p] += 1
        else:
            counts[p] = 1

    while step < steps:
        temp_counts = dict()
        for key in counts.keys():
            temp = list()
            temp.append(key[0] + pair[key])
            temp.append(pair[key] + key[1])
            for p in temp:
                if p in temp_counts:
                    temp_counts[p] += counts[key]
                else:
                    temp_counts[p] = counts[key]
        counts = temp_counts.copy()
        step += 1

    alphabet_amount = dict()
    i = 1
    for key in counts.keys():
        if key[0] in alphabet_amount:
            alphabet_amount[key[0]] += counts[key]
        else:
            alphabet_amount[key[0]] = counts[key]
        i += 1

    alphabet_amount[seq[-1]] += 1

    x = sorted(alphabet_amount.values())

    return max(x)-min(x)

if __name__ == "__main__":
    seq, pair = data("input_data/day14_data.txt")
    answer1 = part(seq,pair,10)
    answer2 = part(seq,pair,40)
    
    print(f"Solution part 1: {answer1}\nSolution part 2: {answer2}")
    


