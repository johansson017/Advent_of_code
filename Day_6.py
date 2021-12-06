"""
Day 6 of Advent of Code
"""
def data_read():
    with open("day6_data.txt") as file:
        data = file.readline().strip()
        data = list(map(int, data.split(",")))
        return data

def counting_fish(data, days):
    new_fish = 0
    new_fish_list = [0 for i in range(9)]
    for i in range(0, days):
        for j, fish in enumerate(data):
            if fish != 0:
                data[j] -= 1
            elif fish == 0:
                data[j] = 6
                new_fish += 1
            else:
                data[j] -= 1

        temp = new_fish_list[-1]
        new_fish_list = [new_fish + new_fish_list[-1]] + new_fish_list[:-1]
        new_fish_list[2] += temp
        new_fish = 0

    return sum(new_fish_list) + len(data)


if __name__ == "__main__":
    print(f"Number of fishes for  80 days: {counting_fish(data_read(),80)}")
    print(f"Number of fishes for 256 days: {counting_fish(data_read(), 256)}")