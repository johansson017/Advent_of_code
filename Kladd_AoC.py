"""
Day 6
"""
def counting_fish():
    data = data_read_test()
    new_fish = 0
    new_fish_day = []
    sum = 0
    exp_list = []
    days = 18
    for i in range(1, days+1):
        for j, fish in enumerate(data):
            if fish != 0:
                data[j] -= 1
            elif fish == 0:
                data[j] = 6
                new_fish += 1
            else:
                data[j] -= 1
        #print(data) # Reggar inte dagen då sista är noll och föder om inte +2
        new_fish_day.append([i, new_fish])
        new_fish = 0
        exp_list.append([0,0])
        print(data)
    print(len(new_fish_day))
    #print(new_fish_day, len(new_fish_day))
    for fish in new_fish_day:
        try:
            exp_list[fish[0]+9] = [fish[0]+9, fish[1]]
        except:
            continue
    #print(new_fish_day[1][1]*2**8, (80-[new_fish_day[1][0])//9)
    #print(new_fish_day[18])
    for fish in new_fish_day:
        remaining_days = days-fish[0]
        #exp_days = remaining_days//7
        #diff_days = remaining_days//9
        #print(fish, remaining_days)
        #print(exp_days, diff_days)
        if remaining_days >= 9:
            sum += fish[1]*2
    print(new_fish_day)
    print(exp_list)

    for fish in exp_list:
        remaining_days = days - fish[0]
        exp_days = remaining_days // 7
        #print(fish[0], fish[1] * 2 ** exp_days)
        sum += fish[1] * 2 ** exp_days

    print(sum + len(data))
    print(len(data))