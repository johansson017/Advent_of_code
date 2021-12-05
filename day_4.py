"""
Day 4 of Advent of Code
"""
def read_data():
    with open("day4_data.txt") as file:
        number_draw = file.readline()
        number_draw = list(map(int, number_draw.split(",")))
        temp = file.readline()
        boards_temp = []
        for line in file.readlines():
            temp = line.split()
            boards_temp.append(temp)

        boards = []
        temp = []
        for b in boards_temp:
            if b == []:
                boards.append(temp)
                temp = []
                continue
            else:
                temp.append(list(map(int, b)))
        return number_draw, boards

def finding_bingo(boards, number_draw):
    for number in number_draw:
        for board in enumerate(boards):
            for row in enumerate(board[1]):
                for col in enumerate(row[1]):
                    if col[1] == number:
                        boards[board[0]][row[0]][col[0]] = "x"

        for board in enumerate(boards):
            for row in board[1]:
                i = 0
                for val in row:
                    if val == "x":
                        i += 1
                if i == 5:
                    return board[1], number

            for col in [list(e) for e in zip(*board[1])]:
                i = 0
                for val in col:
                    if val == "x":
                        i += 1
                if i == 5:
                    return board[1], number

def calculating_score(board, number):
    score = 0
    for r in board:
        for v in r:
            try:
                score += v
            except:
                continue
    return score*number

def finding_loser(boards, number_draw):
    for number in number_draw:
        for board in enumerate(boards):
            for row in enumerate(board[1]):
                for col in enumerate(row[1]):
                    if col[1] == number:
                        boards[board[0]][row[0]][col[0]] = "x"

        for board in enumerate(boards):
            for row in board[1]:
                i = 0
                for val in row:
                    if val == "x":
                        i += 1
                if i == 5:
                    if len(boards) == 1:
                        return boards, number
                    del boards[board[0]]

            for col in [list(e) for e in zip(*board[1])]:
                i = 0
                for val in col:
                    if val == "x":
                        i += 1
                if i == 5:
                    if len(boards) == 1:
                        return boards, number
                    del boards[board[0]]


if __name__ == "__main__":
    number_draw, boards = read_data()
    bingo_board, winning_number = finding_bingo(boards, number_draw)
    score = calculating_score(bingo_board, winning_number)
    loser_board, losing_number = finding_loser(boards, number_draw)
    score_loser = calculating_score(loser_board[0], losing_number)
    print(f"Final score for winning board is: {score}\nLosing boards score is: {score_loser}")





