"""
Day 8 of Advent of Code
"""
def puzzle_input():
    with open("input_data/day8_data.txt") as file:
        temp = file.read()
        temp = temp.split("\n")
        tdata = list()
        all_data = list()
        for t in temp:
            all_data.append(t.strip())
        for t in temp:
            t = t.split("|")
            tdata.append(t[1])
        data1 = list()
        for td in tdata:
            td = td.strip().split(" ")
            for d in td:
                data1.append(d)
    return all_data, data1

def decoding(alphabet, right):
    numb_index = [[0,1,2,4,5,6], [2,5], [0,2,3,4,6], [0,2,3,5,6], [1,2,3,5], [0,1,3,5,6], [0,1,3,4,5,6], [0,2,5], list(range(7)), [0,1,2,3,5,6]]
    numbers = [sorted([alphabet[i] for i in number]) for number in numb_index]
    number_string = ""
    for ele in right:
        listele= sorted([l for l in ele])
        for i, number in enumerate(numbers):
            if listele == number:
                number_string = number_string+str(i)
    return int(number_string)

def part1(data):
    return sum([len(element) in [2,4,3,7] for element in data])

def part2(data):
    total_output = 0
    letter_amount = [6,2,5,5,4,5,6,3,7,6]
    for each in data:
        each = each.split("|")
        left = each[0].strip().split(" ")
        right = each[1].strip().split(" ")
        alphabet = [" " for i in range(7)]
        uniques = []
        fives = []
        for ele in left:
            n_match = 0
            for i, letters in enumerate(letter_amount):
                if len(ele) == letters:
                    n_match += 1
                    m_letter = ele
                    index = i
            if len(ele) == 5:
                fives.append(ele)
            if n_match == 1:
                uniques.append((index, m_letter))

        uniques = sorted(uniques)
        uni7 = [lett not in uniques[0][1] for lett in uniques[2][1]] # rätt
        alphabet[0] = uniques[2][1][uni7.index(True)]
        unique_alphabet = [u for ele in uniques[:3] for u in ele[1]]
        uni8 = []
        for ele in uniques[3][1]:
            if ele not in unique_alphabet:
                uni8.append(ele)

        alphabet_fives = [l for ele in fives for l in ele]
        two_fives = Counter(alphabet_fives).most_common()[-2:]
        three_fives = Counter(alphabet_fives).most_common()[:3]
        alpha_twofives = [l[0] for l in two_fives]

        for l_eight in uni8:
            if l_eight not in alpha_twofives:
                alphabet[6] = l_eight

        for ele in two_fives:
            l, am = ele
            if l in uniques[1][1]:
                alphabet[1] = l

                for five in fives:
                    if l not in five:
                        for l_one in uniques[0][1]:
                            if l_one not in five:
                                alphabet[5] = l_one
            else:
                alphabet[4] = l

        for ele in three_fives:
            l, am = ele
            if l in uniques[1][1]:
                alphabet[3] = l

        for l_one in uniques[0][1]:
            if l_one not in alphabet:
                alphabet[2] = l_one

        value = decoding(alphabet, right)
        total_output += value

    return total_output

if __name__=="__main__":
    from collections import Counter
    data2, data1 = puzzle_input()
    print(f"Answer for part 1 is: {part1(data1)}")
    print(f"Answer for part 2 is: {part2(data2)}")











